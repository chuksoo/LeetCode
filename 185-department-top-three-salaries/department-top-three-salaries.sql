# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
    SELECT 
        e.name AS Employee, 
        e.salary AS Salary, 
        d.name AS Department, 
        DENSE_RANK () OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rank_
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id 
) AS ranked_cte
WHERE rank_ <= 3
