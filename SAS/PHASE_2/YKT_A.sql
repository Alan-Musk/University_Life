/* 1. Creating a table ADMIN_ENROLMENT6570 with the same structure as the Enrolment table in YKT6570 schema */
proc sql;
    create table YKT6570.ADMIN_ENROLMENT6570 like YKT6570.Enrolment;
quit;

/* 2. Creating a table EMPLOYEE6570 by selecting all records from the Trainer table in YKT6570 schema */
proc sql;
    create table YKT6570.EMPLOYEE6570 as select * from YKT6570.Trainer;
quit;

/* 3. Retrieving all records from the EMPLOYEE6570 table in YKT6570 schema */
proc sql;
    select * from YKT6570.EMPLOYEE6570;
quit;

/* 4. Selecting first and last names, and renaming DateOfJoin to HireDate from Trainer table, filtering entries after 01Jan2009, and sorting by DateOfJoin in descending order */
proc sql;
    select FirstName, LastName, DateOfJoin as HireDate
    from YKT6570.Trainer
    where DateOfJoin > '01Jan2009'
    order by DateOfJoin desc;
quit;

/* 5. Creating a view named trainer_view with formatted trainer names, date of joining, and room numbers from the Trainer table, and displaying the view with a title */
proc sql;
    create view trainer_view as
    select upcase(LastName) || ', ' || FirstName as Trainer_Name, DateOfJoin, RoomNum
    from YKT6570.Trainer;
quit;
proc print data=trainer_view;
    title "Trainer Details";
run;

/* 6. Selecting all records from the Student table in YKT6570 schema, sorted by FirstName */
proc sql;
    select * from YKT6570.Student
    order by FirstName;
quit;

/* 7. Selecting CourseCode and TrainerID from the Course table for specific course titles */
proc sql;
    select CourseCode, TrainerID
    from YKT6570.Course
    where CourseTitle = 'Advanced Database'
       or CourseTitle = 'Introduction to IT';
quit;

/* 8. Selecting the top record from the Enrolment table in YKT6570 schema based on highest Marks */
proc sql outobs=1;
    select *
    from YKT6570.Enrolment
    order by Marks desc;
quit;

/* 9. Retrieving records from the Trainer table where TrainerID is greater than 103, sorted by FirstName in descending order */
proc sql;
    select *
    from YKT6570.Trainer
    where TrainerID > '103'
    order by FirstName desc;
quit;

/* 10. Selecting distinct Major fields from the Student table in YKT6570 schema */
proc sql;
    select distinct Major
    from YKT6570.Student;
quit;
