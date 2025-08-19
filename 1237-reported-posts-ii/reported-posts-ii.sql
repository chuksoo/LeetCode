# Write your MySQL query statement below
WITH reported_post AS (
    SELECT  
        COUNT(DISTINCT a.post_id) AS total_spams,
        COUNT(DISTINCT r.post_id) AS removed
    FROM Actions a
    LEFT JOIN Removals r
    ON a.post_id = r.post_id
    WHERE action = 'report'
    AND extra = 'spam'
    GROUP BY action_date
),
total_reported_cte AS (
        SELECT (100 * removed / total_spams) AS percentage
        FROM reported_post
) 

SELECT 
    ROUND(AVG(percentage), 2) AS average_daily_percent
FROM total_reported_cte



