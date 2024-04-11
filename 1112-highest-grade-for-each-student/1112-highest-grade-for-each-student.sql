# Write your MySQL query statement below
WITH ranked_enrollments_cte AS (
    SELECT 
        student_id, 
        course_id, 
        grade,
        RANK () OVER(PARTITION BY student_id ORDER BY grade DESC, course_id ASC) rnk
    FROM Enrollments
    )
SELECT 
    student_id, course_id, grade
FROM
    ranked_enrollments_cte
WHERE rnk = 1
ORDER BY 1 ASC
