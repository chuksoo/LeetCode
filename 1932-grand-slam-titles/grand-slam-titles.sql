# Write your MySQL query statement below
WITH 
    winning_tournament_cte AS (
        SELECT
            Wimbledon AS tournament
        FROM Championships

        UNION ALL

        SELECT
            Fr_open AS tournament
        FROM Championships

        UNION ALL

        SELECT
            US_open AS tournament
        FROM Championships

        UNION ALL

        SELECT
            Au_open AS tournament
        FROM Championships
    ), 
    games_won_cte AS (
        SELECT 
            tournament AS player_id
            , COUNT(*) AS grand_slams_count
        FROM winning_tournament_cte
        GROUP BY 1
    )

SELECT 
    gw.player_id
    , p.player_name
    , gw.grand_slams_count
FROM games_won_cte gw
LEFT JOIN Players p
ON gw.player_id = p.player_id
