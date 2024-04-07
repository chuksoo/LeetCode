# Write your MySQL query statement below
WITH point_update AS (
    SELECT
        t.team_id,
        t.name,
        t.points,
        RANK() OVER (ORDER BY (t.points + p.points_change) DESC, t.name ASC) AS 'afterRnk',
        RANK() OVER (ORDER BY t.points DESC, t.name ASC) AS 'beforeRnk'
    FROM TeamPoints AS t
    JOIN PointsChange AS p
        ON t.team_id = p.team_id
)

SELECT point_update.team_id,
    point_update.name,
    (CAST(point_update.beforeRnk AS SIGNED) - CAST(point_update.afterRnk AS SIGNED)) AS rank_diff
FROM point_update
