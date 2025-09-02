# Write your MySQL query statement below
WITH
    ranked_activity_cte AS (
        SELECT 
            username
            , activity
            , startDate
            , endDate
            , RANK() OVER(PARTITION BY username ORDER BY startDate DESC) AS rnk
        FROM UserActivity
    ),
    user_activity_count AS (
        SELECT 
            username
            , COUNT(username) AS activity_count
        FROM ranked_activity_cte
        GROUP BY 1
    ), 
    all_result AS (
        SELECT 
            rac.username
            , rac.activity
            , rac.startDate
            , rac.endDate
            , rac.rnk
            , uac.activity_count
        FROM ranked_activity_cte rac
        LEFT JOIN user_activity_count uac 
        ON rac.username = uac.username
    )

SELECT 
    username
    , activity
    , startDate
    , endDate
FROM all_result
WHERE (rnk = 2 AND activity_count > 1) 
    OR (rnk = 1 AND activity_count = 1)





