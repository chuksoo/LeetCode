# Write your MySQL query statement below
WITH dist_stats AS (
    SELECT x, 
        -- CASE
        --     WHEN (LAG(x, 1) OVER (ORDER BY x)) IS NULL THEN 0
        --     ELSE LAG(x, 1) OVER (ORDER BY x) 
        -- END AS prev_x,
        LEAD(x, 1) OVER (ORDER BY x) AS next_x
    FROM Point
),
shortest_dist AS (
    SELECT ABS(x - next_x) AS shortest 
    FROM dist_stats
    WHERE next_x IS NOT NULL
)

SELECT MIN(shortest) AS shortest
FROM shortest_dist

