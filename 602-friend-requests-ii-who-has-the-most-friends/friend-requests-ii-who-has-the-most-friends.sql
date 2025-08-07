# Write your MySQL query statement below
WITH friend_stats AS (
    SELECT requester_id as id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id
    FROM RequestAccepted
),
most_friends AS (
    SELECT id, COUNT(*) as num
    FROM friend_stats
    GROUP BY 1
)
SELECT id, num
FROM most_friends 
WHERE num >= (SELECT MAX(num) FROM most_friends)

