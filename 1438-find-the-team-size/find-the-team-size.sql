# Write your MySQL query statement below
SELECT 
    e.employee_id
    , f.team_size
FROM Employee e
LEFT JOIN (
    SELECT DISTINCT team_id, COUNT(team_id) AS team_size
    FROM Employee
    GROUP BY 1
) AS f
ON e.team_id = f.team_id

