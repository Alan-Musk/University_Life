1.

proc sql;
    select Major, count(StudentID) as NumberOfStudents
    from s1546489.Student
    group by Major
    having count(StudentID) > 2;
quit;

2.

proc sql;
    select upcase(Street) || ', ' || Suburb as Student_Address
    from s1546489.Student
    where substr(FirstName, 3, 1) = 'a';
quit;

3.

proc sql;
    select CourseCode, mean(Marks) as AverageMarks
    from s1546489.Enrolment
    group by CourseCode
    order by CourseCode;
quit;

4.

proc sql;
    select upcase(LastName) || ' ' || FirstName as Name
    from s1546489.Student
    where DateOfBirth > '01Jan2000'
       or index(FirstName, 'in') > 0;
quit;

5.

proc sql;
    select StudentID, round(Marks) as ROUNDEDMARKS
    from s1546489.Enrolment;
quit;

