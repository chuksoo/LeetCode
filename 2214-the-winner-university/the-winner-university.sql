# Write your MySQL query statement below
WITH excellent_student_count AS (
    SELECT
        (SELECT COUNT(*) FROM NewYork WHERE score >= 90) as ny,
        (SELECT COUNT(*) FROM California WHERE score >= 90) as cali 
)

SELECT 
    CASE
        WHEN e.ny > e.cali THEN "New York University"
        WHEN e.ny < e.cali THEN "California University"
        ELSE "No Winner"
    END AS winner
FROM excellent_student_count e