# Write your MySQL query statement below
WITH 
    working_day_count_cte AS (
        SELECT
            1 AS id
            , COUNT(DAYNAME(submit_date)) AS working_cnt
        FROM Tasks
        WHERE DAYNAME(submit_date) = 'Monday'
        OR DAYNAME(submit_date) = 'Tuesday'
        OR DAYNAME(submit_date) = 'Wednesday'
        OR DAYNAME(submit_date) = 'Thursday'
        OR DAYNAME(submit_date) = 'Friday'
    ),
    weekend_count_cte AS (
        SELECT
            1 AS id
            , COUNT(DAYNAME(submit_date)) AS weekend_cnt
        FROM Tasks
        WHERE DAYNAME(submit_date) = 'Saturday'
        OR DAYNAME(submit_date) = 'Sunday'
    )

SELECT
    a.weekend_cnt
    , b.working_cnt
FROM weekend_count_cte AS a
JOIN working_day_count_cte AS b
ON a.id = b.id