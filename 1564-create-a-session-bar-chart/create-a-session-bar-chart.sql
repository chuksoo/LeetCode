# Write your MySQL query statement below
WITH 
    session_minutes_cte AS (
        SELECT session_id
            , duration
            , duration / 60 AS duration_min
        FROM Sessions
    )

SELECT
    '[0-5>' AS bin
    , COUNT(duration_min) AS total
FROM session_minutes_cte
WHERE duration_min < 5
UNION 
SELECT
    '[5-10>' AS bin
    , COUNT(duration_min) AS total
FROM session_minutes_cte
WHERE duration_min > 5 AND duration_min < 10 
UNION
SELECT
    '[10-15>' AS bin
    , COUNT(duration_min) AS total
FROM session_minutes_cte
WHERE duration_min > 10 AND duration_min < 15 
UNION 
SELECT
    '15 or more' AS bin
    , COUNT(duration_min) AS total
FROM session_minutes_cte
WHERE duration_min > 15

