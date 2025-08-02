# Write your MySQL query statement below
WITH employee_bonus_cte AS (
    SELECT e.empId, e.name, e.supervisor, e.salary, b.bonus
    FROM Employee e
    LEFT JOIN Bonus b
    ON e.empId = b.empId
)
SELECT name, bonus FROM employee_bonus_cte WHERE bonus < 1000 OR bonus IS NULL