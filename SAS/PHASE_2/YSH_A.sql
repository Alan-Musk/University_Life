/* 1. Create a new table ADMIN_ENROLMENT4431 with the same structure as the Enrolment table */
proc sql;
create table YSH_4431.ADMIN_ENROLMENT4431 like YSH_4431.Enrolment;
quit;

/* 2. Create a new table EMPLOYEE4431 by selecting all records from the Trainer table */
proc sql;
create table YSH_4431.EMPLOYEE4431 as select * from YSH_4431.Trainer;
quit;

/* 3. Select and display all records from the EMPLOYEE4431 table */
proc sql;
select * from YSH_4431.EMPLOYEE4431;
quit;

/* 4. Select and display the FirstName, LastName, and DateOfJoin (as HireDate) from Trainer table for records where DateOfJoin is after 01 Jan 2009, ordered by DateOfJoin in descending order */
proc sql;
select FirstName, LastName, DateOfJoin as HireDate
from YSH_4431.Trainer
where DateOfJoin > '01Jan2009'
order by DateOfJoin desc;
quit;

/* 5. Create a view named trainer_view with formatted Trainer name, DateOfJoin, and RoomNum, and print the view with a title */
proc sql;
    create view trainer_view as
    select upcase(LastName) || ', ' || FirstName as Trainer_Name, DateOfJoin, RoomNum
    from YSH_4431.Trainer;
quit;
proc print data=trainer_view;
    title "Trainer Details";
run;

/* 6. Select and display all records from the Student table ordered by FirstName */
proc sql;
    select * from YSH_4431.Student
    order by FirstName;
quit;

/* 7. Select and display CourseCode and TrainerID from the Course table for courses with titles 'Advanced Database' or 'Introduction to IT' */
proc sql;
    select CourseCode, TrainerID
    from YSH_4431.Course
    where CourseTitle = 'Advanced Database'
       or CourseTitle = 'Introduction to IT';
quit;

/* 8. Select and display the top record from the Enrolment table ordered by Marks in descending order */
proc sql outobs=1;
    select *
    from YSH_4431.Enrolment
    order by Marks desc;
quit;

/* 9. Select and display all records from the Trainer table where TrainerID is greater than 103, ordered by FirstName in descending order */
proc sql;
    select *
    from YSH_4431.Trainer
    where TrainerID > '103'
    order by FirstName desc;
quit;

/* 10. Select and display distinct Major values from the Student table */
proc sql;
    select distinct Major
    from YSH_4431.Student;
quit;
