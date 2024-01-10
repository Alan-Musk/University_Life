1.

proc sql;
create table s1546489.ADMIN_ENROLMENT6489 like s1546489.Enrolment;
quit;

2.

proc sql;
create table s1546489.EMPLOYEE6489 as select * from s1546489.Trainer;
quit;

3.

proc sql;
select * from s1546489.EMPLOYEE6489;
quit;

4.

proc sql;
select FirstName, LastName, DateOfJoin as HireDate
from s1546489.Trainer
where DateOfJoin > '01Jan2009'
order by DateOfJoin desc;
quit;

5.

proc sql;
select upcase(LastName) || ', ' || FirstName as "Trainer_Name6489"
from s1546489.Trainer;
quit;
