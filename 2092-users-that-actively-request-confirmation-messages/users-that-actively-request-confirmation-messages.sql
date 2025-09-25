# Write your MySQL query statement below
WITH
    get_next_timestamp_cte AS (
        SELECT
            user_id
            , time_stamp
            , LEAD(time_stamp, 1) OVER(PARTITION BY user_id ORDER BY user_id, time_stamp) AS next_timestamp
        FROM Confirmations
    ),
    get_timestamp_diff_cte AS (
        SELECT
            user_id
            , TIMESTAMPDIFF(SECOND, time_stamp, next_timestamp) AS sec_diff
        FROM get_next_timestamp_cte
        WHERE next_timestamp IS NOT NULL
    )


SELECT 
    DISTINCT user_id
FROM get_timestamp_diff_cte
WHERE sec_diff <= 86400