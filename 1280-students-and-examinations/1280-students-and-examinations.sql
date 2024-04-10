# Write your MySQL query statement below

WITH crossjoin_student_subject_cte AS (
    SELECT *
    FROM Students 
    CROSS JOIN Subjects 
    ), 
student_exam_attended_cte AS (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
    )

SELECT 
    c.student_id, 
    c.student_name, 
    c.subject_name, 
    CASE
        WHEN s.attended_exams IS null THEN 0
        ELSE s.attended_exams
    END AS attended_exams
FROM crossjoin_student_subject_cte c
LEFT JOIN student_exam_attended_cte s
ON c.student_id = s.student_id AND c.subject_name = s.subject_name
ORDER BY 1, 2, 3
