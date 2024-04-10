# Write your MySQL query statement below
WITH employee_correct_cte AS (
    SELECT employee_id
    FROM Employees
    WHERE employee_id IN (
        SELECT employee_id FROM Salaries)
), 
all_employee_cte AS (
    SELECT employee_id 
    FROM Employees
    UNION
    SELECT employee_id FROM Salaries
) 
SELECT employee_id
FROM all_employee_cte 
WHERE employee_id NOT IN (SELECT employee_id FROM employee_correct_cte)
ORDER BY 1