/* 1. Retrieve Major and count of StudentIDs as NumberOfStudents from Student table, grouped by Major, with a minimum of 3 students in each Major */
proc sql;
    select Major, count(StudentID) as NumberOfStudents
    from TH_6437.Student
    group by Major
    having count(StudentID) > 2;
quit;

/* 2. Extract and concatenate uppercase Street and Suburb as Student_Address from Student table where the third letter of FirstName is 'a' */
proc sql;
    select upcase(Street) || ', ' || Suburb as Student_Address
    from TH_6437.Student
    where substr(FirstName, 3, 1) = 'a';
quit;

/* 3. Select CourseCode and calculate the average of Marks as AverageMarks from Enrolment table, grouped and ordered by CourseCode */
proc sql;
    select CourseCode, mean(Marks) as AverageMarks
    from TH_6437.Enrolment
    group by CourseCode
    order by CourseCode;
quit;

/* 4. Create a concatenated uppercase LastName and FirstName as Name from Student table where DateOfBirth is post 01 Jan 2000 or FirstName includes 'in' */
proc sql;
    select upcase(LastName) || ' ' || FirstName as Name
    from TH_6437.Student
    where DateOfBirth > '01Jan2000'
       or index(FirstName, 'in') > 0;
quit;

/* 5. Select StudentID and round Marks as ROUNDEDMARKS from Enrolment table */
proc sql;
    select StudentID, round(Marks) as ROUNDEDMARKS
    from TH_6437.Enrolment;
quit;
