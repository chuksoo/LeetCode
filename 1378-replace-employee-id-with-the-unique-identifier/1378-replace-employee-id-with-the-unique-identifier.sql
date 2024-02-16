# Write your MySQL query statement below
SELECT empu.unique_id, emp.name 
FROM Employees emp
LEFT JOIN EmployeeUNI empu
ON emp.id = empu.id