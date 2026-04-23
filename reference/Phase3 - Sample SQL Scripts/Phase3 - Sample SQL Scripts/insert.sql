/*
** ----------------------------------------------------------------------------
** script to insert data into the student table 
** --------------------------------------------------------------------------*/
INSERT INTO student VALUES('John Smith',123456789,'cse','02-FEB-95');
INSERT INTO student VALUES('Franklin Johns',333445555,'his','01-DEC-02');
INSERT INTO student VALUES('Alicia Keys',999887777,'cem','11-JAN-99');
INSERT INTO student VALUES('Jennifer Ortiz',987654321,'bio','05-NOV-11');
INSERT INTO student VALUES('Ramesh Fahr',666884444,'cse','04-JUL-99');
INSERT INTO student VALUES('Joyce Jones',453453453,'mat','04-OCT-05');
INSERT INTO student VALUES('Ahmad Rashad',987987987,'art','06-OCT-10');
INSERT INTO student VALUES('James Kenedy',888665555,'eee','12-SEP-01');

/*
** ----------------------------------------------------------------------------
** script to insert data in the course table 
** --------------------------------------------------------------------------*/
INSERT INTO course VALUES('CSE110','Bob Simms','Spring',2001);
INSERT INTO course VALUES('BIO213','Roger Harris','Fall',2003);
INSERT INTO course VALUES('CEM352','Tim Young','Fall',1999);
INSERT INTO course VALUES('MAT234','Ross Wilkins','Summer',2009);
INSERT INTO course VALUES('CSE450','Eddie Page','Summer',2008);
INSERT INTO course VALUES('HIS120','Matt Rawlings','Fall',2008);
INSERT INTO course VALUES('COM101','Josh Hill','Fall',2007);
INSERT INTO course VALUES('MAT340','Tony Flores','Spring',2009);

/*
** ----------------------------------------------------------------------------
** script to insert data in the university table 
** --------------------------------------------------------------------------*/
INSERT INTO university VALUES(1,'ASU');
INSERT INTO university VALUES(2,'NAU');
INSERT INTO university VALUES(3,'MCC');
INSERT INTO university VALUES(4,'SCC');
INSERT INTO university VALUES(5,'GCC');
INSERT INTO university VALUES(6,'UOA');
INSERT INTO university VALUES(7,'CAL');
INSERT INTO university VALUES(8,'BYU');


/*
** ----------------------------------------------------------------------------
** script to insert data into the documents table 
** --------------------------------------------------------------------------*/
INSERT INTO documents VALUES(1,'Homework','A','hwk 1.1');
INSERT INTO documents VALUES(2,'Test','B','Test 1');
INSERT INTO documents VALUES(3,'Quiz','C','Quiz 3');
INSERT INTO documents VALUES(4,'Homework','B','hwk 3.2');
INSERT INTO documents VALUES(5,'Homework','A','hwk 3.4');
INSERT INTO documents VALUES(6,'Test','A','Test1');
INSERT INTO documents VALUES(7,'Test','D','Test2');
INSERT INTO documents VALUES(8,'Test','B','Test2');
INSERT INTO documents VALUES(9,'Homework','B','hwk 5.4');
INSERT INTO documents VALUES(10,'Quiz','C','Quiz 2');

/*
** ----------------------------------------------------------------------------
** script to insert data in the enrolled table 
** --------------------------------------------------------------------------*/
INSERT INTO enrolled VALUES('John Smith',4,'02-FEB-95');
INSERT INTO enrolled VALUES('Franklin Johns',4,'01-DEC-02');
INSERT INTO enrolled VALUES('Alicia Keys',7,'11-JAN-99');
INSERT INTO enrolled VALUES('Jennifer Ortiz',1,'05-NOV-11');
INSERT INTO enrolled VALUES('Ramesh Fahr',8,'04-JUL-99');
INSERT INTO enrolled VALUES('Joyce Jones',2,'04-OCT-05');
INSERT INTO enrolled VALUES('Ahmad Rashad',2,'06-OCT-10');
INSERT INTO enrolled VALUES('James Kenedy',6,'12-SEP-01');

/*
** ----------------------------------------------------------------------------
** script to insert data into the contains table 
** --------------------------------------------------------------------------*/
INSERT INTO contains VALUES(1,'MAT234');
INSERT INTO contains VALUES(2,'CSE110');
INSERT INTO contains VALUES(3,'HIS120');
INSERT INTO contains VALUES(4,'CSE450');
INSERT INTO contains VALUES(5,'COM101');
INSERT INTO contains VALUES(6,'CSE450');
INSERT INTO contains VALUES(7,'HIS120');
INSERT INTO contains VALUES(8,'MAT340');



/*
** ----------------------------------------------------------------------------
** script to insert data into the offers table 
** --------------------------------------------------------------------------*/
INSERT INTO offers VALUES(1,'MAT234');
INSERT INTO offers VALUES(2,'CSE110');
INSERT INTO offers VALUES(3,'HIS120');
INSERT INTO offers VALUES(4,'CSE450');
INSERT INTO offers VALUES(5,'COM101');
INSERT INTO offers VALUES(6,'CSE450');
INSERT INTO offers VALUES(7,'HIS120');
INSERT INTO offers VALUES(8,'MAT340');


/*
** ----------------------------------------------------------------------------
** script to insert data into the uploaded table 
** --------------------------------------------------------------------------*/
INSERT INTO uploaded VALUES('John Smith',1,'02-FEB-95');
INSERT INTO uploaded VALUES('Alicia Keys',2,'04-DEC-99');
INSERT INTO uploaded VALUES('Alicia Keys',3,'05-DEC-99');
INSERT INTO uploaded VALUES('James Kenedy',4,'15-SEP-01');
INSERT INTO uploaded VALUES('John Smith',5,'21-JAN-02');
INSERT INTO uploaded VALUES('John Smith',6,'22-JAN-02');
INSERT INTO uploaded VALUES('Franklin Johns',7,'30-DEC-02');
INSERT INTO uploaded VALUES('James Kenedy',8,'12-JAN-03');
INSERT INTO uploaded VALUES('Joyce Jones',9,'04-OCT-05');
INSERT INTO uploaded VALUES('Joyce Jones',10,'05-OCT-05');


/*
** ----------------------------------------------------------------------------
** script to insert data into the downloaded_courses table 
** --------------------------------------------------------------------------*/
INSERT INTO downloaded_courses VALUES('John Smith','MAT234','02-FEB-95');
INSERT INTO downloaded_courses VALUES('Franklin Johns','CSE110','01-DEC-02');
INSERT INTO downloaded_courses VALUES('Alicia Keys','HIS120','11-JAN-99');
INSERT INTO downloaded_courses VALUES('Jennifer Ortiz','CSE450','05-NOV-11');
INSERT INTO downloaded_courses VALUES('Ramesh Fahr','COM101','04-JUL-99');
INSERT INTO downloaded_courses VALUES('Joyce Jones','CSE450','04-OCT-05');
INSERT INTO downloaded_courses VALUES('Ahmad Rashad','HIS120','06-OCT-10');
INSERT INTO downloaded_courses VALUES('James Kenedy','MAT340','12-SEP-01');
