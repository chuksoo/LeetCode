# Write your MySQL query statement below
WITH grouped_cte AS (
    SELECT 
        e.id as empId, 
        e.name as Employee, 
        e.salary,
        e.departmentId,
        d.name as Department,
        DENSE_RANK () OVER(PARTITION BY d.name ORDER BY e.salary DESC) rnk
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
    )

SELECT 
    g.Department,
    g.Employee,
    g.salary as Salary
FROM grouped_cte as g
WHERE rnk = 1