# Write your MySQL query statement below
WITH manager_cte AS (
    SELECT managerId
    FROM Employee 
    GROUP BY 1
    HAVING COUNT(managerId) >= 5
)

SELECT name 
FROM Employee
WHERE id IN (
    SELECT managerId FROM manager_cte
)




