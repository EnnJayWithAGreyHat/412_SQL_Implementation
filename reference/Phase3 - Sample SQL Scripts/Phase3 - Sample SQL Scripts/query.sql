/*
** ----------------------------------------------------------------------------
** User Uploads
** List all the students who have uploaded documents and their 
** document number
** --------------------------------------------------------------------------*/
SELECT S.userName, U.uploadDocumentID
FROM student S, uploaded U
WHERE U.uploadUserName = S.userName;

/*
** ----------------------------------------------------------------------------
** Higher than C
** List all the documents who have a grade of a C or better.
** 
** --------------------------------------------------------------------------*/
SELECT D.dID, D.dType, D.dName
FROM documents D
WHERE D.dGrade = 'A' or D.dGrade = 'B' or D.dGrade = 'C';

/*
** ----------------------------------------------------------------------------
** ASU
** List all the students who are enrolled at ASU and their major
** 
** --------------------------------------------------------------------------*/
SELECT S.userName, S.major
FROM student S, enrolled E, university U
WHERE E.enrolledUserName = S.userName and E.enrolledUnivID = U.univID;


/*
** ----------------------------------------------------------------------------
** ASU
** List all the students who are majoring in cse
** 
** --------------------------------------------------------------------------*/
SELECT S.userName, S.studentID
FROM student S 
WHERE S.major = 'cse';