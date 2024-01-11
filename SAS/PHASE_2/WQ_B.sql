/* 1. Select Major and count of StudentID as NumberOfStudents from Student table in WQ_5836 schema, grouped by Major, having more than 2 students */
proc sql;
    select Major, count(StudentID) as NumberOfStudents
    from WQ_5836.Student
    group by Major
    having count(StudentID) > 2;
quit;

/* 2. Select concatenated uppercase Street and Suburb as Student_Address from Student table in WQ_5836 schema where the third letter of FirstName is 'a' */
proc sql;
    select upcase(Street) || ', ' || Suburb as Student_Address
    from WQ_5836.Student
    where substr(FirstName, 3, 1) = 'a';
quit;

/* 3. Select CourseCode and the average of Marks as AverageMarks from Enrolment table in WQ_5836 schema, grouped by CourseCode, ordered by CourseCode */
proc sql;
    select CourseCode, mean(Marks) as AverageMarks
    from WQ_5836.Enrolment
    group by CourseCode
    order by CourseCode;
quit;

/* 4. Select concatenated uppercase LastName and FirstName as Name from Student table in WQ_5836 schema where DateOfBirth is after 01 Jan 2000 or FirstName contains 'in' */
proc sql;
    select upcase(LastName) || ' ' || FirstName as Name
    from WQ_5836.Student
    where DateOfBirth > '01Jan2000'
       or index(FirstName, 'in') > 0;
quit;

/* 5. Select StudentID and rounded Marks as ROUNDEDMARKS from Enrolment table in WQ_5836 schema */
proc sql;
    select StudentID, round(Marks) as ROUNDEDMARKS
    from WQ_5836.Enrolment;
quit;
