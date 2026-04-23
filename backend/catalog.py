"""Canonical schema, seed data, and assignment queries."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATABASE_LABEL = "cse412_phase3_materials"


@dataclass(frozen=True)
class TableDefinition:
    name: str
    description: str
    columns: tuple[str, ...]
    constraints: tuple[str, ...]
    indexes: tuple[str, ...] = ()
    select_order_by: tuple[str, ...] = ()


@dataclass(frozen=True)
class SeedDefinition:
    table_name: str
    columns: tuple[str, ...]
    rows: tuple[tuple[Any, ...], ...]


@dataclass(frozen=True)
class QueryParameter:
    name: str
    description: str
    sample_value: Any


@dataclass(frozen=True)
class QueryDefinition:
    key: str
    title: str
    description: str
    sql: str
    parameters: tuple[QueryParameter, ...] = ()
    sample_params: dict[str, Any] = field(default_factory=dict)


TABLES: tuple[TableDefinition, ...] = (
    TableDefinition(
        name="student",
        description="Students who upload and download course material.",
        columns=(
            "user_name VARCHAR(50) NOT NULL",
            "student_id INTEGER NOT NULL",
            "major VARCHAR(20) NOT NULL",
            "date_joined DATE NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (user_name)",
            "UNIQUE (student_id)",
        ),
        indexes=(
            "CREATE INDEX idx_student_major ON student (major)",
        ),
        select_order_by=("user_name",),
    ),
    TableDefinition(
        name="documents",
        description="Study documents that can be uploaded and linked to courses.",
        columns=(
            "document_id INTEGER NOT NULL",
            "document_type VARCHAR(20) NOT NULL",
            "letter_grade CHAR(1) NOT NULL CHECK (letter_grade IN ('A', 'B', 'C', 'D', 'F'))",
            "document_name VARCHAR(50) NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (document_id)",
        ),
        indexes=(
            "CREATE INDEX idx_documents_grade ON documents (letter_grade)",
        ),
        select_order_by=("document_id",),
    ),
    TableDefinition(
        name="course",
        description="Courses that can be offered by universities and linked to documents.",
        columns=(
            "course_id VARCHAR(10) NOT NULL",
            "teacher_name VARCHAR(50) NOT NULL",
            "semester VARCHAR(10) NOT NULL",
            "academic_year INTEGER NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (course_id)",
        ),
        select_order_by=("course_id",),
    ),
    TableDefinition(
        name="university",
        description="Universities where students enroll and that offer courses.",
        columns=(
            "university_id INTEGER NOT NULL",
            "university_name VARCHAR(20) NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (university_id)",
            "UNIQUE (university_name)",
        ),
        select_order_by=("university_id",),
    ),
    TableDefinition(
        name="offers",
        description="Many-to-many relationship between universities and courses.",
        columns=(
            "university_id INTEGER NOT NULL",
            "course_id VARCHAR(10) NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (university_id, course_id)",
            "FOREIGN KEY (university_id) REFERENCES university(university_id) ON DELETE CASCADE",
            "FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE",
        ),
        indexes=(
            "CREATE INDEX idx_offers_course ON offers (course_id)",
        ),
        select_order_by=("university_id", "course_id"),
    ),
    TableDefinition(
        name="contains",
        description="Many-to-many relationship between documents and courses.",
        columns=(
            "document_id INTEGER NOT NULL",
            "course_id VARCHAR(10) NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (document_id, course_id)",
            "FOREIGN KEY (document_id) REFERENCES documents(document_id) ON DELETE CASCADE",
            "FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE",
        ),
        indexes=(
            "CREATE INDEX idx_contains_course ON contains (course_id)",
        ),
        select_order_by=("document_id", "course_id"),
    ),
    TableDefinition(
        name="downloaded_courses",
        description="Tracks which student downloaded material for which course.",
        columns=(
            "user_name VARCHAR(50) NOT NULL",
            "course_id VARCHAR(10) NOT NULL",
            "download_date DATE NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (user_name, course_id)",
            "FOREIGN KEY (user_name) REFERENCES student(user_name) ON DELETE CASCADE",
            "FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE",
        ),
        indexes=(
            "CREATE INDEX idx_downloaded_courses_course ON downloaded_courses (course_id)",
        ),
        select_order_by=("user_name", "course_id"),
    ),
    TableDefinition(
        name="enrolled",
        description="Tracks the university where each student is enrolled.",
        columns=(
            "user_name VARCHAR(50) NOT NULL",
            "university_id INTEGER NOT NULL",
            "enroll_date DATE NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (user_name, university_id)",
            "FOREIGN KEY (user_name) REFERENCES student(user_name) ON DELETE CASCADE",
            "FOREIGN KEY (university_id) REFERENCES university(university_id) ON DELETE CASCADE",
        ),
        indexes=(
            "CREATE INDEX idx_enrolled_university ON enrolled (university_id)",
        ),
        select_order_by=("user_name", "university_id"),
    ),
    TableDefinition(
        name="uploaded",
        description="Tracks the documents uploaded by each student.",
        columns=(
            "user_name VARCHAR(50) NOT NULL",
            "document_id INTEGER NOT NULL",
            "upload_date DATE NOT NULL",
        ),
        constraints=(
            "PRIMARY KEY (user_name, document_id)",
            "FOREIGN KEY (user_name) REFERENCES student(user_name) ON DELETE CASCADE",
            "FOREIGN KEY (document_id) REFERENCES documents(document_id) ON DELETE CASCADE",
        ),
        indexes=(
            "CREATE INDEX idx_uploaded_document ON uploaded (document_id)",
        ),
        select_order_by=("user_name", "document_id"),
    ),
)


SEEDS: tuple[SeedDefinition, ...] = (
    SeedDefinition(
        table_name="student",
        columns=("user_name", "student_id", "major", "date_joined"),
        rows=(
            ("John Smith", 123456789, "cse", "1995-02-02"),
            ("Franklin Johns", 333445555, "his", "2002-12-01"),
            ("Alicia Keys", 999887777, "cem", "1999-01-11"),
            ("Jennifer Ortiz", 987654321, "bio", "2011-11-05"),
            ("Ramesh Fahr", 666884444, "cse", "1999-07-04"),
            ("Joyce Jones", 453453453, "mat", "2005-10-04"),
            ("Ahmad Rashad", 987987987, "art", "2010-10-06"),
            ("James Kenedy", 888665555, "eee", "2001-09-12"),
        ),
    ),
    SeedDefinition(
        table_name="course",
        columns=("course_id", "teacher_name", "semester", "academic_year"),
        rows=(
            ("CSE110", "Bob Simms", "Spring", 2001),
            ("BIO213", "Roger Harris", "Fall", 2003),
            ("CEM352", "Tim Young", "Fall", 1999),
            ("MAT234", "Ross Wilkins", "Summer", 2009),
            ("CSE450", "Eddie Page", "Summer", 2008),
            ("HIS120", "Matt Rawlings", "Fall", 2008),
            ("COM101", "Josh Hill", "Fall", 2007),
            ("MAT340", "Tony Flores", "Spring", 2009),
        ),
    ),
    SeedDefinition(
        table_name="university",
        columns=("university_id", "university_name"),
        rows=(
            (1, "ASU"),
            (2, "NAU"),
            (3, "MCC"),
            (4, "SCC"),
            (5, "GCC"),
            (6, "UOA"),
            (7, "CAL"),
            (8, "BYU"),
        ),
    ),
    SeedDefinition(
        table_name="documents",
        columns=("document_id", "document_type", "letter_grade", "document_name"),
        rows=(
            (1, "Homework", "A", "hwk 1.1"),
            (2, "Test", "B", "Test 1"),
            (3, "Quiz", "C", "Quiz 3"),
            (4, "Homework", "B", "hwk 3.2"),
            (5, "Homework", "A", "hwk 3.4"),
            (6, "Test", "A", "Test1"),
            (7, "Test", "D", "Test2"),
            (8, "Test", "B", "Test2"),
            (9, "Homework", "B", "hwk 5.4"),
            (10, "Quiz", "C", "Quiz 2"),
        ),
    ),
    SeedDefinition(
        table_name="enrolled",
        columns=("user_name", "university_id", "enroll_date"),
        rows=(
            ("John Smith", 4, "1995-02-02"),
            ("Franklin Johns", 4, "2002-12-01"),
            ("Alicia Keys", 7, "1999-01-11"),
            ("Jennifer Ortiz", 1, "2011-11-05"),
            ("Ramesh Fahr", 8, "1999-07-04"),
            ("Joyce Jones", 2, "2005-10-04"),
            ("Ahmad Rashad", 2, "2010-10-06"),
            ("James Kenedy", 6, "2001-09-12"),
        ),
    ),
    SeedDefinition(
        table_name="contains",
        columns=("document_id", "course_id"),
        rows=(
            (1, "MAT234"),
            (2, "CSE110"),
            (3, "HIS120"),
            (4, "CSE450"),
            (5, "COM101"),
            (6, "CSE450"),
            (7, "HIS120"),
            (8, "MAT340"),
        ),
    ),
    SeedDefinition(
        table_name="offers",
        columns=("university_id", "course_id"),
        rows=(
            (1, "MAT234"),
            (2, "CSE110"),
            (3, "HIS120"),
            (4, "CSE450"),
            (5, "COM101"),
            (6, "CSE450"),
            (7, "HIS120"),
            (8, "MAT340"),
        ),
    ),
    SeedDefinition(
        table_name="uploaded",
        columns=("user_name", "document_id", "upload_date"),
        rows=(
            ("John Smith", 1, "1995-02-02"),
            ("Alicia Keys", 2, "1999-12-04"),
            ("Alicia Keys", 3, "1999-12-05"),
            ("James Kenedy", 4, "2001-09-15"),
            ("John Smith", 5, "2002-01-21"),
            ("John Smith", 6, "2002-01-22"),
            ("Franklin Johns", 7, "2002-12-30"),
            ("James Kenedy", 8, "2003-01-12"),
            ("Joyce Jones", 9, "2005-10-04"),
            ("Joyce Jones", 10, "2005-10-05"),
        ),
    ),
    SeedDefinition(
        table_name="downloaded_courses",
        columns=("user_name", "course_id", "download_date"),
        rows=(
            ("John Smith", "MAT234", "1995-02-02"),
            ("Franklin Johns", "CSE110", "2002-12-01"),
            ("Alicia Keys", "HIS120", "1999-01-11"),
            ("Jennifer Ortiz", "CSE450", "2011-11-05"),
            ("Ramesh Fahr", "COM101", "1999-07-04"),
            ("Joyce Jones", "CSE450", "2005-10-04"),
            ("Ahmad Rashad", "HIS120", "2010-10-06"),
            ("James Kenedy", "MAT340", "2001-09-12"),
        ),
    ),
)


QUERIES: tuple[QueryDefinition, ...] = (
    QueryDefinition(
        key="user_uploads",
        title="User Uploads",
        description="List every student who uploaded a document with the uploaded document details.",
        sql="""
