/* 1. Retrieve the count of students in each major with more than 2 students */
proc sql;
    select Major, count(StudentID) as NumberOfStudents
    from YKT6570.Student
    group by Major
    having count(StudentID) > 2;
quit;

/* 2. Generate a list of student addresses in uppercase with the condition that the third letter of the first name is 'a' */
proc sql;
    select upcase(Street) || ', ' || Suburb as Student_Address
    from YKT6570.Student
    where substr(FirstName, 3, 1) = 'a';
quit;

/* 3. Calculate the average marks for each course and order by course code */
proc sql;
    select CourseCode, mean(Marks) as AverageMarks
    from YKT6570.Enrolment
    group by CourseCode
    order by CourseCode;
quit;

/* 4. Select students' names in a specific format if their date of birth is after 01 Jan 2000 or their first name contains 'in' */
proc sql;
    select upcase(LastName) || ' ' || FirstName as Name
    from YKT6570.Student
    where DateOfBirth > '01Jan2000'
       or index(FirstName, 'in') > 0;
quit;

/* 5. Display the student ID and their rounded marks from the enrolment data */
proc sql;
    select StudentID, round(Marks) as ROUNDEDMARKS
    from YKT6570.Enrolment;
quit;
