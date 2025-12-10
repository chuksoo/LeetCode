# Write your MySQL query statement below
SELECT 
    a.team_name AS home_team 
    , b.team_name AS away_team
FROM teams a 
CROSS JOIN teams b 
WHERE a.team_name != b.team_name