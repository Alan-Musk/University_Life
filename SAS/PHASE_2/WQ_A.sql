/* 1. Create a new table ADMIN_ENROLMENT5836 with the same structure as the Enrolment table in the WQ_5836 schema */
proc sql;
create table WQ_5836.ADMIN_ENROLMENT5836 like WQ_5836.Enrolment;
quit;

/* 2. Create a new table EMPLOYEE5836 by selecting all records from the Trainer table in the WQ_5836 schema */
proc sql;
create table WQ_5836.EMPLOYEE5836 as select * from WQ_5836.Trainer;
quit;

/* 3. Select and display all records from the EMPLOYEE5836 table in the WQ_5836 schema */
proc sql;
select * from WQ_5836.EMPLOYEE5836;
quit;

/* 4. Select and display the FirstName, LastName, and DateOfJoin (as HireDate) from Trainer table in the WQ_5836 schema for records where DateOfJoin is after 01 Jan 2009, ordered by DateOfJoin in descending order */
proc sql;
select FirstName, LastName, DateOfJoin as HireDate
from WQ_5836.Trainer
where DateOfJoin > '01Jan2009'
order by DateOfJoin desc;
quit;

/* 5. Create a view named trainer_view with formatted Trainer name, DateOfJoin, and RoomNum from Trainer table in the WQ_5836 schema, and print the view with a title */
proc sql;
    create view trainer_view as
    select upcase(LastName) || ', ' || FirstName as Trainer_Name, DateOfJoin, RoomNum
    from WQ_5836.Trainer;
quit;
proc print data=trainer_view;
    title "Trainer Details";
run;

/* 6. Select and display all records from the Student table in the WQ_5836 schema ordered by FirstName */
proc sql;
    select * from WQ_5836.Student
    order by FirstName;
quit;

/* 7. Select and display CourseCode and TrainerID from the Course table in the WQ_5836 schema for courses with titles 'Advanced Database' or 'Introduction to IT' */
proc sql;
    select CourseCode, TrainerID
    from WQ_5836.Course
    where CourseTitle = 'Advanced Database'
       or CourseTitle = 'Introduction to IT';
quit;

/* 8. Select and display the top record from the Enrolment table in the WQ_5836 schema ordered by Marks in descending order */
proc sql outobs=1;
    select *
    from WQ_5836.Enrolment
    order by Marks desc;
quit;

/* 9. Select and display all records from the Trainer table in the WQ_5836 schema where TrainerID is greater than 103, ordered by FirstName in descending order */
proc sql;
    select *
    from WQ_5836.Trainer
    where TrainerID > '103'
    order by FirstName desc;
quit;

/* 10. Select and display distinct Major values from the Student table in the WQ_5836 schema */
proc sql;
    select distinct Major
    from WQ_5836.Student;
quit;
