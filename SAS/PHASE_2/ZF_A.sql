1.

proc sql;
create table s1546489.ADMIN_ENROLMENT6489 like s1546489.Enrolment;
quit;

2.

proc sql;
create table s1546489.EMPLOYEE6489 as select * from s1546489.Trainer;
quit;

3.

proc sql;
select * from s1546489.EMPLOYEE6489;
quit;

4.

proc sql;
select FirstName, LastName, DateOfJoin as HireDate
from s1546489.Trainer
where DateOfJoin > '01Jan2009'
order by DateOfJoin desc;
quit;

5.

proc sql;
    create view trainer_view as
    select upcase(LastName) || ', ' || FirstName as Trainer_Name, DateOfJoin, RoomNum
    from s1546489.Trainer;
quit;
proc print data=trainer_view;
    title "Trainer Details";
run;

6.

proc sql;
    select * from s1546489.Student
    order by FirstName;
quit;

7.

proc sql;
    select CourseCode, TrainerID
    from s1546489.Course
    where CourseTitle = 'Advanced Database'
       or CourseTitle = 'Introduction to IT';
quit;

8.

proc sql outobs=1;
    select *
    from s1546489.Enrolment
    order by Marks desc;
quit;

9.

proc sql;
    select *
    from s1546489.Trainer
    where TrainerID > '103'
    order by FirstName desc;
quit;

10.

proc sql;
    select distinct Major
    from s1546489.Student;
quit;
