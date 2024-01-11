/* 1. Select StudentID, FirstName, LastName, CourseCode, and Grade from Student and Enrolment tables in TH_6437 schema where Grade is 'N' */
proc sql;
    select a.StudentID, a.FirstName, a.LastName, b.CourseCode, b.Grade
    from TH_6437.Student as a
    join TH_6437.Enrolment as b
    on a.StudentID = b.StudentID
    where b.Grade = 'N';
quit;

/* 2. Select all columns from Student table in TH_6437 schema where StudentID is in the list of StudentIDs from Enrolment table with Grade 'N' */
proc sql;
    select *
    from TH_6437.Student
    where StudentID in (select StudentID from TH_6437.Enrolment where Grade = 'N');
quit;

/* 3. Select StudentID and CourseCode from Enrolment table in TH_6437 schema where Marks are equal to the second lowest marks */
proc sql;
    select StudentID, CourseCode
    from TH_6437.Enrolment
    where Marks = (select min(Marks) from TH_6437.Enrolment where Marks > (select min(Marks) from TH_6437.Enrolment));
quit;

/* 4. Select TrainerID, FirstName, LastName, DateOfJoin, CourseCode, and CourseTitle from Trainer and Course tables in TH_6437 schema where DateOfJoin is before 01 Jan 2014 */
proc sql;
    select a.TrainerID, a.FirstName, a.LastName, a.DateOfJoin, b.CourseCode, b.CourseTitle
    from TH_6437.Trainer as a
    join TH_6437.Course as b
    on a.TrainerID = b.TrainerID
    where input(a.DateOfJoin, date9.) < '01Jan2014'd;
quit;

/* 5. Select StudentID, FirstName, and Major from Student table in TH_6437 schema, ordered by FirstName */
proc sql;
    select StudentID, FirstName, Major
    from TH_6437.Student
    order by FirstName;
quit;

/* 6. Select StudentID, FirstName, and Major from Student table in TH_6437 schema where Major is the same as the Major of StudentID 'S7867' */
proc sql;
    select a.StudentID, a.FirstName, a.Major
    from TH_6437.Student as a
    where a.Major = (select Major from TH_6437.Student where StudentID = 'S7867');
quit;
