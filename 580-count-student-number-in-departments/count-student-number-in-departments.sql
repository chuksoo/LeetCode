# Write your MySQL query statement below
WITH all_data AS (
    SELECT d.dept_id, d.dept_name, s.student_name
    FROM Department d
    LEFT JOIN Student s
    ON d.dept_id = s.dept_id
)

SELECT DISTINCT dept_name,
    COUNT(student_name) AS student_number
FROM all_data
GROUP BY 1
ORDER BY 2 DESC, 1 ASC