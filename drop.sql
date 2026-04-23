/*
** ----------------------------------------------------------------------------
** drop.sql
** Drop tables in dependency order so the schema can be rebuilt cleanly.
** ----------------------------------------------------------------------------
*/

DROP TABLE IF EXISTS uploaded;

DROP TABLE IF EXISTS enrolled;

DROP TABLE IF EXISTS downloaded_courses;

DROP TABLE IF EXISTS contains;

DROP TABLE IF EXISTS offers;

DROP TABLE IF EXISTS documents;

DROP TABLE IF EXISTS course;

DROP TABLE IF EXISTS university;

DROP TABLE IF EXISTS student;
