# Write your MySQL query statement below
WITH post_cte AS (
    SELECT post_id, CONCAT(' ', content, ' ') AS content
    FROM Posts
),
post_topic_matches AS (
    SELECT p.post_id, GROUP_CONCAT(DISTINCT k.topic_id separator ',') AS topic_list
    FROM post_cte p
    JOIN Keywords k
    WHERE INSTR(p.content, CONCAT(' ', LOWER(k.word), ' ')) > 0
    GROUP BY 1
)

SELECT 
    DISTINCT a.post_id,
    IFNULL(b.topic_list, "Ambiguous!") AS topic
FROM Posts a
LEFT JOIN post_topic_matches b
ON a.post_id = b.post_id