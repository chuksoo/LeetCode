# Write your MySQL query statement below
WITH RECURSIVE employee_hierarchy AS (
    -- Base Case: Find all direct reports to employee 1 (Head of company)
    SELECT employee_id, manager_id, 1 as level
    FROM Employees 
    WHERE manager_id = 1 
      AND employee_id != 1  -- Exclude the head itself

UNION ALL

-- Recursive Case: Find employees who report to current level employees
SELECT e.employee_id, e.manager_id, eh.level + 1
FROM Employees e
JOIN employee_hierarchy eh 
    ON e.manager_id = eh.employee_id  -- Current employee's manager is in our hierarchy
WHERE eh.level < 3  -- Limit recursion depth to 3 levels
)

SELECT DISTINCT employee_id
FROM employee_hierarchy
ORDER BY 1