SELECT
    s.user_name,
    d.document_id,
    d.document_name,
    d.document_type,
    u.upload_date
FROM uploaded AS u
JOIN student AS s
    ON s.user_name = u.user_name
JOIN documents AS d
    ON d.document_id = u.document_id
ORDER BY
    s.user_name,
    d.document_id
""".strip(),
    ),
    QueryDefinition(
        key="passing_documents",
        title="Higher Than C",
        description="List all documents that received a grade of C or better.",
        sql="""
SELECT
    document_id,
    document_type,
    document_name,
    letter_grade
FROM documents
WHERE letter_grade IN ('A', 'B', 'C')
ORDER BY
    document_id
""".strip(),
    ),
    QueryDefinition(
        key="students_by_university",
        title="ASU Enrollment",
        description="List all students enrolled at a selected university and show their major.",
        sql="""
SELECT
    s.user_name,
    s.major,
    u.university_name,
    e.enroll_date
FROM enrolled AS e
JOIN student AS s
    ON s.user_name = e.user_name
JOIN university AS u
    ON u.university_id = e.university_id
WHERE u.university_name = :university_name
ORDER BY
    s.user_name
""".strip(),
        parameters=(
            QueryParameter(
                name="university_name",
                description="University name selected from the frontend filter.",
                sample_value="ASU",
            ),
        ),
        sample_params={"university_name": "ASU"},
    ),
    QueryDefinition(
        key="students_by_major",
        title="CSE Students",
        description="List all students who belong to a selected major.",
        sql="""
