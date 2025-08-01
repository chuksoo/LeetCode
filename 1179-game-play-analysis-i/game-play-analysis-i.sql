# Write your MySQL query statement below
WITH ranked_logins AS (
    SELECT 
        player_id, 
        device_id, 
        event_date, 
        games_played, 
        RANK () OVER(PARTITION BY player_id ORDER BY event_date ASC) as login_rank
    FROM Activity
)
SELECT player_id, event_date AS first_login FROM ranked_logins WHERE login_rank = 1