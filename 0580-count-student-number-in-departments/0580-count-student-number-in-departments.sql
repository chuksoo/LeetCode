# Write your MySQL query statement below
WITH dept_student_cte AS (
    SELECT d.dept_id, d.dept_name, s.student_name
    FROM Department d
    LEFT JOIN Student s
    ON d.dept_id = s.dept_id
    )
SELECT 
    dept_name, 
    CASE 
        WHEN student_name IS null THEN 0
        ELSE COUNT(student_Name) 
    END AS student_number
FROM dept_student_cte
GROUP BY 1
ORDER BY 2 DESC, 1 ASC
