/* 1. Select StudentID, FirstName, LastName, CourseCode, and Grade from Student and Enrolment tables where Grade is 'N' */
proc sql;
    select a.StudentID, a.FirstName, a.LastName, b.CourseCode, b.Grade
    from YSH_4431.Student as a
    join YSH_4431.Enrolment as b
    on a.StudentID = b.StudentID
    where b.Grade = 'N';
quit;

/* 2. Select all columns from Student table where StudentID is in the list of StudentIDs from Enrolment table with Grade 'N' */
proc sql;
    select *
    from YSH_4431.Student
    where StudentID in (select StudentID from YSH_4431.Enrolment where Grade = 'N');
quit;

/* 3. Select StudentID and CourseCode from Enrolment table where Marks are equal to the second lowest marks */
proc sql;
    select StudentID, CourseCode
    from YSH_4431.Enrolment
    where Marks = (select min(Marks) from YSH_4431.Enrolment where Marks > (select min(Marks) from YSH_4431.Enrolment));
quit;

/* 4. Select TrainerID, FirstName, LastName, DateOfJoin, CourseCode, and CourseTitle from Trainer and Course tables where DateOfJoin is before 01 Jan 2014 */
proc sql;
    select a.TrainerID, a.FirstName, a.LastName, a.DateOfJoin, b.CourseCode, b.CourseTitle
    from YSH_4431.Trainer as a
    join YSH_4431.Course as b
    on a.TrainerID = b.TrainerID
    where input(a.DateOfJoin, date9.) < '01Jan2014'd;
quit;

/* 5. Select StudentID, FirstName, and Major from Student table, ordered by FirstName */
proc sql;
    select StudentID, FirstName, Major
    from YSH_4431.Student
    order by FirstName;
quit;

/* 6. Select StudentID, FirstName, and Major from Student table where Major is the same as the Major of StudentID 'S7867' */
proc sql;
    select a.StudentID, a.FirstName, a.Major
    from YSH_4431.Student as a
    where a.Major = (select Major from YSH_4431.Student where StudentID = 'S7867');
quit;
