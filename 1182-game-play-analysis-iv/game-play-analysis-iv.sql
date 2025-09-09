# Write your MySQL query statement below
WITH first_login_cte AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),
players_with_next_day_login AS (
    SELECT DISTINCT f.player_id
    FROM first_login_cte f
    JOIN Activity a
    ON f.player_id = a.player_id
    WHERE a.event_date = DATE_ADD(f.first_login_date, INTERVAL 1 DAY)
)

SELECT (
    ROUND(
        ((SELECT COUNT(*) FROM players_with_next_day_login) / (SELECT COUNT(DISTINCT player_id) FROM Activity)), 2
    ) 
) AS fraction



