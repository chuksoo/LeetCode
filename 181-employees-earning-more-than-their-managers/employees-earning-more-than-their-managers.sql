# Write your MySQL query statement below
WITH manager_salary_cte AS (
    SELECT e.id AS manager_id, e.name AS manager_name, e.salary AS manager_salary
    FROM Employee e 
    JOIN Employee f 
    ON e.id = f.managerId 
),
employee_cte AS (
    SELECT * FROM Employee 
),
check_salary_greater AS (
SELECT DISTINCT name AS Employee, ec.salary, manager_salary, 
    CASE
        WHEN manager_salary < ec.salary THEN 'Yes'
        ELSE 'No'
    END AS emp_salary_greater
FROM employee_cte AS ec
JOIN manager_salary_cte AS mc
ON ec.managerId = manager_id
)

SELECT Employee FROM check_salary_greater
WHERE emp_salary_greater = 'Yes'
