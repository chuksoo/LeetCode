# Write your MySQL query statement below
WITH prj_count_cte AS 
(
    SELECT p.project_id, COUNT(*) as emp_count
    FROM Project p
    LEFT JOIN Employee e
    ON p.employee_id = e.employee_id
    GROUP BY 1
    ORDER BY emp_count DESC
)
    
SELECT project_id
FROM prj_count_cte
WHERE emp_count = (SELECT MAX(emp_count) FROM prj_count_cte)