SELECT
    user_name,
    student_id,
    major,
    date_joined
FROM student
WHERE major = :major
ORDER BY
    user_name
""".strip(),
        parameters=(
            QueryParameter(
                name="major",
                description="Major selected from the frontend filter.",
                sample_value="cse",
            ),
        ),
        sample_params={"major": "cse"},
    ),
    QueryDefinition(
        key="course_material_summary",
        title="Course Material Summary",
        description="Summarize course offerings by university and show how many linked documents each offering has.",
        sql="""
SELECT
    c.course_id,
    c.teacher_name,
    c.semester,
    c.academic_year,
    COALESCE(u.university_name, 'UNASSIGNED') AS university_name,
    COUNT(DISTINCT ct.document_id) AS linked_documents
FROM course AS c
LEFT JOIN offers AS o
    ON o.course_id = c.course_id
LEFT JOIN university AS u
    ON u.university_id = o.university_id
LEFT JOIN contains AS ct
    ON ct.course_id = c.course_id
GROUP BY
    c.course_id,
    c.teacher_name,
    c.semester,
    c.academic_year,
    COALESCE(u.university_name, 'UNASSIGNED')
ORDER BY
    c.course_id,
    university_name
""".strip(),
    ),
)


DROP_ORDER: tuple[str, ...] = (
    "uploaded",
    "enrolled",
    "downloaded_courses",
    "contains",
    "offers",
    "documents",
    "course",
    "university",
    "student",
)


def get_table(name: str) -> TableDefinition:
    for table in TABLES:
        if table.name == name:
            return table
    raise KeyError(name)


def get_seed(table_name: str) -> SeedDefinition:
    for seed in SEEDS:
        if seed.table_name == table_name:
            return seed
    raise KeyError(table_name)


def get_query(key: str) -> QueryDefinition:
    for query in QUERIES:
        if query.key == key:
            return query
    raise KeyError(key)
