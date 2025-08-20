# Write your MySQL query statement below
WITH article_views_cte AS (
    SELECT 
        viewer_id, 
        view_date,
        COUNT(DISTINCT viewer_id) as author_count
    FROM Views 
    GROUP BY 2, 1
    HAVING COUNT(DISTINCT article_id) >= 2
)

SELECT DISTINCT viewer_id AS id
FROM article_views_cte
ORDER BY 1 ASC



