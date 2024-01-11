/* 1. Duplicate the structure of the Enrolment table from TH_6437 schema to create ADMIN_ENROLMENT6437 table */
proc sql;
create table TH_6437.ADMIN_ENROLMENT6437 like TH_6437.Enrolment;
quit;

/* 2. Generate EMPLOYEE6437 table by selecting all entries from the Trainer table in the TH_6437 schema */
proc sql;
create table TH_6437.EMPLOYEE6437 as select * from TH_6437.Trainer;
quit;

/* 3. Retrieve and display all records from the EMPLOYEE6437 table within the TH_6437 schema */
proc sql;
select * from TH_6437.EMPLOYEE6437;
quit;

/* 4. Extract and display FirstName, LastName, and DateOfJoin (renamed as HireDate) from Trainer table, filtering records post 01 Jan 2009, sorted by DateOfJoin in descending order */
proc sql;
select FirstName, LastName, DateOfJoin as HireDate
from TH_6437.Trainer
where DateOfJoin > '01Jan2009'
order by DateOfJoin desc;
quit;

/* 5. Establish a view named trainer_view with formatted Trainer name, DateOfJoin, and RoomNum, and print the view with a title */
proc sql;
    create view trainer_view as
    select upcase(LastName) || ', ' || FirstName as Trainer_Name, DateOfJoin, RoomNum
    from TH_6437.Trainer;
quit;
proc print data=trainer_view;
    title "Trainer Details";
run;

/* 6. Display all entries from the Student table, ordered by FirstName */
proc sql;
    select * from TH_6437.Student
    order by FirstName;
quit;

/* 7. Retrieve and display CourseCode and TrainerID from Course table for specified courses ('Advanced Database', 'Introduction to IT') */
proc sql;
    select CourseCode, TrainerID
    from TH_6437.Course
    where CourseTitle = 'Advanced Database'
       or CourseTitle = 'Introduction to IT';
quit;

/* 8. Fetch and display the top entry from the Enrolment table, ordered by Marks in descending order */
proc sql outobs=1;
    select *
    from TH_6437.Enrolment
    order by Marks desc;
quit;

/* 9. Extract and show all records from Trainer table where TrainerID exceeds 103, sorted by FirstName in descending order */
proc sql;
    select *
    from TH_6437.Trainer
    where TrainerID > '103'
    order by FirstName desc;
quit;

/* 10. Display unique Major values from the Student table */
proc sql;
    select distinct Major
    from TH_6437.Student;
quit;
