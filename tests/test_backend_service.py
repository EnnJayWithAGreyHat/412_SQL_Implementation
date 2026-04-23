from __future__ import annotations

import sqlite3
import unittest

from backend.service import DatabaseService


class DatabaseServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = DatabaseService.create_in_memory()
        self.service.bootstrap()

    def tearDown(self) -> None:
        self.service.close()

    def test_bootstrap_creates_all_tables_with_seed_rows(self) -> None:
        tables = {table["table_name"]: table for table in self.service.list_tables()}
        self.assertEqual(len(tables), 9)
        for table_name, expected_minimum in {
            "student": 8,
            "documents": 10,
            "course": 8,
            "university": 8,
            "offers": 8,
            "contains": 8,
            "downloaded_courses": 8,
            "enrolled": 8,
            "uploaded": 10,
        }.items():
            self.assertIn(table_name, tables)
            self.assertGreaterEqual(tables[table_name]["row_count"], expected_minimum)

    def test_assignment_queries_return_expected_rows(self) -> None:
        uploads = self.service.run_query("user_uploads")
        self.assertEqual(uploads["row_count"], 10)

        passing_documents = self.service.run_query("passing_documents")
        self.assertEqual(passing_documents["row_count"], 9)
        returned_document_ids = {row["document_id"] for row in passing_documents["rows"]}
        self.assertNotIn(7, returned_document_ids)

        asu_students = self.service.run_query(
            "students_by_university",
            {"university_name": "ASU"},
        )
        self.assertEqual(asu_students["row_count"], 1)
        self.assertEqual(asu_students["rows"][0]["user_name"], "Jennifer Ortiz")

        cse_students = self.service.run_query("students_by_major", {"major": "cse"})
        self.assertEqual(cse_students["row_count"], 2)
        self.assertEqual(
            {row["user_name"] for row in cse_students["rows"]},
            {"John Smith", "Ramesh Fahr"},
        )

        course_summary = self.service.run_query("course_material_summary")
        self.assertEqual(course_summary["row_count"], 10)
        bio213_row = next(
            row for row in course_summary["rows"] if row["course_id"] == "BIO213"
        )
        self.assertEqual(bio213_row["university_name"], "UNASSIGNED")
        self.assertEqual(bio213_row["linked_documents"], 0)

    def test_invalid_foreign_key_insert_is_rejected(self) -> None:
        with self.assertRaises(sqlite3.IntegrityError):
            self.service.connection.execute(
                """
                INSERT INTO uploaded (user_name, document_id, upload_date)
                VALUES (?, ?, ?)
                """,
                ("Ghost User", 999, "2026-04-23"),
            )

    def test_cascade_delete_removes_related_course_rows(self) -> None:
        before_counts = {
            "offers": self.service.connection.execute(
                "SELECT COUNT(*) AS row_count FROM offers WHERE course_id = 'CSE450'"
            ).fetchone()["row_count"],
            "contains": self.service.connection.execute(
                "SELECT COUNT(*) AS row_count FROM contains WHERE course_id = 'CSE450'"
            ).fetchone()["row_count"],
            "downloaded_courses": self.service.connection.execute(
                """
                SELECT COUNT(*) AS row_count
                FROM downloaded_courses
                WHERE course_id = 'CSE450'
                """
            ).fetchone()["row_count"],
        }
        self.assertEqual(before_counts, {"offers": 2, "contains": 2, "downloaded_courses": 2})

        self.service.connection.execute("DELETE FROM course WHERE course_id = 'CSE450'")
        self.service.connection.commit()

        after_counts = {
            "offers": self.service.connection.execute(
                "SELECT COUNT(*) AS row_count FROM offers WHERE course_id = 'CSE450'"
            ).fetchone()["row_count"],
            "contains": self.service.connection.execute(
                "SELECT COUNT(*) AS row_count FROM contains WHERE course_id = 'CSE450'"
            ).fetchone()["row_count"],
            "downloaded_courses": self.service.connection.execute(
                """
                SELECT COUNT(*) AS row_count
                FROM downloaded_courses
                WHERE course_id = 'CSE450'
                """
            ).fetchone()["row_count"],
        }
        self.assertEqual(after_counts, {"offers": 0, "contains": 0, "downloaded_courses": 0})

    def test_frontend_ready_payloads_include_metadata(self) -> None:
        query_catalog = self.service.list_queries()
        self.assertEqual(len(query_catalog), 5)

        filtered_query = next(
            query for query in query_catalog if query["key"] == "students_by_major"
        )
        self.assertEqual(filtered_query["parameters"][0]["name"], "major")

        table_payload = self.service.fetch_rows("student")
        self.assertEqual(table_payload["table_name"], "student")
        self.assertIn("user_name", table_payload["columns"])
        self.assertEqual(table_payload["total_count"], 8)


if __name__ == "__main__":
    unittest.main()
