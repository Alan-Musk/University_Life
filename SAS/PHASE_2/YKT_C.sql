1.

proc sql;
    select a.StudentID, a.FirstName, a.LastName, b.CourseCode, b.Grade
    from YKT6570.Student as a
    join YKT6570.Enrolment as b
    on a.StudentID = b.StudentID
    where b.Grade = 'N';
quit;

2.

proc sql;
    select *
    from YKT6570.Student
    where StudentID in (select StudentID from YKT6570.Enrolment where Grade = 'N');
quit;

3.

proc sql;
    select StudentID, CourseCode
    from YKT6570.Enrolment
    where Marks = (select min(Marks) from YKT6570.Enrolment where Marks > (select min(Marks) from YKT6570.Enrolment));
quit;

4.

proc sql;
    select a.TrainerID, a.FirstName, a.LastName, a.DateOfJoin, b.CourseCode, b.CourseTitle
    from YKT6570.Trainer as a
    join YKT6570.Course as b
    on a.TrainerID = b.TrainerID
    where input(a.DateOfJoin, date9.) < '01Jan2014'd;
quit;


5.

proc sql;
    select StudentID, FirstName, Major
    from YKT6570.Student
    order by FirstName;
quit;


6.

proc sql;
    select a.StudentID, a.FirstName, a.Major
    from YKT6570.Student as a
    where a.Major = (select Major from YKT6570.Student where StudentID = 'S7867');
quit;
