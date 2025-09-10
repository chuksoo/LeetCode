# Write your MySQL query statement below
SELECT 
    SUM(apple_count) AS apple_count
    , SUM(orange_count) AS orange_count
FROM (
    SELECT
        b.box_id
        , b.chest_id
        , (IFNULL(b.apple_count, 0) + IFNULL(c.apple_count, 0)) AS apple_count
        , (IFNULL(b.orange_count, 0) + IFNULL(c.orange_count, 0)) AS orange_count
    FROM Boxes b
    LEFT JOIN Chests c
    ON b.chest_id = c.chest_id
) AS sums
