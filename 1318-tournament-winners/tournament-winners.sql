# Write your MySQL query statement below
WITH player_scores AS (
    -- Calculate total points for each player
    SELECT 
        p.player_id,
        p.group_id,
        COALESCE(SUM(
            CASE 
                WHEN m.first_player = p.player_id THEN m.first_score
                WHEN m.second_player = p.player_id THEN m.second_score
                ELSE 0
            END
        ), 0) AS total_points
    FROM Players p
    LEFT JOIN Matches m ON (p.player_id = m.first_player OR p.player_id = m.second_player)
    GROUP BY p.player_id, p.group_id
),
ranked_players AS (
    -- Rank players within each group
    SELECT 
        group_id,
        player_id,
        total_points,
        RANK() OVER (
            PARTITION BY group_id 
            ORDER BY total_points DESC, player_id ASC
        ) as rnk
    FROM player_scores
)

SELECT 
    group_id,
    player_id
FROM ranked_players
WHERE rnk = 1
ORDER BY group_id
