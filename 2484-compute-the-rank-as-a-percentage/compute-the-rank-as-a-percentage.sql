# Write your MySQL query statement below
WITH student_rank_cte AS (
    SELECT 
        student_Id, 
        department_id,
        RANK () OVER(PARTITION BY department_id ORDER BY mark DESC) as student_rnk
    FROM Students
)

SELECT 
    student_Id, 
    department_id,
    CASE 
        WHEN ROUND((student_rnk - 1) * 100 / (COUNT(student_Id) OVER(PARTITION BY department_id) - 1), 2) IS NULL THEN 0
        ELSE ROUND((student_rnk - 1) * 100 / (COUNT(student_Id) OVER(PARTITION BY department_id) - 1), 2) 
    END AS percentage
FROM student_rank_cte

