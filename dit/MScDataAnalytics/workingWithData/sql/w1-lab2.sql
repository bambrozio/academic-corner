/* Task 2 */

drop table student cascade constraints;

create table STUDENT (
  student_number VARCHAR2(20) PRIMARY KEY,
  first_name VARCHAR2(20),
  surname VARCHAR2(20),
  dob DATE,
  prog_code VARCHAR2(6)
);

insert into STUDENT (student_number, first_name, surname, dob, prog_code)
values ('D020150120', 'Brendan', 'Tierney', to_date('19/01/1995', 'DD/MM/YYYY'), 'DT228B');

insert into STUDENT (student_number, first_name, surname, dob, prog_code)
values ('D020150121', 'Damian', 'Gordon', to_date('20/06/1965', 'DD/MM/YYYY'), 'DT228B');

insert into STUDENT (student_number, first_name, surname, dob, prog_code)
values ('D020150122', 'Deirdre', 'Lawless', to_date('04/10/1973', 'DD/MM/YYYY'), 'DT228B');

insert into STUDENT (student_number, first_name, surname, dob, prog_code)
values ('D020150123', 'Robert', 'Ross', to_date('28/12/2000', 'DD/MM/YYYY'), 'DT228B');

select * from student;
select first_name from student where prog_code = 'DT228B';
select first_name from student where first_name like 'D%';

select * from student where student_number = 'D020150123';

update STUDENT
set prog_code = 'DT228A'
where student_number = 'D020150123';

select * from student where student_number = 'D020150123';

delete from STUDENT where student_number = 'D020150123';
delete from STUDENT where first_name like 'D%';
select * from STUDENT;

/* Task 4 */

insert into student
values ('d1234', 'Bruno', 'Ambrozio', TO_DATE ('27-OCT-00'), 'dt228b');

insert into student
values ('d12345', 'Bruno', 'Ambrozio', TO_DATE('01091986', 'ddmmyyyy'), 'dt228b');

update student
   set dob = TO_DATE('01091986', 'ddmmyyyy'),
       prog_code = 'dt228a'
 where student_number = 'd1234';
 
DROP TABLE course CASCADE CONSTRAINTS;
CREATE TABLE COURSE (
  COURSE_ID int PRIMARY KEY,
  COURSE_CODE VARCHAR2(5),
  COURSE_DESCRIPTION VARCHAR2(20)
)

insert into COURSE VALUES (1, 'c1', 'course c1');
insert into COURSE VALUES (2, 'c2', 'course c2');
insert into COURSE VALUES (3, 'c3', 'course c3');
insert into COURSE VALUES (4, 'c4', 'course c4');

select * from course;

ALTER TABLE course ADD (FULL_PART_TIME NUMBER(1,0));

update course 
  set full_part_time = 1;


/* Lab 3 */
@./master_detail.sql







