"""Frontend-ready service layer for browsing tables and running catalog queries."""

from __future__ import annotations

import sqlite3
from typing import Any

from .catalog import QUERIES, SEEDS, TABLES, get_query, get_table
from .query_engine import compile_named_query


def _rows_to_dicts(cursor: sqlite3.Cursor) -> list[dict[str, Any]]:
    if cursor.description is None:
        return []
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row, strict=False)) for row in cursor.fetchall()]


def _format_column_metadata(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "column_name": row["name"],
        "data_type": row["type"],
        "not_null": bool(row["notnull"]),
        "default_value": row["dflt_value"],
        "primary_key_position": row["pk"],
    }


class DatabaseService:
    """SQLite-backed implementation of the backend contract."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def create_in_memory(cls) -> "DatabaseService":
        return cls(sqlite3.connect(":memory:"))

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> "DatabaseService":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def create_schema(self) -> None:
        for table in TABLES:
            table_body = ",\n    ".join((*table.columns, *table.constraints))
            statement = f"CREATE TABLE {table.name} (\n    {table_body}\n)"
            self.connection.execute(statement)
            for index_statement in table.indexes:
                self.connection.execute(index_statement)
        self.connection.commit()

    def seed_data(self) -> None:
        for seed in SEEDS:
            placeholders = ", ".join("?" for _ in seed.columns)
            columns = ", ".join(seed.columns)
            statement = (
                f"INSERT INTO {seed.table_name} ({columns}) "
                f"VALUES ({placeholders})"
            )
            self.connection.executemany(statement, seed.rows)
        self.connection.commit()

    def bootstrap(self) -> None:
        self.create_schema()
        self.seed_data()

    def drop_schema(self) -> None:
        # Child tables are dropped first to mirror the committed SQL assets.
        from .catalog import DROP_ORDER

        for table_name in DROP_ORDER:
            self.connection.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.connection.commit()

    def list_tables(self) -> list[dict[str, Any]]:
        tables: list[dict[str, Any]] = []
        for table in TABLES:
            row_count = self.connection.execute(
                f"SELECT COUNT(*) AS row_count FROM {table.name}"
            ).fetchone()["row_count"]
            tables.append(
                {
                    "table_name": table.name,
                    "description": table.description,
                    "row_count": row_count,
                }
            )
        return tables

    def describe_table(self, table_name: str) -> dict[str, Any]:
        table = get_table(table_name)
        cursor = self.connection.execute(f"PRAGMA table_info({table.name})")
        columns = [_format_column_metadata(row) for row in cursor.fetchall()]
        row_count = self.connection.execute(
            f"SELECT COUNT(*) AS row_count FROM {table.name}"
        ).fetchone()["row_count"]
        return {
            "table_name": table.name,
            "description": table.description,
            "row_count": row_count,
            "columns": columns,
        }

    def fetch_rows(self, table_name: str, *, limit: int = 100) -> dict[str, Any]:
        table = get_table(table_name)
        order_by = ", ".join(table.select_order_by) if table.select_order_by else "1"
        cursor = self.connection.execute(
            f"SELECT * FROM {table.name} ORDER BY {order_by} LIMIT ?",
            (limit,),
        )
        rows = _rows_to_dicts(cursor)
        columns = list(rows[0].keys()) if rows else [column.split()[0] for column in table.columns]
        total_count = self.connection.execute(
            f"SELECT COUNT(*) AS row_count FROM {table.name}"
        ).fetchone()["row_count"]
        return {
            "table_name": table.name,
            "description": table.description,
            "columns": columns,
            "row_count": len(rows),
            "total_count": total_count,
            "rows": rows,
        }

    def list_queries(self) -> list[dict[str, Any]]:
        query_list: list[dict[str, Any]] = []
        for query in QUERIES:
            query_list.append(
                {
                    "key": query.key,
                    "title": query.title,
                    "description": query.description,
                    "parameters": [
                        {
                            "name": parameter.name,
                            "description": parameter.description,
                            "sample_value": parameter.sample_value,
                        }
                        for parameter in query.parameters
                    ],
                    "sample_params": dict(query.sample_params),
                }
            )
        return query_list

    def run_query(
        self,
        key: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        query = get_query(key)
        compiled_sql, compiled_params = compile_named_query(
            query.sql,
            params or dict(query.sample_params),
            dialect="sqlite",
        )
        cursor = self.connection.execute(compiled_sql, compiled_params)
        rows = _rows_to_dicts(cursor)
        columns = list(rows[0].keys()) if rows else []
        return {
            "key": query.key,
            "title": query.title,
            "description": query.description,
            "sql": compiled_sql,
            "columns": columns,
            "row_count": len(rows),
            "rows": rows,
        }
