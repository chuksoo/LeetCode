# Write your MySQL query statement below
SELECT
    p1.id AS p1
    , p2.id AS p2
    , ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) AS area
FROM Points p1
CROSS JOIN Points p2
HAVING area != 0 AND p1 < p2
ORDER BY area DESC, p1 ASC, p2 ASC