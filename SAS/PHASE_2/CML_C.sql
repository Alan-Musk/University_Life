/* 1. Fetching StudentID, FirstName, LastName, CourseCode, and Grade for students with Grade 'N', by joining the Student and Enrolment tables */
proc sql;
    select a.StudentID, a.FirstName, a.LastName, b.CourseCode, b.Grade
    from CML_6425.Student as a
    join CML_6425.Enrolment as b
    on a.StudentID = b.StudentID
    where b.Grade = 'N';
quit;

/* 2. Extracting all fields from the Student table for those students whose IDs are listed in the Enrolment table with a Grade of 'N' */
proc sql;
    select *
    from CML_6425.Student
    where StudentID in (select StudentID from CML_6425.Enrolment where Grade = 'N');
quit;

/* 3. Selecting StudentID and CourseCode for enrolments with the second-lowest Marks in the Enrolment table */
proc sql;
    select StudentID, CourseCode
    from CML_6425.Enrolment
    where Marks = (select min(Marks) from CML_6425.Enrolment where Marks > (select min(Marks) from CML_6425.Enrolment));
quit;

/* 4. Retrieving TrainerID, FirstName, LastName, DateOfJoin, CourseCode, and CourseTitle for trainers who started before 01 Jan 2014, by joining Trainer and Course tables */
proc sql;
    select a.TrainerID, a.FirstName, a.LastName, a.DateOfJoin, b.CourseCode, b.CourseTitle
    from CML_6425.Trainer as a
    join CML_6425.Course as b
    on a.TrainerID = b.TrainerID
    where input(a.DateOfJoin, date9.) < '01Jan2014'd;
quit;

/* 5. Extracting StudentID, FirstName, and Major from the Student table, with results ordered by FirstName */
proc sql;
    select StudentID, FirstName, Major
    from CML_6425.Student
    order by FirstName;
quit;

/* 6. Selecting StudentID, FirstName, and Major from the Student table for students sharing the same Major as StudentID 'S7867' */
proc sql;
    select a.StudentID, a.FirstName, a.Major
    from CML_6425.Student as a
    where a.Major = (select Major from CML_6425.Student where StudentID = 'S7867');
quit;
