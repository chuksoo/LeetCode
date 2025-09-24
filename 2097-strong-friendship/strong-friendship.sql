# Write your MySQL query statement below
WITH 
    bidirectional_friends_cte AS (
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
    )

SELECT 
    f.user1_id
    , f.user2_id
    , COUNT(DISTINCT bf1.friends) AS common_friend
FROM Friendship AS f
JOIN bidirectional_friends_cte AS bf1
ON bf1.user_id = f.user1_id
JOIN bidirectional_friends_cte AS bf2
ON bf2.user_id = f.user2_id
WHERE bf1.friends = bf2.friends
GROUP BY 1, 2
HAVING common_friend >= 3
