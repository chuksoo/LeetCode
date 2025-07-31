# Write your MySQL query statement below
WITH select_cte AS (
    SELECT email, COUNT(email) AS repeat_times 
    FROM Person 
    GROUP BY email
)
SELECT email FROM select_cte WHERE repeat_times >= 2;