# Assignment Coverage

## Scope

This implementation turns the reference Phase 3 schema into a backend-first, MySQL-ready deliverable that is also structured for a later frontend. The schema, seed data, and five required queries live in one canonical catalog so the SQL files, backend service layer, tests, and transcript all stay in sync.

## Deliverable Mapping

`ddl.sql`

- Implemented at the repository root.
- Creates the full nine-table schema, which exceeds the assignment minimum of three tables.
- Uses MySQL-compatible types and syntax instead of Oracle-specific `VARCHAR2` and `@file` usage from the sample.
- Includes primary keys, foreign keys, cascade behavior, uniqueness constraints, and supporting indexes.

`insert.sql`

- Implemented at the repository root.
- Inserts explicit seed rows into every table.
- Every table has at least five rows, satisfying and exceeding the minimum requirement.
- Inserts use explicit column lists so the file remains stable if the schema evolves.

`query.sql`

- Implemented at the repository root with exactly five queries.
- The five queries cover filters, joins, parameterized frontend use cases, and aggregation:
  1. User uploads with document details.
  2. Documents graded C or better.
  3. Students enrolled at a selected university.
  4. Students in a selected major.
  5. Course offering and material summary by university.
- The committed `query.sql` contains runnable sample values for the filtered queries while the backend catalog keeps parameterized versions for frontend use.

`drop.sql`

- Implemented at the repository root.
- Drops every table in dependency-safe order with `DROP TABLE IF EXISTS`.

`run.sql`

- Implemented at the repository root.
- Uses `SOURCE filename.sql;` rather than Oracle `@file`, matching the assignment note.
- Describes tables, loads seed data, prints table contents in deterministic order, runs the five assignment queries, and finally drops the schema.

`output.txt`

- Implemented at the repository root.
- Generated from the local verification runner that executes the same canonical schema, data, and queries in the same create -> inspect -> insert -> query -> drop flow.
- Because a MySQL server is not bundled in this repository, rerun `run.sql` in MySQL Workbench or the MySQL CLI when you want a native MySQL transcript for submission.

## Backend Readiness

`backend/catalog.py`

- Single source of truth for:
  - table definitions
  - seed data
  - five required queries
  - dependency-aware drop order
- This prevents the SQL files, backend logic, and tests from drifting apart.

`backend/service.py`

- Exposes frontend-ready methods:
  - `create_schema()`
  - `seed_data()`
  - `bootstrap()`
  - `drop_schema()`
  - `list_tables()`
  - `describe_table(table_name)`
  - `fetch_rows(table_name, limit=...)`
  - `list_queries()`
  - `run_query(query_key, params)`
- All results are returned in JSON-serializable dictionary shapes that a later FastAPI or Flask HTTP layer can expose directly.

`backend/query_engine.py`

- Keeps filtered queries parameterized for real frontend execution.
- Supports SQLite-style execution today and MySQL-style placeholder compilation for later connector-based execution.

`backend/sql_assets.py`

- Generates the root SQL files from the canonical catalog.
- This makes the assignment deliverables reproducible and keeps future edits consistent.

## Reference Conversion Notes

The reference materials were Oracle-oriented. This implementation explicitly converts those expectations to MySQL-style deliverables:

- `VARCHAR2` became `VARCHAR`.
- `@ddl`, `@insert`, and `@query` became `SOURCE ddl.sql;`, `SOURCE insert.sql;`, and `SOURCE query.sql;`.
- The sample query labeled as an ASU filter was corrected so it actually filters to `ASU`.
- ANSI joins were used instead of legacy comma joins for clarity and maintainability.
- Column names were normalized for readability and frontend/API friendliness.

## Data Integrity and Production Readiness

The backend is more than a bare class assignment scaffold. It includes the integrity rules you would want before wiring it to a frontend:

- Primary keys on every base and relationship table.
- Foreign keys on every relationship table.
- `ON DELETE CASCADE` so dependent rows do not become orphaned.
- Unique constraints on `student.student_id` and `university.university_name`.
- A grade check constraint on `documents.letter_grade`.
- Supporting indexes on frequently joined and filtered columns.
- Deterministic ordering in `run.sql` and the transcript so output is stable and reviewable.
- Explicit insert column lists to protect against column-order breakage.
- Parameterized query handling for filtered frontend requests.

## Test Coverage

`tests/test_backend_service.py`

- Verifies that all nine tables are created and populated.
- Verifies expected row counts.
- Executes all five assignment queries and checks their results.
- Verifies foreign-key enforcement by attempting an invalid insert.
- Verifies cascade deletion by deleting a course and checking dependent tables.
- Verifies that the service methods return frontend-ready metadata and row payloads.

`tests/test_sql_assets.py`

- Verifies the SQL asset files can be generated.
- Verifies `run.sql` uses `SOURCE`.
- Verifies `query.sql` contains exactly five queries.
- Verifies `insert.sql` contains at least five rows per table.
- Verifies MySQL parameter compilation for future connector use.
- Verifies the output transcript includes the query-results section.

## Requirement-by-Requirement Conclusion

From the pasted assignment text:

- `ddl.sql`: fully implemented and exceeds minimum scope.
- `insert.sql`: fully implemented and exceeds row minimums.
- `query.sql`: fully implemented with five meaningful queries.
- `drop.sql`: fully implemented.
- `run.sql`: fully implemented with MySQL `SOURCE` syntax.
- `output.txt`: implemented as a reproducible transcript from the committed backend flow, with a clear path to regenerate native MySQL output.

From the checklist/sample documents:

- The required files exist at the repo root in the expected format.
- The file structure is MySQL-oriented rather than Oracle-oriented.
- The backend workflow matches the expected create -> show tables -> insert -> show contents -> run queries -> drop pattern.
- The implementation is test-backed and frontend-ready rather than being only a loose collection of SQL scripts.
