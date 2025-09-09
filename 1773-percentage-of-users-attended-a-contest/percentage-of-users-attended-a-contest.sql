# Write your MySQL query statement below
SELECT
    contest_id
    , ROUND(100 * COUNT(user_id) / (SELECT COUNT(user_id) FROM Users), 2) AS percentage
FROM Register
GROUP BY 1
ORDER BY 2 DESC, 1 ASC