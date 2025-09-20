# Write your MySQL query statement below
WITH ranked_cte AS (
    SELECT 
        e.name AS Employee, 
        e.salary AS Salary, 
        d.name AS Department, 
        RANK () OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS sal_rnk
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id 
)
SELECT Department, Employee, Salary
FROM ranked_cte
WHERE sal_rnk = 1
