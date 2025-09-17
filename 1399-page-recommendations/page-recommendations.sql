# Write your MySQL query statement below
WITH friends_with_user_one AS (
    SELECT user2_id AS users
    FROM Friendship
    WHERE user1_id = 1

    UNION ALL

    SELECT user1_id AS users
    FROM Friendship 
    WHERE user2_id = 1
)

SELECT 
    DISTINCT l.page_id AS recommended_page
FROM Likes l
JOIN friends_with_user_one f
ON f.users = l.user_id
WHERE l.page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)