# Write your MySQL query statement below
WITH
    confirmed_users_cte AS (
        SELECT
            user_id
            , SUM(IF(action = 'confirmed', 1, 0)) AS count_confirm
            , COUNT(*) AS count_users
        FROM Confirmations
        GROUP BY 1
    ),
    confirmation_rate_cte AS (
        SELECT 
            user_id
            , ROUND((count_confirm / count_users), 2) AS confirmation_rate
        FROM confirmed_users_cte
    )

SELECT 
    s.user_id
    , IFNULL(c.confirmation_rate, 0) AS confirmation_rate
FROM Signups s
LEFT JOIN confirmation_rate_cte c
ON s.user_id = c.user_id

