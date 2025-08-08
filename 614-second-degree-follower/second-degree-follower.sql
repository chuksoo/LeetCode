# Write your MySQL query statement below
WITH follower_count_cte AS (
    SELECT followee, COUNT(follower) AS cnt
    FROM Follow
    GROUP BY 1
    ORDER BY 1 ASC
),
second_degree_users AS (
    SELECT DISTINCT followee AS sdu
    FROM Follow
    WHERE followee IN (SELECT DISTINCT follower FROM Follow)
)

SELECT followee AS follower, cnt AS num
FROM follower_count_cte
HAVING followee IN (SELECT sdu FROM second_degree_users)



