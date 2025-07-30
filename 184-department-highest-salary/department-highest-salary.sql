# Write your MySQL query statement below
WITH ranked_cte AS (
    SELECT 
        e.name AS Employee, 
        e.salary AS Salary, 
        d.name AS Department, 
        RANK () OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rank_
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id 
)
SELECT Department, Employee, Salary
FROM ranked_cte
WHERE rank_ = 1

