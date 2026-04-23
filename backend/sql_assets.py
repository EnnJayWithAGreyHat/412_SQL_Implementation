"""Render assignment SQL assets from the canonical catalog."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .catalog import DROP_ORDER, PROJECT_ROOT, QUERIES, SEEDS, TABLES


def _comment_block(title: str, subtitle: str) -> str:
    return "\n".join(
        (
            "/*",
            "** ----------------------------------------------------------------------------",
            f"** {title}",
            f"** {subtitle}",
            "** ----------------------------------------------------------------------------",
            "*/",
        )
    )


def _sql_literal(value: Any) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, str):
        escaped = value.replace("'", "''")
        return f"'{escaped}'"
    return str(value)


def _render_query_sample_sql(sql: str, params: dict[str, Any]) -> str:
    rendered = sql
    for name, value in params.items():
        rendered = rendered.replace(f":{name}", _sql_literal(value))
    return rendered


def render_ddl_sql() -> str:
    sections: list[str] = [
        _comment_block(
            "ddl.sql",
            "Create every table from the study-material relational schema in MySQL.",
        )
    ]

    for table in TABLES:
        body = ",\n    ".join((*table.columns, *table.constraints))
        sections.append(
            _comment_block(
                f"Create {table.name}",
                table.description,
            )
        )
        sections.append(f"CREATE TABLE {table.name} (\n    {body}\n);")
        for index_statement in table.indexes:
            sections.append(index_statement + ";")

    return "\n\n".join(sections) + "\n"


def render_insert_sql() -> str:
    sections: list[str] = [
        _comment_block(
            "insert.sql",
            "Insert seed data into every table with explicit column lists.",
        )
    ]

    for seed in SEEDS:
        sections.append(
            _comment_block(
                f"Insert rows into {seed.table_name}",
                f"Populate {seed.table_name} with {len(seed.rows)} seed rows.",
            )
        )
        columns = ", ".join(seed.columns)
        for row in seed.rows:
            values = ", ".join(_sql_literal(value) for value in row)
            sections.append(
                f"INSERT INTO {seed.table_name} ({columns}) VALUES ({values});"
            )

    return "\n\n".join(sections) + "\n"


def render_query_sql() -> str:
    sections: list[str] = [
        _comment_block(
            "query.sql",
            "Five assignment queries that demonstrate joins, filters, and aggregation.",
        )
    ]

    for index, query in enumerate(QUERIES, start=1):
        subtitle = query.description
        if query.sample_params:
            samples = ", ".join(
                f"{name}={value}" for name, value in query.sample_params.items()
            )
            subtitle = f"{subtitle} Sample parameters: {samples}."

        sections.append(
            _comment_block(
                f"Query {index}: {query.title}",
                subtitle,
            )
        )
        sections.append(
            _render_query_sample_sql(query.sql, dict(query.sample_params)) + ";"
        )

    return "\n\n".join(sections) + "\n"


def render_drop_sql() -> str:
    sections: list[str] = [
        _comment_block(
            "drop.sql",
            "Drop tables in dependency order so the schema can be rebuilt cleanly.",
        )
    ]

    for table_name in DROP_ORDER:
        sections.append(f"DROP TABLE IF EXISTS {table_name};")

    return "\n\n".join(sections) + "\n"


def render_run_sql() -> str:
    sections: list[str] = [
        "-- Run this file from MySQL Workbench or the MySQL CLI after selecting a schema.",
        "-- Keep ddl.sql, insert.sql, query.sql, drop.sql, and run.sql in the same directory.",
        "",
        "-- Create the schema objects.",
        "SOURCE ddl.sql;",
        "",
        "-- Show the table structures.",
    ]

    for table in TABLES:
        sections.append(f"DESCRIBE {table.name};")

    sections.extend(
        (
            "",
            "-- Seed the tables.",
            "SOURCE insert.sql;",
            "",
            "-- Show the table contents in deterministic order for verification.",
        )
    )

    for table in TABLES:
        order_by = ", ".join(table.select_order_by) if table.select_order_by else "1"
        sections.append(f"SELECT * FROM {table.name} ORDER BY {order_by};")

    sections.extend(
        (
            "",
            "-- Run the five assignment queries.",
            "SOURCE query.sql;",
            "",
            "-- Drop the schema objects.",
            "SOURCE drop.sql;",
        )
    )

    return "\n".join(sections) + "\n"


def render_all_assets() -> dict[str, str]:
    return {
        "ddl.sql": render_ddl_sql(),
        "insert.sql": render_insert_sql(),
        "query.sql": render_query_sql(),
        "drop.sql": render_drop_sql(),
        "run.sql": render_run_sql(),
    }


def write_project_sql_assets(project_root: Path | None = None) -> dict[str, Path]:
    root = project_root or PROJECT_ROOT
    written_files: dict[str, Path] = {}
    for filename, contents in render_all_assets().items():
        path = root / filename
        path.write_text(contents, encoding="utf-8")
        written_files[filename] = path
    return written_files
