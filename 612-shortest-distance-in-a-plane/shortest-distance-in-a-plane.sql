# Write your MySQL query statement below
WITH euclidean_distance AS (
    SELECT
        SQRT((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2))) AS d
    FROM
        Point2D p1
            JOIN
        Point2D p2 ON p1.x != p2.x OR p1.y != p2.y
)

SELECT 
    ROUND(MIN(d), 2) AS shortest 
FROM euclidean_distance

