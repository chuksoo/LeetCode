# Write your MySQL query statement below
SELECT 
    state
    , GROUP_CONCAT(DISTINCT city ORDER BY city ASC SEPARATOR ', ') AS cities
    , SUM(IF(LEFT(state, 1) = LEFT(city, 1), 1, 0)) AS matching_letter_count
FROM cities
GROUP BY 1
HAVING COUNT(city) >= 3 AND matching_letter_count > 0
ORDER BY 3 DESC, 1 ASC

