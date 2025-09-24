# Write your MySQL query statement below
WITH all_users_cte AS (
    SELECT  
        user1_id AS user_id
        , user2_id AS friends
    FROM Friendship
    UNION
    SELECT  
        user2_id AS user_id
        , user1_id AS friends
    FROM Friendship
    ORDER BY 1, 2
),
user_likes_cte AS (
    SELECT
        a.user_id
        , l.page_id
        , COUNT(*) AS friends_likes
    FROM all_users_cte AS a 
    JOIN Likes AS l
    ON a.friends = l.user_id
    GROUP BY 2, 1
    ORDER BY 1, 2
)

SELECT 
    u.user_id
    , u.page_id
    , u.friends_likes
FROM user_likes_cte AS u
LEFT JOIN Likes AS l
ON l.user_id = u.user_id AND l.page_id = u.page_id
WHERE l.user_id IS NULL