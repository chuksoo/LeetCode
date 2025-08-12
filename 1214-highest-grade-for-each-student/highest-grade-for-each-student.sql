# Write your MySQL query statement below
WITH student_highest_grade AS (
    SELECT 
        student_id, 
        course_id,
        grade, 
        DENSE_RANK () OVER(PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS rnk
    FROM Enrollments
)

SELECT student_id, course_id, grade
FROM student_highest_grade
WHERE rnk = 1
ORDER BY 1 ASC 