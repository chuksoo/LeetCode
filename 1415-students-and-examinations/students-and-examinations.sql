# Write your MySQL query statement below
WITH student_subject_cte AS (
    SELECT 
        a.student_id, 
        a.student_name,
        b.subject_name
    FROM Students a
    CROSS JOIN Subjects b
),
exam_attended AS (
    SELECT 
        student_id
        , subject_name, 
        COUNT(subject_name) AS attended_exams
    FROM Examinations
    GROUP BY 1, 2
)

SELECT 
    c.student_id,
    c.student_name,
    c.subject_name,
    IFNULL(d.attended_exams, 0) AS attended_exams
FROM student_subject_cte c
LEFT JOIN exam_attended d
ON c.student_id = d.student_id
AND c.subject_name = d.subject_name
ORDER BY 1 ASC, 3 ASC


