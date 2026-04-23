-- Run this file from MySQL Workbench or the MySQL CLI after selecting a schema.
-- Keep ddl.sql, insert.sql, query.sql, drop.sql, and run.sql in the same directory.

-- Create the schema objects.
SOURCE ddl.sql;

-- Show the table structures.
DESCRIBE student;
DESCRIBE documents;
DESCRIBE course;
DESCRIBE university;
DESCRIBE offers;
DESCRIBE contains;
DESCRIBE downloaded_courses;
DESCRIBE enrolled;
DESCRIBE uploaded;

-- Seed the tables.
SOURCE insert.sql;

-- Show the table contents in deterministic order for verification.
SELECT * FROM student ORDER BY user_name;
SELECT * FROM documents ORDER BY document_id;
SELECT * FROM course ORDER BY course_id;
SELECT * FROM university ORDER BY university_id;
SELECT * FROM offers ORDER BY university_id, course_id;
SELECT * FROM contains ORDER BY document_id, course_id;
SELECT * FROM downloaded_courses ORDER BY user_name, course_id;
SELECT * FROM enrolled ORDER BY user_name, university_id;
SELECT * FROM uploaded ORDER BY user_name, document_id;

-- Run the five assignment queries.
SOURCE query.sql;

-- Drop the schema objects.
SOURCE drop.sql;
