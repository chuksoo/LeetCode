# Write your MySQL query statement below
WITH 
    company_max_salary_cte AS (
        SELECT DISTINCT
            company_id
            , MAX(salary) OVER(PARTITION BY company_id) AS max_salary
        FROM Salaries
    )

SELECT
    s.company_id
    , s.employee_id
    , s.employee_name
    , ROUND(
        (CASE
            WHEN c.max_salary < 1000 THEN (s.salary - s.salary * 0.0)
            WHEN (c.max_salary >= 1000 AND c.max_salary <= 10000) THEN (s.salary - s.salary * 0.24)
            ELSE (s.salary - s.salary * 0.49)
        END), 0) AS salary
FROM Salaries AS s
JOIN company_max_salary_cte AS c
ON s.company_id = c.company_id

