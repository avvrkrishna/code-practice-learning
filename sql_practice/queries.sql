/*SQL query to fetch “FIRST_NAME” from Worker table using the alias name as <WORKER_NAME>*/
SELECT FIRST_NAME AS WORKER_NAME FROM WORKER;

/*SQL query to fetch “FIRST_NAME” from Worker table in upper case*/
SELECT UPPER(FIRST_NAME) FROM WORKER;

/*SQL query to fetch unique values of DEPARTMENT from Worker table.*/
SELECT DISTINCT DEPARTMENT FROM WORKER;

/*SQL query to print the first three characters of  FIRST_NAME from Worker table.*/
SELECT SUBSTRING(FIRST_NAME,1,3) FROM WORKER;

/*SQL query to print the FIRST_NAME and LAST_NAME from Worker table into a single column COMPLETE_NAME. A space char should separate them*/
SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) AS COMPLETE_NAME FROM WORKER;

/* SQL query to fetch departments along with the total salaries paid for each of them.*/
SELECT DEPARTMENT, sum(Salary) from worker group by DEPARTMENT;

/*SQL query to fetch the names of workers who earn the highest salary*/
SELECT FIRST_NAME, SALARY from Worker WHERE SALARY=(SELECT max(SALARY) from Worker);

/*SQL query to print the name of employees having the highest salary in each department*/
SELECT t.DEPARTMENT,t.FIRST_NAME,t.Salary from
(SELECT max(Salary) as TotalSalary,DEPARTMENT from Worker group by DEPARTMENT) as TempNew 
Inner Join Worker t on TempNew.DEPARTMENT=t.DEPARTMENT 
 and TempNew.TotalSalary=t.Salary;
 
 /*SQL query to fetch three min salaries from a table*/
 SELECT distinct Salary from worker a WHERE 3 >= (SELECT count(distinct Salary) from worker b WHERE a.Salary >= b.Salary) order by a.Salary desc;
 
 /*SQL query to fetch three max salaries from a table*/
 SELECT distinct Salary from worker a WHERE 3 >= (SELECT count(distinct Salary) from worker b WHERE a.Salary <= b.Salary) order by a.Salary desc;
 
 /*SQL query to fetch the departments that have less than five people in it*/
 SELECT DEPARTMENT, COUNT(WORKER_ID) as 'Number of Workers' FROM Worker GROUP BY DEPARTMENT HAVING COUNT(WORKER_ID) < 5;

/*SQL query to fetch duplicate records having matching data in some fields of a table*/
SELECT WORKER_TITLE, AFFECTED_FROM, COUNT(*)
FROM Title
GROUP BY WORKER_TITLE, AFFECTED_FROM
HAVING COUNT(*) > 1;

/*SQL query to show only odd rows from a table*/
SELECT * FROM Worker WHERE MOD (WORKER_ID, 2) <> 0;

/*SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets*/
Select * from Worker where FIRST_NAME like '_____h';

/*SQL query to print details of the Workers whose FIRST_NAME ends with ‘a’*/
Select * from Worker where FIRST_NAME like '%a';

/*SQL query to print details of the Workers whose FIRST_NAME contains ‘a’*/
Select * from Worker where FIRST_NAME like '%a%';

/*SQL query to fetch the list of employees with the same salary*/
Select distinct W.WORKER_ID, W.FIRST_NAME, W.Salary 
from Worker W, Worker W1 
where W.Salary = W1.Salary 
and W.WORKER_ID != W1.WORKER_ID;

/*SQL query to show one row twice in results from a table*/
select FIRST_NAME, DEPARTMENT from worker W where W.DEPARTMENT='HR' 
union all 
select FIRST_NAME, DEPARTMENT from Worker W1 where W1.DEPARTMENT='HR';

/*SQL query to fetch intersecting records of two tables*/
(SELECT * FROM Worker)
INTERSECT
(SELECT * FROM WorkerClone);
