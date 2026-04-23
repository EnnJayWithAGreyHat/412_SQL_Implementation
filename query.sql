/*
** ----------------------------------------------------------------------------
** query.sql
** Five assignment queries that demonstrate joins, filters, and aggregation.
** ----------------------------------------------------------------------------
*/

/*
** ----------------------------------------------------------------------------
** Query 1: User Uploads
** List every student who uploaded a document with the uploaded document details.
** ----------------------------------------------------------------------------
*/

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
    d.document_id;

/*
** ----------------------------------------------------------------------------
** Query 2: Higher Than C
** List all documents that received a grade of C or better.
** ----------------------------------------------------------------------------
*/

SELECT
    document_id,
    document_type,
    document_name,
    letter_grade
FROM documents
WHERE letter_grade IN ('A', 'B', 'C')
ORDER BY
    document_id;

/*
** ----------------------------------------------------------------------------
** Query 3: ASU Enrollment
** List all students enrolled at a selected university and show their major. Sample parameters: university_name=ASU.
** ----------------------------------------------------------------------------
*/

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
WHERE u.university_name = 'ASU'
ORDER BY
    s.user_name;

/*
** ----------------------------------------------------------------------------
** Query 4: CSE Students
** List all students who belong to a selected major. Sample parameters: major=cse.
** ----------------------------------------------------------------------------
*/

SELECT
    user_name,
    student_id,
    major,
    date_joined
FROM student
WHERE major = 'cse'
ORDER BY
    user_name;

/*
** ----------------------------------------------------------------------------
** Query 5: Course Material Summary
** Summarize course offerings by university and show how many linked documents each offering has.
** ----------------------------------------------------------------------------
*/

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
    university_name;
