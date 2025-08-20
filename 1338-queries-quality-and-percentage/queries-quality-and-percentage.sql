# Write your MySQL query statement below
WITH sum_quality AS (
    SELECT
        DISTINCT query_name,
        SUM(rating / position) AS sum_quality,
        COUNT(query_name) AS query_count
    FROM Queries
    GROUP BY 1
),
rating_less_than_three AS (
    SELECT 
        query_name,
        COUNT(query_name) AS poor_quality_count
    FROM Queries 
    WHERE rating < 3
    GROUP BY 1
)

SELECT 
    s.query_name,
    ROUND((s.sum_quality / s.query_count), 2) AS quality,
    COALESCE(ROUND((100 * r.poor_quality_count / s.query_count), 2), 0) AS poor_query_percentage
FROM sum_quality s
LEFT JOIN rating_less_than_three r
ON s.query_name = r.query_name
