# Write your MySQL query statement below
SELECT name
FROM (
    SELECT a.id, a.name, a.department, COUNT(b.managerId) AS manager_count
    FROM Employee a
    JOIN Employee b
    ON a.id = b.managerId
    GROUP BY a.id, a.name, a.department
    HAVING COUNT(b.managerId) >= 5
) AS manager_table


