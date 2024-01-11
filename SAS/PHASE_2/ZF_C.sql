1.

proc sql;
    select a.StudentID, a.FirstName, a.LastName, b.CourseCode, b.Grade
    from s1546489.Student as a
    join s1546489.Enrolment as b
    on a.StudentID = b.StudentID
    where b.Grade = 'N';
quit;

2.

proc sql;
    select *
    from s1546489.Student
    where StudentID in (select StudentID from s1546489.Enrolment where Grade = 'N');
quit;

3.

proc sql;
    select StudentID, CourseCode
    from s1546489.Enrolment
    where Marks = (select min(Marks) from s1546489.Enrolment where Marks > (select min(Marks) from s1546489.Enrolment));
quit;

4.

proc sql;
    select a.TrainerID, a.FirstName, a.LastName, a.DateOfJoin, b.CourseCode, b.CourseTitle
    from s1546489.Trainer as a
    join s1546489.Course as b
    on a.TrainerID = b.TrainerID
    where input(a.DateOfJoin, date9.) < '01Jan2014'd;
quit;


5.

proc sql;
    select StudentID, FirstName, Major
    from s1546489.Student
    order by FirstName;
quit;


6.

proc sql;
    select a.StudentID, a.FirstName, a.Major
    from s1546489.Student as a
    where a.Major = (select Major from s1546489.Student where StudentID = 'S7867');
quit;
