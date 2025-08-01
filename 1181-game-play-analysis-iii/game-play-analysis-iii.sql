# Write your MySQL query statement below
WITH game_play_cte AS (
    SELECT 
        *,
        SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date) AS games_played_so_far
    FROM Activity
)
SELECT player_id, event_date, games_played_so_far FROM game_play_cte