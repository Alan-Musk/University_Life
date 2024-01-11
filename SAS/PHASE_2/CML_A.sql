/* 1. Cloning the Enrolment table structure to create a new table named ADMIN_ENROLMENT6425 in the CML_6425 schema */
proc sql;
create table CML_6425.ADMIN_ENROLMENT6425 like CML_6425.Enrolment;
quit;

/* 2. Creating EMPLOYEE6425 table by extracting all records from the Trainer table in the CML_6425 schema */
proc sql;
create table CML_6425.EMPLOYEE6425 as select * from CML_6425.Trainer;
quit;

/* 3. Fetching and displaying every record from the EMPLOYEE6425 table within the CML_6425 schema */
proc sql;
select * from CML_6425.EMPLOYEE6425;
quit;

/* 4. Selecting FirstName, LastName, and DateOfJoin (renamed to HireDate) from the Trainer table, filtered for entries after 01 Jan 2009, and ordering by DateOfJoin in descending sequence */
proc sql;
select FirstName, LastName, DateOfJoin as HireDate
from CML_6425.Trainer
where DateOfJoin > '01Jan2009'
order by DateOfJoin desc;
quit;

/* 5. Creating a view named trainer_view comprising formatted Trainer name, DateOfJoin, and RoomNum, and subsequently displaying this view with a specific title */
proc sql;
create view trainer_view as
select upcase(LastName) || ', ' || FirstName as Trainer_Name, DateOfJoin, RoomNum
from CML_6425.Trainer;
quit;
proc print data=trainer_view;
title "Trainer Details";
run;

/* 6. Displaying all records from the Student table, sorted alphabetically by FirstName */
proc sql;
select * from CML_6425.Student
order by FirstName;
quit;

/* 7. Selecting and showing CourseCode and TrainerID from the Course table for specific courses ('Advanced Database', 'Introduction to IT') */
proc sql;
select CourseCode, TrainerID
from CML_6425.Course
where CourseTitle = 'Advanced Database'
   or CourseTitle = 'Introduction to IT';
quit;

/* 8. Retrieving and displaying the top record from the Enrolment table, sorted by Marks in a descending order */
proc sql outobs=1;
select *
from CML_6425.Enrolment
order by Marks desc;
quit;

/* 9. Extracting and displaying records from the Trainer table where TrainerID is greater than 103, ordered by FirstName in a descending manner */
proc sql;
select *
from CML_6425.Trainer
where TrainerID > '103'
order by FirstName desc;
quit;

/* 10. Displaying unique Major values from the Student table, highlighting the diversity of majors */
proc sql;
select distinct Major
from CML_6425.Student;
quit;
