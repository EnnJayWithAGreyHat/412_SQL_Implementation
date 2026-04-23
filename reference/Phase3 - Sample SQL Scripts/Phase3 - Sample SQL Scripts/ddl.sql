/*
** ----------------------------------------------------------------------------
** script to create the student table 
** --------------------------------------------------------------------------*/
 
CREATE TABLE student (
	userName	  VARCHAR2(20)	primary key,
  studentID   INTEGER       NOT NULL,
	major			  VARCHAR2(20)  NOT NULL,
	dateJoined	DATE			    NOT NULL
);

SHOW ERRORS;

/*
** ----------------------------------------------------------------------------
** script to create the document table 
** --------------------------------------------------------------------------*/

CREATE TABLE documents (
  dID			INTEGER		    PRIMARY KEY,
	dType 	VARCHAR2(20)  NOT NULL,
  dGrade	CHAR(1)       NOT NULL,
  dName		VARCHAR2(20)  NOT NULL
);

SHOW ERRORS;


/*
** ----------------------------------------------------------------------------
** script to create the course table 
** --------------------------------------------------------------------------*/
CREATE TABLE course (
	courseID  VARCHAR(10) primary key,
  teacher   VARCHAR(20),
  semester	VARCHAR2(10),
  year		  INTEGER
);

SHOW ERRORS;

/*
** ----------------------------------------------------------------------------
** script to create the university table 
** --------------------------------------------------------------------------*/

CREATE TABLE university (
  univID   INTEGER  	  PRIMARY KEY,
	uName    VARCHAR(20)	NOT NULL
);

SHOW ERRORS;

/*
** ----------------------------------------------------------------------------
** script to create the offers table 
** --------------------------------------------------------------------------*/

CREATE TABLE offers (
  offersUnivID   INTEGER ,
  offersCourseID VARCHAR(10),
	PRIMARY KEY (offersCourseID, offersUnivID),
	FOREIGN KEY(offersCourseID) REFERENCES course(courseID) ON DELETE CASCADE,
	FOREIGN KEY(offersUnivID) REFERENCES university(univID) ON DELETE CASCADE
);

SHOW ERRORS;

/*
** ----------------------------------------------------------------------------
** script to create the contains table 
** --------------------------------------------------------------------------*/

CREATE TABLE contains (
  containsDocumentID			INTEGER,
  containsCourseID   VARCHAR(10),
	PRIMARY KEY(containsDocumentID, containsCourseID),
	FOREIGN KEY(containsDocumentID) REFERENCES documents(dID) ON DELETE CASCADE,
  FOREIGN KEY(containsCourseID) REFERENCES course(courseID) ON DELETE CASCADE
);

SHOW ERRORS;

/*
** ----------------------------------------------------------------------------
** script to create the downloaded_courses table 
** --------------------------------------------------------------------------*/

CREATE TABLE downloaded_courses (
  downUserName	 VARCHAR2(20),
  downCourseID   VARCHAR(10),
  downDate       Date,
	PRIMARY KEY(downUserName, downCourseID),
	FOREIGN KEY(downUserName) REFERENCES student(userName) ON DELETE CASCADE,
  FOREIGN KEY(downCourseID) REFERENCES course(courseID) ON DELETE CASCADE
);

SHOW ERRORS;


/*
** ----------------------------------------------------------------------------
** script to create the enrolled table 
** --------------------------------------------------------------------------*/

CREATE TABLE enrolled (
  enrolledUserName VARCHAR2(20),
  enrolledUnivID   INTEGER,
  enrollDate       Date,
	PRIMARY KEY(enrolledUserName, enrolledUnivID),
	FOREIGN KEY(enrolledUserName) REFERENCES student(userName) ON DELETE CASCADE,
	FOREIGN KEY(enrolledUnivID) REFERENCES university(univID) ON DELETE CASCADE
);

SHOW ERRORS;

/*
** ----------------------------------------------------------------------------
** script to create the upload table 
** --------------------------------------------------------------------------*/

CREATE TABLE uploaded (
  uploadUserName		 VARCHAR2(20),
  uploadDocumentID   INTEGER,
  uploadDate         Date,
	PRIMARY KEY(uploadUserName, uploadDocumentID),
	FOREIGN KEY(uploadUserName) REFERENCES student(userName) ON DELETE CASCADE,
	FOREIGN KEY(uploadDocumentID) REFERENCES documents(dID) ON DELETE CASCADE
);

SHOW ERRORS;