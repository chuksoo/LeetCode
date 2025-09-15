# Write your MySQL query statement below
WITH
    employee_with_unique_salary AS (
        SELECT 
            employee_id
            , name
            , salary
        FROM Employees
        GROUP BY salary
        HAVING COUNT(*) = 1
    ),
    employee_without_unique_salary AS (
        SELECT * FROM Employees
        EXCEPT
        SELECT * FROM employee_with_unique_salary
    )

SELECT 
    employee_id
    , name
    , salary
    , DENSE_RANK () OVER(ORDER BY salary ASC) AS team_id
FROM employee_without_unique_salary
ORDER BY team_id ASC, employee_id ASC