# Write your MySQL query statement below
SELECT DISTINCT viewer_id AS id
FROM (
    SELECT 
        viewer_id, 
        view_date,
        COUNT(DISTINCT viewer_id) as author_count
    FROM Views 
    GROUP BY 2, 1
    HAVING COUNT(DISTINCT article_id) >= 2
) AS v
ORDER BY 1 ASC



