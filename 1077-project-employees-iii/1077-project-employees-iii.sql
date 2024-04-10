# Write your MySQL query statement below
WITH rnk_cte AS 
(
    SELECT 
        p.project_id, 
        p.employee_id, 
        RANK () OVER(PARTITION BY project_id ORDER BY experience_years DESC) AS rnk
    FROM Project p
    JOIN Employee e
    ON p.employee_id = e.employee_id
)

SELECT project_id, employee_id 
FROM rnk_cte
WHERE rnk = 1


