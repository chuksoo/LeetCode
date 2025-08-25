# Write your MySQL query statement below
WITH unique_post_id AS (
    SELECT DISTINCT sub_id AS post_id
    FROM Submissions
    WHERE parent_id IS NULL
    ORDER BY sub_id ASC
)

SELECT 
    u.post_id, 
    COUNT(DISTINCT s.sub_id) AS number_of_comments
FROM unique_post_id u
LEFT JOIN Submissions s
ON u.post_id = s.parent_id
GROUP BY u.post_id