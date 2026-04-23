/*
** ----------------------------------------------------------------------------
** insert.sql
** Insert seed data into every table with explicit column lists.
** ----------------------------------------------------------------------------
*/

/*
** ----------------------------------------------------------------------------
** Insert rows into student
** Populate student with 8 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO student (user_name, student_id, major, date_joined) VALUES ('John Smith', 123456789, 'cse', '1995-02-02');

INSERT INTO student (user_name, student_id, major, date_joined) VALUES ('Franklin Johns', 333445555, 'his', '2002-12-01');

INSERT INTO student (user_name, student_id, major, date_joined) VALUES ('Alicia Keys', 999887777, 'cem', '1999-01-11');

INSERT INTO student (user_name, student_id, major, date_joined) VALUES ('Jennifer Ortiz', 987654321, 'bio', '2011-11-05');

INSERT INTO student (user_name, student_id, major, date_joined) VALUES ('Ramesh Fahr', 666884444, 'cse', '1999-07-04');

INSERT INTO student (user_name, student_id, major, date_joined) VALUES ('Joyce Jones', 453453453, 'mat', '2005-10-04');

INSERT INTO student (user_name, student_id, major, date_joined) VALUES ('Ahmad Rashad', 987987987, 'art', '2010-10-06');

INSERT INTO student (user_name, student_id, major, date_joined) VALUES ('James Kenedy', 888665555, 'eee', '2001-09-12');

/*
** ----------------------------------------------------------------------------
** Insert rows into course
** Populate course with 8 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO course (course_id, teacher_name, semester, academic_year) VALUES ('CSE110', 'Bob Simms', 'Spring', 2001);

INSERT INTO course (course_id, teacher_name, semester, academic_year) VALUES ('BIO213', 'Roger Harris', 'Fall', 2003);

INSERT INTO course (course_id, teacher_name, semester, academic_year) VALUES ('CEM352', 'Tim Young', 'Fall', 1999);

INSERT INTO course (course_id, teacher_name, semester, academic_year) VALUES ('MAT234', 'Ross Wilkins', 'Summer', 2009);

INSERT INTO course (course_id, teacher_name, semester, academic_year) VALUES ('CSE450', 'Eddie Page', 'Summer', 2008);

INSERT INTO course (course_id, teacher_name, semester, academic_year) VALUES ('HIS120', 'Matt Rawlings', 'Fall', 2008);

INSERT INTO course (course_id, teacher_name, semester, academic_year) VALUES ('COM101', 'Josh Hill', 'Fall', 2007);

INSERT INTO course (course_id, teacher_name, semester, academic_year) VALUES ('MAT340', 'Tony Flores', 'Spring', 2009);

/*
** ----------------------------------------------------------------------------
** Insert rows into university
** Populate university with 8 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO university (university_id, university_name) VALUES (1, 'ASU');

INSERT INTO university (university_id, university_name) VALUES (2, 'NAU');

INSERT INTO university (university_id, university_name) VALUES (3, 'MCC');

INSERT INTO university (university_id, university_name) VALUES (4, 'SCC');

INSERT INTO university (university_id, university_name) VALUES (5, 'GCC');

INSERT INTO university (university_id, university_name) VALUES (6, 'UOA');

INSERT INTO university (university_id, university_name) VALUES (7, 'CAL');

INSERT INTO university (university_id, university_name) VALUES (8, 'BYU');

/*
** ----------------------------------------------------------------------------
** Insert rows into documents
** Populate documents with 10 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (1, 'Homework', 'A', 'hwk 1.1');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (2, 'Test', 'B', 'Test 1');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (3, 'Quiz', 'C', 'Quiz 3');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (4, 'Homework', 'B', 'hwk 3.2');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (5, 'Homework', 'A', 'hwk 3.4');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (6, 'Test', 'A', 'Test1');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (7, 'Test', 'D', 'Test2');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (8, 'Test', 'B', 'Test2');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (9, 'Homework', 'B', 'hwk 5.4');

INSERT INTO documents (document_id, document_type, letter_grade, document_name) VALUES (10, 'Quiz', 'C', 'Quiz 2');

/*
** ----------------------------------------------------------------------------
** Insert rows into enrolled
** Populate enrolled with 8 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO enrolled (user_name, university_id, enroll_date) VALUES ('John Smith', 4, '1995-02-02');

INSERT INTO enrolled (user_name, university_id, enroll_date) VALUES ('Franklin Johns', 4, '2002-12-01');

INSERT INTO enrolled (user_name, university_id, enroll_date) VALUES ('Alicia Keys', 7, '1999-01-11');

INSERT INTO enrolled (user_name, university_id, enroll_date) VALUES ('Jennifer Ortiz', 1, '2011-11-05');

INSERT INTO enrolled (user_name, university_id, enroll_date) VALUES ('Ramesh Fahr', 8, '1999-07-04');

INSERT INTO enrolled (user_name, university_id, enroll_date) VALUES ('Joyce Jones', 2, '2005-10-04');

INSERT INTO enrolled (user_name, university_id, enroll_date) VALUES ('Ahmad Rashad', 2, '2010-10-06');

INSERT INTO enrolled (user_name, university_id, enroll_date) VALUES ('James Kenedy', 6, '2001-09-12');

/*
** ----------------------------------------------------------------------------
** Insert rows into contains
** Populate contains with 8 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO contains (document_id, course_id) VALUES (1, 'MAT234');

INSERT INTO contains (document_id, course_id) VALUES (2, 'CSE110');

INSERT INTO contains (document_id, course_id) VALUES (3, 'HIS120');

INSERT INTO contains (document_id, course_id) VALUES (4, 'CSE450');

INSERT INTO contains (document_id, course_id) VALUES (5, 'COM101');

INSERT INTO contains (document_id, course_id) VALUES (6, 'CSE450');

INSERT INTO contains (document_id, course_id) VALUES (7, 'HIS120');

INSERT INTO contains (document_id, course_id) VALUES (8, 'MAT340');

/*
** ----------------------------------------------------------------------------
** Insert rows into offers
** Populate offers with 8 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO offers (university_id, course_id) VALUES (1, 'MAT234');

INSERT INTO offers (university_id, course_id) VALUES (2, 'CSE110');

INSERT INTO offers (university_id, course_id) VALUES (3, 'HIS120');

INSERT INTO offers (university_id, course_id) VALUES (4, 'CSE450');

INSERT INTO offers (university_id, course_id) VALUES (5, 'COM101');

INSERT INTO offers (university_id, course_id) VALUES (6, 'CSE450');

INSERT INTO offers (university_id, course_id) VALUES (7, 'HIS120');

INSERT INTO offers (university_id, course_id) VALUES (8, 'MAT340');

/*
** ----------------------------------------------------------------------------
** Insert rows into uploaded
** Populate uploaded with 10 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('John Smith', 1, '1995-02-02');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('Alicia Keys', 2, '1999-12-04');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('Alicia Keys', 3, '1999-12-05');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('James Kenedy', 4, '2001-09-15');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('John Smith', 5, '2002-01-21');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('John Smith', 6, '2002-01-22');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('Franklin Johns', 7, '2002-12-30');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('James Kenedy', 8, '2003-01-12');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('Joyce Jones', 9, '2005-10-04');

INSERT INTO uploaded (user_name, document_id, upload_date) VALUES ('Joyce Jones', 10, '2005-10-05');

/*
** ----------------------------------------------------------------------------
** Insert rows into downloaded_courses
** Populate downloaded_courses with 8 seed rows.
** ----------------------------------------------------------------------------
*/

INSERT INTO downloaded_courses (user_name, course_id, download_date) VALUES ('John Smith', 'MAT234', '1995-02-02');

INSERT INTO downloaded_courses (user_name, course_id, download_date) VALUES ('Franklin Johns', 'CSE110', '2002-12-01');

INSERT INTO downloaded_courses (user_name, course_id, download_date) VALUES ('Alicia Keys', 'HIS120', '1999-01-11');

INSERT INTO downloaded_courses (user_name, course_id, download_date) VALUES ('Jennifer Ortiz', 'CSE450', '2011-11-05');

INSERT INTO downloaded_courses (user_name, course_id, download_date) VALUES ('Ramesh Fahr', 'COM101', '1999-07-04');

INSERT INTO downloaded_courses (user_name, course_id, download_date) VALUES ('Joyce Jones', 'CSE450', '2005-10-04');

INSERT INTO downloaded_courses (user_name, course_id, download_date) VALUES ('Ahmad Rashad', 'HIS120', '2010-10-06');

INSERT INTO downloaded_courses (user_name, course_id, download_date) VALUES ('James Kenedy', 'MAT340', '2001-09-12');
