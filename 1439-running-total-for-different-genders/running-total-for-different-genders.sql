# Write your MySQL query statement below
SELECT 
    gender
    , day
    , SUM(score_points) OVER(PARTITION BY gender ORDER BY day ASC) AS total
FROM Scores
