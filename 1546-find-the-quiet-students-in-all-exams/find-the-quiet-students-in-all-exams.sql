# Write your MySQL query statement below
WITH 
    low_scores AS (
        SELECT 
            DISTINCT exam_id
            , student_id
            , score
            , MIN(score) OVER(PARTITION BY exam_id) AS lowest_score
        FROM Exam
    ),
    high_scores AS (
        SELECT 
            DISTINCT exam_id
            , student_id
            , score
            , MAX(score) OVER(PARTITION BY exam_id) AS highest_score
        FROM Exam
    ),
    highest_and_lowest_cte AS (
        SELECT 
            exam_id
            , student_id
            , score
        FROM high_scores
        WHERE score = highest_score
        UNION ALL
        SELECT 
            exam_id
            , student_id
            , score
        FROM low_scores
        WHERE score = lowest_score
        ORDER BY exam_id, score DESC
    )

SELECT 
    DISTINCT s.student_id
    , s.student_name
FROM Student s
RIGHT JOIN Exam e
ON s.student_id = e.student_id
WHERE s.student_id NOT IN (SELECT student_id FROM highest_and_lowest_cte)
ORDER BY s.student_id ASC