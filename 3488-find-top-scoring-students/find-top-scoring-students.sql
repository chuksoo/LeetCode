# Write your MySQL query statement below
WITH student_major_courses AS (
    -- Get all courses available in each student's major
    SELECT s.student_id, s.name, s.major, c.course_id
    FROM students s
    JOIN courses c ON s.major = c.major
),
student_enrollments AS (
    -- Get students who took courses in their major with grades
    SELECT s.student_id, s.major, e.course_id, e.grade
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    WHERE s.major = c.major
),
student_stats AS (
    -- Calculate stats for each student
    SELECT 
        smc.student_id,
        smc.major,
        COUNT(DISTINCT smc.course_id) AS total_major_courses,
        COUNT(DISTINCT se.course_id) AS courses_taken,
        COUNT(DISTINCT CASE WHEN se.grade = 'A' THEN se.course_id END) AS courses_with_a
    FROM student_major_courses smc
    LEFT JOIN student_enrollments se ON smc.student_id = se.student_id 
                                      AND smc.course_id = se.course_id
    GROUP BY smc.student_id, smc.major
)

SELECT student_id
FROM student_stats
WHERE total_major_courses = courses_taken 
  AND courses_taken = courses_with_a
ORDER BY student_id ASC;





