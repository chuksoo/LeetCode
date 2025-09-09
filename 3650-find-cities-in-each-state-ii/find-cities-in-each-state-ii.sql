# Write your MySQL query statement below
WITH
    matching_city_cte AS (
        SELECT DISTINCT
            state
            , COUNT(*) AS matching_letter_count
        FROM cities
        WHERE LEFT(state, 1) = LEFT(city, 1)
        GROUP BY 1
    ),
    grouped_cities_cte AS (
        SELECT
            state
            , GROUP_CONCAT(DISTINCT city ORDER BY city ASC SEPARATOR ', ') AS cities
        FROM cities
        GROUP BY 1
        HAVING COUNT(city) >= 3
    )

SELECT
    m.state
    , g.cities
    , m.matching_letter_count
FROM matching_city_cte m
JOIN grouped_cities_cte g
ON m.state = g.state
ORDER BY 3 DESC, 1 ASC

