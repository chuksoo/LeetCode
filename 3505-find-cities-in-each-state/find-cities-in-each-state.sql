# Write your MySQL query statement below
SELECT
    state
    , GROUP_CONCAT(DISTINCT city SEPARATOR ', ') AS cities
FROM cities
GROUP BY 1
ORDER BY 1, 2