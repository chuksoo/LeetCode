# Write your MySQL query statement below
WITH candidate_data AS (
    SELECT 
        DISTINCT c.candidate_id, 
        c.name, 
        c.years_of_exp, 
        c.interview_id, 
        SUM(r.score) OVER(
            PARTITION BY c.interview_id
        ) AS agg_score
    FROM Rounds r
    JOIN Candidates c
    ON r.interview_id = c.interview_id
)

SELECT candidate_id
FROM candidate_data
WHERE years_of_exp >= 2 AND agg_score > 15