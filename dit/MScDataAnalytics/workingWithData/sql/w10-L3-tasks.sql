/*
Exercises: http://b-tierney.com/msc-working-with-data/wwd_wk3/

Task 1
*/
create table DEPT_COPY as
select * from DEPT;

create table EMP_COPY
as select * from EMP;

create table EMP_DETAILS as
select e.empno,
  e.ename,
  e.job,
  e.sal,
  d.dname,
  d.loc
from emp e 
  inner join dept d on e.DEPTNO = d.DEPTNO;

/*
Task 2
*/

/*Run with F5 or "as a script" button */
set feedback off;
SPOOL ./w10-l3-task2.csv;
  SELECT /*csv*/* FROM emp_copy;
SPOOL OFF;
SPOOL ./w10-l3-task2.json;
  SELECT /*json*/* FROM emp_copy;
SPOOL OFF;
SPOOL ./w10-l3-task2.html;
      SELECT /*html*/* FROM emp_copy;
SPOOL OFF;
set feedback on;


drop table EMP_COPY;
/*imported uisng SQL Developer from file*/
desc EMP_COPY
desc EMP


select d.dname,
  count(e.sal) 
from emp e 
  inner join dept d on e.DEPTNO = d.DEPTNO
GROUP BY d.dname
HAVING d.dname = 'ACCOUNTING'


