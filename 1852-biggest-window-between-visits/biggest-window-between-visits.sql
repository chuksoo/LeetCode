# Write your MySQL query statement below
WITH
    next_visit_cte AS (
        SELECT 
            user_id
            , visit_date
            , IFNULL(LEAD(visit_date, 1) OVER(PARTITION BY user_id ORDER BY visit_date ASC), '2021-1-1') AS next_visit
        FROM UserVisits
    ),
    get_window_days_cte AS (
        SELECT
            user_id
            , visit_date
            , next_visit
            , DATEDIFF(next_visit, visit_date) AS biggest_window
            , RANK() OVER(PARTITION BY user_id ORDER BY DATEDIFF(next_visit, visit_date) DESC) AS date_rnk
        FROM next_visit_cte
    )

SELECT 
    DISTINCT user_id
    , biggest_window
FROM get_window_days_cte
WHERE date_rnk = 1
ORDER BY 1