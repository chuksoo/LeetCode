# Write your MySQL query statement below
WITH group_class AS (
    SELECT class, COUNT(student) as student_count
    FROM Courses
    GROUP BY 1
)

SELECT class
FROM group_class
WHERE student_count >= 5