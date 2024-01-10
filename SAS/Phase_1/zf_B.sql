1.

proc sql;
    /* Inserting data into the Student table */
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S7869', 'KING', 'Lee', '11May1990', 'Networking', '1 Fairways', 'Croydon');
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S7870', 'BLAKE', 'Edwards', '05Aug1996', 'Programming', '2 Pecos Pl', 'Clayton');
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S7871', 'CLARK', 'Johnson', '21Jun1994', 'Advanced Database', '7 Elsie St', 'Box Hill');
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S6780', 'SMITH', 'John', '21Oct2001', 'Programming', '15 Lonsdale St', 'Clayton');
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S7872', 'JONES', 'Letty', '23Jan2000', 'Advanced Database', '4 Oxley Crt', 'Boronia');
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S7867', 'NEWS', 'Smith', '15Nov1994', 'Networking', '163 Dorset Road', 'Preston');
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S7868', 'SMITH', 'Jones', '05Mar1995', 'Advanced Database', '23 Elsie Street', 'Epping');
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S7866', 'OLENKO', 'Nathan', '15Mar1997', 'Networking', '23 Alto Avenue', 'Essendon');
    INSERT INTO s1546489.Student (StudentID, LastName, FirstName, DateOfBirth, Major, Street, Suburb)
    VALUES
    ('S7864', 'PRATT', 'Reeve', '03Jan2000', 'Networking', 'Unit 8-41 Karingal St', 'Box Hill');

    /* Inserting data into the Trainer table */
    INSERT INTO s1546489.Trainer (TrainerID, LastName, FirstName, DateOfJoin, RoomNum)
    VALUES
    ('101', 'News', 'John', '08Nov2000', '502');
    INSERT INTO s1546489.Trainer (TrainerID, LastName, FirstName, DateOfJoin, RoomNum)
    VALUES
    ('102', 'Senior', 'David', '12Jun2009', '501');
    INSERT INTO s1546489.Trainer (TrainerID, LastName, FirstName, DateOfJoin, RoomNum)
    VALUES
    ('103', 'Arbough', 'June', '01Dec2007', '503');
    INSERT INTO s1546489.Trainer (TrainerID, LastName, FirstName, DateOfJoin, RoomNum)
    VALUES
    ('104', 'Ramoras', 'Anne', '15Nov2018', '505');
    INSERT INTO s1546489.Trainer (TrainerID, LastName, FirstName, DateOfJoin, RoomNum)
    VALUES
    ('105', 'Johnson', 'Alice', '01Feb2014', '504');
    INSERT INTO s1546489.Trainer (TrainerID, LastName, FirstName, DateOfJoin, RoomNum)
    VALUES
    ('106', 'Smithfield', 'William', '22Jun2005', '500');

    /* Inserting data into the Course table */
    INSERT INTO s1546489.Course (CourseCode, CourseTitle, TrainerID)
    VALUES
    ('BIT235', 'Object Oriented Programming', '101');
    INSERT INTO s1546489.Course (CourseCode, CourseTitle, TrainerID)
    VALUES
    ('BIT111', 'Programming Concepts', '105');
    INSERT INTO s1546489.Course (CourseCode, CourseTitle, TrainerID)
    VALUES
    ('BIT101', 'Introduction to IT', '12');
    INSERT INTO s1546489.Course (CourseCode, CourseTitle, TrainerID)
    VALUES
    ('BIT358', 'Advanced Database', '103');
    INSERT INTO s1546489.Course (CourseCode, CourseTitle, TrainerID)
    VALUES
    ('BIT230', 'System Analysis and Design', '106');
    INSERT INTO s1546489.Course (CourseCode, CourseTitle, TrainerID)
    VALUES
    ('BIT231', 'Database Systems', '105');

    /* Inserting data into the Enrolment table */
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S7869', 'BIT235', 88.50, 'HD');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S7870', 'BIT235', 50.20, 'PA');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S7870', 'BIT101', 76.50, 'D');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S7871', 'BIT101', 73.14, 'D');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S6780', 'BIT101', 60.00, 'CR');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S6780', 'BIT358', 98.00, 'HD');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S7872', 'BIT230', 63.50, 'CR');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S7867', 'BIT101', 55.00, 'PA');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S7868', 'BIT358', 43.00, 'N');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)    
    VALUES
    ('S7866', 'BIT101', 57.00, 'PA');
    INSERT INTO s1546489.Enrolment (StudentID, CourseCode, Marks, Grade)
    VALUES
    ('S7864', 'BIT358', 67.00, 'CR');
quit;


2.
proc sql;

    /* Update ROOMNUM for Trainer Anne who joined on 15Nov2018 */
    UPDATE s1546489.Trainer
    SET RoomNum = '509'
    WHERE FirstName = 'Anne' AND DateOfJoin = '15Nov2018';

    /* Update Grade to HD for student S7871 in the Enrolment table */
    UPDATE s1546489.Enrolment
    SET Grade = 'HD'
    WHERE StudentID = 'S7871';

    /* Update LastName to "W" for student Letty */
    UPDATE s1546489.Student
    SET LastName = 'W'
    WHERE FirstName = 'Letty';

    /* Increase MARKS by 10 for student S7870 in course BIT235 */
    UPDATE s1546489.Enrolment
    SET Marks = Marks + 10
    WHERE StudentID = 'S7870' AND CourseCode = 'BIT235';

quit;

3.

proc sql;

    /* Delete the course with code BIT111 from the Course table */
    DELETE FROM s1546489.Course
    WHERE CourseCode = 'BIT111';

    /* Due to the FK,So we need to delete dependent records in the Enrolment table */
    DELETE FROM s1546489.Enrolment
    WHERE StudentID IN (SELECT StudentID FROM s1546489.Student WHERE DateOfBirth = '11May1990');

    /* Delete the student records from the Student table whose date of birth is 11May1990 */
    DELETE FROM s1546489.Student
    WHERE DateOfBirth = '11May1990';

quit;
