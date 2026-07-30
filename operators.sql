USE d23r;
show tables;
select * from students;

-- Addition
UPDATE students SET marks=marks+500 
WHERE stu_id=101;
SET SQL_SAFE_UPDATES = 0;

SELECT *,marks+500 as new_marks FROM students;

-- Subtraction
UPDATE students SET marks= marks-500 
WHERE stu_id = 102;
INSERT INTO students VALUE(103,'Raghu',3900);
-- Multiplication
UPDATE students SET marks = marks*2
where stu_id = 103;

-- Division
UPDATE students SET marks = marks/2
WHERE stu_id = 104; 
INSERT INTO students VALUES(105,'ram',4300);
-- remainder
UPDATE students SET marks = marks%10
WHERE stu_id = 105;
SELECT * FROM students;

-- Comparision Operators: It compare the values in the table
-- We run the comparision operator in where clause

-- = : equal operator
SELECT * FROM students WHERE stu_name='Bhai';

-- != : Not Equal to Operator
SELECT * FROM students WHERE stu_name != 'Varun';

-- less than (<):
SELECT *  FROM students WHERE marks < 3000;

-- greater than (>)
SELECT * FROM students WHERE marks > 3000;

-- less than or equal to 
SELECT * FROM students WHERE marks <= 2000;

-- greater than or equal to 
SELECT * FROM students WHERE marks >= 3000;

select * from students;


-- logical operators: 
SELECT * FROM students WHERE marks > 3000 and stu_name='Varun';

SELECT * FROM students WHERE marks > 5000 or stu_name < 'mahesh'; 

SELECT * FROM students WHERE stu_name <'mahesh';
-- XOR: 1 - 1 -->0 1 - 0 --> 1 0 - 1 --> 1 0-0 -->1
SELECT * FROM students WHERE marks >3000 xor stu_name < 'Bhai';

SELECT * FROM students WHERE not marks>3000;