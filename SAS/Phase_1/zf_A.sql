Part A
1.
libname s1546489 '/home/u63677629';

proc sql;
/* Creating the Student table */
create table s1546489.Student (
   StudentID varchar(50),
   FirstName varchar(50),
   LastName varchar(50),
   Street varchar(100),
   Suburb varchar(100),
   DateOfBirth varchar(50),
   Major varchar(50),
   constraint last_name_not_null NOT NULL (LastName),
   constraint dob_not_null NOT NULL (DateOfBirth),
   constraint major_not_null NOT NULL (Major),
   constraint student_pk primary key (StudentID),
   constraint first_name_not_null NOT NULL (FirstName)
);

/* Creating the Trainer table */
create table s1546489.Trainer (
   TrainerID varchar(50),
   FirstName varchar(50),
   LastName varchar(50),
   DateOfJoin varchar(50),
   RoomNum varchar(10),
   constraint doj_not_null NOT NULL (DateOfJoin),
   constraint room_num_unique UNIQUE (RoomNum),
   constraint trainer_pk primary key (TrainerID),
   constraint trainer_first_name_not_null NOT NULL (FirstName),
   constraint trainer_last_name_not_null NOT NULL (LastName)
);

/* Creating the Course table */
create table s1546489.Course (
   CourseCode varchar(20),
   CourseTitle varchar(100),
   TrainerID varchar(50),
   constraint course_code_pk primary key (CourseCode),
   constraint course_title_unique UNIQUE (CourseTitle)
);

/* Creating the Enrollment table */
create table s1546489.Enrolment (
   StudentID varchar(50),
   CourseCode varchar(20),
   Grade varchar(2),
   YearOfEnrolment int,
   constraint enrol_pk primary key (StudentID, CourseCode),
constraint enrol_student_fk foreign key (StudentID) references s1546489.Student(StudentID),
   constraint enrol_course_fk foreign key (CourseCode) references s1546489.Course(CourseCode)
);
quit;

2.
proc sql;
/* Start of Enrolment table deletion process */
ALTER TABLE s1546489.Enrolment DROP CONSTRAINT enrol_student_fk;
ALTER TABLE s1546489.Enrolment DROP CONSTRAINT enrol_course_fk;
DROP TABLE s1546489.Enrolment;

/* Commencing deletion of Course table */
ALTER TABLE s1546489.Course DROP CONSTRAINT course_trainer_fk;
DROP TABLE s1546489.Course;

/* Initiating drop of Student table */
DROP TABLE s1546489.Student;

/* Beginning removal of Trainer table */
DROP TABLE s1546489.Trainer;
quit;

3.
proc sql;

/* Executing removal of POSTCODE column from Student table */
ALTER TABLE s1546489.Student DROP COLUMN POSTCODE;

/* Adjusting ROOMNUM column in Trainer table to varchar(10) with NOT NULL */
ALTER TABLE s1546489.Trainer MODIFY ROOMNUM varchar(10) NOT NULL;

/* Adding new POSTCODE column to Student table, with integer data type */
ALTER TABLE s1546489.Student ADD POSTCODE int;

/* Appending MARKS column to Enrolment table, specified as float */
ALTER TABLE s1546489.Enrolment ADD MARKS float;

quit;


