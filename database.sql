CREATE TABLE employees (
id SERIAL PRIMARY KEY,
name VARCHAR(100),
salary INTEGER,
title VARCHAR(100) 
);

INSERT INTO employees(name, salary , title)
VALUES ('Tushar', 65000, 'Backend dev');

SELECT * FROM employees;

INSERT INTO employees(name, salary, title)
VALUES ('Palak', 85400, 'Senior QA'), ('Amrit' , 23000, 'Analyst');

SELECT * FROM employees;

SELECT * FROM employees
WHERE name = 'Palak';

UPDATE employees 
SET title = 'Senior backend dev' WHERE name= 'Tushar';

SELECT * FROM employees;


UPDATE employees SET salary = 50000 WHERE name = 'Amrit';

SELECT * FROM employees; 

SELECT * FROM employees ORDER BY id ASC ;

SELECT * FROM employees ORDER BY id ASC , salary DESC ;

DELETE FROM employees WHERE  name = 'Amrit'; 

SELECT * FROM employees;

INSERT INTO employees(name , salary , title)
values
('Ravi', 135000 , 'Consultant'),
('Sunder', 85000, 'Associate Consultant'),
('Yashes', 35000, 'Analyst');

SELECT * FROM employees;

SELECT name , salary FROM employees
WHERE salary >= 50000 ORDER BY salary DESC; 

DELETE FROM employees 
WHERE salary < 40000;

SELECT * FROM employees ; 

SELECT name , salary FROM employees 
WHERE salary >80000 ORDER BY salary DESC
LIMIT 2;

SELECT name , salary FROM employees 
WHERE salary > 50000 ORDER BY salary DESC
LIMIT 2 OFFSET 1;

