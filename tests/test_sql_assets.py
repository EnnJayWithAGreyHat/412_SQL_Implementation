from __future__ import annotations

import unittest
from pathlib import Path
import shutil
from uuid import uuid4

from backend.output_generator import generate_output_text
from backend.query_engine import compile_named_query
from backend.sql_assets import render_all_assets, write_project_sql_assets


class SqlAssetTests(unittest.TestCase):
    def test_sql_assets_are_written_with_expected_files(self) -> None:
        temp_dir = Path.cwd() / f".tmp_sql_assets_{uuid4().hex}"
        temp_dir.mkdir()
        try:
            written = write_project_sql_assets(temp_dir)
            self.assertEqual(
                set(written),
                {"ddl.sql", "insert.sql", "query.sql", "drop.sql", "run.sql"},
            )
            for path in written.values():
                self.assertTrue(path.exists())
                self.assertGreater(path.stat().st_size, 0)
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_run_sql_uses_source_syntax_required_by_assignment(self) -> None:
        assets = render_all_assets()
        run_sql = assets["run.sql"]
        self.assertIn("SOURCE ddl.sql;", run_sql)
        self.assertIn("SOURCE insert.sql;", run_sql)
        self.assertIn("SOURCE query.sql;", run_sql)
        self.assertIn("SOURCE drop.sql;", run_sql)

    def test_query_sql_contains_five_queries(self) -> None:
        query_sql = render_all_assets()["query.sql"]
        self.assertEqual(query_sql.count("SELECT"), 5)

    def test_insert_sql_has_at_least_five_rows_per_table(self) -> None:
        insert_sql = render_all_assets()["insert.sql"]
        for table_name in (
            "student",
            "documents",
            "course",
            "university",
            "offers",
            "contains",
            "downloaded_courses",
            "enrolled",
            "uploaded",
        ):
            count = insert_sql.count(f"INSERT INTO {table_name} ")
            self.assertGreaterEqual(count, 5, msg=f"{table_name} only had {count} rows")

    def test_mysql_parameter_compilation_preserves_order(self) -> None:
        sql = "SELECT * FROM student WHERE major = :major AND user_name <> :user_name"
        compiled_sql, params = compile_named_query(
            sql,
            {"major": "cse", "user_name": "John Smith"},
            dialect="mysql",
        )
        self.assertEqual(
            compiled_sql,
            "SELECT * FROM student WHERE major = %s AND user_name <> %s",
        )
        self.assertEqual(params, ["cse", "John Smith"])

    def test_output_generator_contains_query_results_section(self) -> None:
        output = generate_output_text()
        self.assertIn("== QUERY RESULTS ==", output)
        self.assertIn("[User Uploads]", output)
        self.assertIn("[Course Material Summary]", output)


if __name__ == "__main__":
    unittest.main()
