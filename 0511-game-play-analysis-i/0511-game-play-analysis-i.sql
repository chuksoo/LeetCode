# Write your MySQL query statement below
WITH ranked_login AS (
    SELECT 
        player_id, 
        event_date, 
        DENSE_RANK () OVER (PARTITION BY player_id ORDER BY event_date ASC) AS 'rank'
    FROM Activity
)

SELECT player_id, event_date AS first_login
FROM ranked_login 
WHERE ranked_login.rank = 1

