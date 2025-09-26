# Write your MySQL query statement below
WITH 
    systems_data AS (
        SELECT
            fail_date AS period_date
            , 'failed' AS period_state 
        FROM Failed
        UNION ALL
        SELECT 
            success_date AS period_date
            , 'succeeded' AS period_state 
        FROM Succeeded
        ORDER BY period_date ASC
    ),
    ranked_period_cte AS (
        SELECT 
            period_date
            , period_state 
            , ROW_NUMBER() OVER(ORDER BY period_date) AS row_cnt
            , RANK () OVER (PARTITION BY period_state ORDER BY period_date ASC, period_state ASC) AS rnk
        FROM systems_data
        WHERE period_date BETWEEN '2019-01-01' AND '2019-12-31'
        ORDER BY period_date ASC
    ),
    ranked_diff_cte AS (
        SELECT 
            period_date
            , period_state
            , (row_cnt - rnk) AS period
        FROM ranked_period_cte
        ORDER BY period_date ASC
    )

SELECT 
    period_state
    , MIN(period_date) AS start_date
    , MAX(period_date) AS end_date
FROM ranked_diff_cte
GROUP BY period, period_state


