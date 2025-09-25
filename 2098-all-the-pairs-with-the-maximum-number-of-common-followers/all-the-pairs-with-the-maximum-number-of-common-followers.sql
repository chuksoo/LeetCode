# Write your MySQL query statement below
WITH
    grouped_followers AS (
        SELECT
            a.user_id AS user1_id
            , b.user_id AS user2_id
            , COUNT(*) AS user_cnt
        FROM Relations AS a
        JOIN Relations AS b
        ON a.user_id < b.user_id AND a.follower_id = b.follower_id
        GROUP BY a.user_id, b.user_id
    )

SELECT 
    user1_id
    , user2_id
FROM grouped_followers
WHERE user_cnt = (SELECT MAX(user_cnt) FROM grouped_followers)