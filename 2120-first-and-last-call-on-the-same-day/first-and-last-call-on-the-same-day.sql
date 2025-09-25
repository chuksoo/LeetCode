# Write your MySQL query statement below
WITH
    all_calls_cte AS (
        SELECT
            caller_id AS user_id
            , call_time
            , recipient_id
        FROM Calls
        UNION
        SELECT
            recipient_id AS user_id
            , call_time
            , caller_id AS recipient_id
        FROM Calls
    ),
    first_and_last_calls_cte AS (
        SELECT 
            user_id
            , recipient_id
            , DATE(call_time) AS call_day
            , RANK() OVER(PARTITION BY user_id, DATE(call_time) ORDER BY call_time ASC) AS min_call_rnk
            , RANK() OVER(PARTITION BY user_id, DATE(call_time) ORDER BY call_time DESC) AS max_call_rnk
        FROM all_calls_cte 
    )

SELECT
    DISTINCT user_id
FROM first_and_last_calls_cte
WHERE min_call_rnk = 1 OR max_call_rnk = 1
GROUP BY user_id, call_day
HAVING COUNT(DISTINCT recipient_id) = 1
