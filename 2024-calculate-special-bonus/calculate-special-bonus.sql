# Write your MySQL query statement below
WITH
    employee_with_bonus AS (
        SELECT
            employee_id
            , salary AS bonus
        FROM Employees
        WHERE LEFT(name, 1) != 'M' AND employee_id % 2 != 0
    )

SELECT 
    DISTINCT e.employee_id
    , IFNULL(eb.bonus, 0) AS bonus
FROM Employees e
LEFT JOIN employee_with_bonus eb
ON e.employee_id = eb.employee_id
ORDER BY 1
