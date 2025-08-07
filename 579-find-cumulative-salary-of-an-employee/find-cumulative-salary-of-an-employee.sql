# Write your MySQL query statement below
WITH employee_with_max AS (
    SELECT 
        id, 
        month,
        salary,
        MAX(month) OVER(PARTITION BY id) AS max_month
    FROM Employee
),
employee_without_max AS (
    SELECT id, month, salary 
    FROM employee_with_max 
    WHERE month < max_month 
)

SELECT 
    id, 
    month, 
    -- salary,
    SUM(salary) OVER(
        PARTITION BY id 
        ORDER BY month 
        RANGE 2 PRECEDING
    ) AS Salary
FROM employee_without_max
ORDER BY id ASC, month DESC