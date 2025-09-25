# Write your MySQL query statement below
WITH
    get_next_timestamp_cte AS (
        SELECT
            user_id
            , time_stamp
            , LEAD(time_stamp, 1) OVER(PARTITION BY user_id ORDER BY user_id, time_stamp) AS next_timestamp
            , TIMESTAMPDIFF(SECOND, time_stamp, LEAD(time_stamp, 1) OVER(PARTITION BY user_id ORDER BY user_id, time_stamp)) AS sec_diff
        FROM Confirmations
    )

SELECT 
    DISTINCT user_id
FROM get_next_timestamp_cte
WHERE next_timestamp IS NOT NULL
AND sec_diff <= 86400