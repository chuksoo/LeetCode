# Write your MySQL query statement below
WITH game_points_cte AS(
    SELECT 
        host_team AS winning_team
        , CASE
            WHEN (host_goals > guest_goals) THEN 3
            WHEN (host_goals = guest_goals) THEN 1
            ELSE 0
        END AS winning_pts
    FROM Matches
    UNION ALL
    SELECT
        guest_team AS winning_team
        , CASE
            WHEN (guest_goals > host_goals) THEN 3
            WHEN (host_goals = guest_goals) THEN 1
            ELSE 0
        END AS winning_pts
    FROM Matches 
),
winning_points_cte AS (
    SELECT 
        DISTINCT winning_team
        , SUM(winning_pts) AS num_points
    FROM game_points_cte
    GROUP BY 1
)

SELECT 
    t.team_id
    , t.team_name
    , COALESCE(w.num_points, 0) AS num_points
FROM Teams t 
LEFT JOIN winning_points_cte w 
ON t.team_id = w.winning_team
ORDER BY 3 DESC, 1 ASC