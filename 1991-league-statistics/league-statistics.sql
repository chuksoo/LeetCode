# Write your MySQL query statement below
WITH
    matches_by_team_cte AS (
        SELECT 
            home_team_id AS team_id
        FROM Matches
        UNION ALL
        SELECT away_team_id
        FROM Matches
    ),
    matches_played_cte AS (
        SELECT 
            team_id
            , COUNT(team_id) AS matches_played
        FROM matches_by_team_cte
        GROUP BY 1
    ),
    game_points_cte AS (
        SELECT
            home_team_id AS team_id
            , SUM(CASE 
                WHEN home_team_goals > away_team_goals THEN 3
                WHEN home_team_goals = away_team_goals THEN 1
                ELSE 0
            END) AS total_goals
            , SUM(home_team_goals) AS goals_for
            , SUM(away_team_goals) AS goals_against
        FROM Matches
        GROUP BY 1
        UNION ALL
        SELECT
        away_team_id
            , SUM(CASE 
                WHEN away_team_goals > home_team_goals THEN 3
                WHEN away_team_goals = home_team_goals THEN 1
                ELSE 0
            END) AS total_goals
            , SUM(away_team_goals) AS goals_for
            , SUM(home_team_goals) AS goals_against
        FROM Matches
        GROUP BY 1        
    ),
    points_cte AS (
        SELECT
            team_id
            , SUM(total_goals) AS points
            , SUM(goals_for) AS goal_for
            , SUM(goals_against) AS goal_against
        FROM game_points_cte
        GROUP BY 1
    )


SELECT 
    t.team_name
    , m.matches_played
    , p.points
    , p.goal_for
    , p.goal_against
    , (p.goal_for - p.goal_against) AS goal_diff
FROM Teams AS t
JOIN matches_played_cte AS m
ON t.team_id = m.team_id
JOIN points_cte AS p
ON p.team_id = t.team_id
ORDER BY 3 DESC, 6 DESC, 1 ASC