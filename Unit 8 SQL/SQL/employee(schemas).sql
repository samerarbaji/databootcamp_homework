DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_managers;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;

create table departments(
	dept_no varchar(255) not null,
	dept_name varchar(255) not null,
	primary key(dept_no)
);
create table dept_emp(
	emp_no int not null,
	dept_no varchar(255) not null
	
);
create table dept_managers(
	dept_no varchar(255) not null,
	emp_no int not null
);
create table employees(
	emp_no int not null Primary Key,
	emp_title varchar(255) not null,
	birth_date varchar(255) not null,
	first_name varchar(255) not null,
	last_name varchar(255) not null,
	sex varchar(255) not null,
	hire_date varchar(255) not null
	
);
create table salaries(
	emp_no int not null,
	salary int not null
	
);
create table titles(
	title_id varchar(255) not null,
	title varchar(255) not null
	
);

select * from employees;