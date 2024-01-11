/* 1. Select Major and count of StudentID as NumberOfStudents from Student table, grouped by Major, having more than 2 students */
proc sql;
    select Major, count(StudentID) as NumberOfStudents
    from YSH_4431.Student
    group by Major
    having count(StudentID) > 2;
quit;

/* 2. Select concatenated uppercase Street and Suburb as Student_Address from Student table where the third letter of FirstName is 'a' */
proc sql;
    select upcase(Street) || ', ' || Suburb as Student_Address
    from YSH_4431.Student
    where substr(FirstName, 3, 1) = 'a';
quit;

/* 3. Select CourseCode and the average of Marks as AverageMarks from Enrolment table, grouped by CourseCode, ordered by CourseCode */
proc sql;
    select CourseCode, mean(Marks) as AverageMarks
    from YSH_4431.Enrolment
    group by CourseCode
    order by CourseCode;
quit;

/* 4. Select concatenated uppercase LastName and FirstName as Name from Student table where DateOfBirth is after 01 Jan 2000 or FirstName contains 'in' */
proc sql;
    select upcase(LastName) || ' ' || FirstName as Name
    from YSH_4431.Student
    where DateOfBirth > '01Jan2000'
       or index(FirstName, 'in') > 0;
quit;

/* 5. Select StudentID and rounded Marks as ROUNDEDMARKS from Enrolment table */
proc sql;
    select StudentID, round(Marks) as ROUNDEDMARKS
    from YSH_4431.Enrolment;
quit;
