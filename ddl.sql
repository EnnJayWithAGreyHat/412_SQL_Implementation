/*
** ----------------------------------------------------------------------------
** ddl.sql
** Create every table from the study-material relational schema in MySQL.
** ----------------------------------------------------------------------------
*/

/*
** ----------------------------------------------------------------------------
** Create student
** Students who upload and download course material.
** ----------------------------------------------------------------------------
*/

CREATE TABLE student (
    user_name VARCHAR(50) NOT NULL,
    student_id INTEGER NOT NULL,
    major VARCHAR(20) NOT NULL,
    date_joined DATE NOT NULL,
    PRIMARY KEY (user_name),
    UNIQUE (student_id)
);

CREATE INDEX idx_student_major ON student (major);

/*
** ----------------------------------------------------------------------------
** Create documents
** Study documents that can be uploaded and linked to courses.
** ----------------------------------------------------------------------------
*/

CREATE TABLE documents (
    document_id INTEGER NOT NULL,
    document_type VARCHAR(20) NOT NULL,
    letter_grade CHAR(1) NOT NULL CHECK (letter_grade IN ('A', 'B', 'C', 'D', 'F')),
    document_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (document_id)
);

CREATE INDEX idx_documents_grade ON documents (letter_grade);

/*
** ----------------------------------------------------------------------------
** Create course
** Courses that can be offered by universities and linked to documents.
** ----------------------------------------------------------------------------
*/

CREATE TABLE course (
    course_id VARCHAR(10) NOT NULL,
    teacher_name VARCHAR(50) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    academic_year INTEGER NOT NULL,
    PRIMARY KEY (course_id)
);

/*
** ----------------------------------------------------------------------------
** Create university
** Universities where students enroll and that offer courses.
** ----------------------------------------------------------------------------
*/

CREATE TABLE university (
    university_id INTEGER NOT NULL,
    university_name VARCHAR(20) NOT NULL,
    PRIMARY KEY (university_id),
    UNIQUE (university_name)
);

/*
** ----------------------------------------------------------------------------
** Create offers
** Many-to-many relationship between universities and courses.
** ----------------------------------------------------------------------------
*/

CREATE TABLE offers (
    university_id INTEGER NOT NULL,
    course_id VARCHAR(10) NOT NULL,
    PRIMARY KEY (university_id, course_id),
    FOREIGN KEY (university_id) REFERENCES university(university_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);

CREATE INDEX idx_offers_course ON offers (course_id);

/*
** ----------------------------------------------------------------------------
** Create contains
** Many-to-many relationship between documents and courses.
** ----------------------------------------------------------------------------
*/

CREATE TABLE contains (
    document_id INTEGER NOT NULL,
    course_id VARCHAR(10) NOT NULL,
    PRIMARY KEY (document_id, course_id),
    FOREIGN KEY (document_id) REFERENCES documents(document_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);

CREATE INDEX idx_contains_course ON contains (course_id);

/*
** ----------------------------------------------------------------------------
** Create downloaded_courses
** Tracks which student downloaded material for which course.
** ----------------------------------------------------------------------------
*/

CREATE TABLE downloaded_courses (
    user_name VARCHAR(50) NOT NULL,
    course_id VARCHAR(10) NOT NULL,
    download_date DATE NOT NULL,
    PRIMARY KEY (user_name, course_id),
    FOREIGN KEY (user_name) REFERENCES student(user_name) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);

CREATE INDEX idx_downloaded_courses_course ON downloaded_courses (course_id);

/*
** ----------------------------------------------------------------------------
** Create enrolled
** Tracks the university where each student is enrolled.
** ----------------------------------------------------------------------------
*/

CREATE TABLE enrolled (
    user_name VARCHAR(50) NOT NULL,
    university_id INTEGER NOT NULL,
    enroll_date DATE NOT NULL,
    PRIMARY KEY (user_name, university_id),
    FOREIGN KEY (user_name) REFERENCES student(user_name) ON DELETE CASCADE,
    FOREIGN KEY (university_id) REFERENCES university(university_id) ON DELETE CASCADE
);

CREATE INDEX idx_enrolled_university ON enrolled (university_id);

/*
** ----------------------------------------------------------------------------
** Create uploaded
** Tracks the documents uploaded by each student.
** ----------------------------------------------------------------------------
*/

CREATE TABLE uploaded (
    user_name VARCHAR(50) NOT NULL,
    document_id INTEGER NOT NULL,
    upload_date DATE NOT NULL,
    PRIMARY KEY (user_name, document_id),
    FOREIGN KEY (user_name) REFERENCES student(user_name) ON DELETE CASCADE,
    FOREIGN KEY (document_id) REFERENCES documents(document_id) ON DELETE CASCADE
);

CREATE INDEX idx_uploaded_document ON uploaded (document_id);
