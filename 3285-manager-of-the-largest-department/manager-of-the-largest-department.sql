# Write your MySQL query statement below
WITH
    employee_count_cte AS (
        SELECT 
            DISTINCT dep_id
            , COUNT(dep_id) AS emp_cnt
        FROM Employees
        GROUP BY 1
    ),
    largest_dept_cte AS (
        SELECT dep_id
            , emp_cnt
        FROM employee_count_cte
        WHERE emp_cnt = (SELECT MAX(emp_cnt) FROM employee_count_cte)
    )

SELECT 
    e.emp_name AS manager_name
    , e.dep_id
FROM Employees e
JOIN largest_dept_cte l
ON e.dep_id = l.dep_id
WHERE e.position = 'Manager'
ORDER BY e.dep_id ASC

