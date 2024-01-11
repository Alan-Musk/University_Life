/* 1. Obtaining Major and the count of StudentIDs as NumberOfStudents from the Student table, grouped by Major, ensuring a minimum of 3 students per Major */
proc sql;
    select Major, count(StudentID) as NumberOfStudents
    from CML_6425.Student
    group by Major
    having count(StudentID) > 2;
quit;

/* 2. Extracting and merging uppercase Street and Suburb into a single field named Student_Address from Student table for records where the third letter of FirstName is 'a' */
proc sql;
    select upcase(Street) || ', ' || Suburb as Student_Address
    from CML_6425.Student
    where substr(FirstName, 3, 1) = 'a';
quit;

/* 3. Calculating and displaying CourseCode along with the average Marks as AverageMarks from the Enrolment table, grouped and sorted by CourseCode */
proc sql;
    select CourseCode, mean(Marks) as AverageMarks
    from CML_6425.Enrolment
    group by CourseCode
    order by CourseCode;
quit;

/* 4. Creating a combined uppercase LastName and FirstName as Name from the Student table, filtering for students born after 01 Jan 2000 or whose FirstName contains 'in' */
proc sql;
    select upcase(LastName) || ' ' || FirstName as Name
    from CML_6425.Student
    where DateOfBirth > '01Jan2000'
       or index(FirstName, 'in') > 0;
quit;

/* 5. Selecting StudentID and rounding off Marks to the nearest whole number as ROUNDEDMARKS from the Enrolment table */
proc sql;
    select StudentID, round(Marks) as ROUNDEDMARKS
    from CML_6425.Enrolment;
quit;
