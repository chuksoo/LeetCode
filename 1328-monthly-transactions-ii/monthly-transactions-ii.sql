WITH chargeback_cte AS (
    SELECT 
        DISTINCT c.trans_id AS id
        , t.country
        , 'chargeback' AS state
        , t.amount
        , c.trans_date
    FROM Chargebacks c
    LEFT JOIN Transactions t 
    ON c.trans_id = t.id
),
all_data AS (
    SELECT DISTINCT * FROM Transactions WHERE state = 'approved'
    UNION ALL
    SELECT * FROM chargeback_cte  
)

SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month
    , country
    , SUM(state = 'approved') AS approved_count
    , SUM(
        CASE 
            WHEN state = 'approved' THEN amount 
            ELSE 0
        END
    ) AS approved_amount
    , SUM(state = 'chargeback') AS chargeback_count
    , SUM(
        CASE 
            WHEN state = 'chargeback' THEN amount 
            ELSE 0
        END
    ) AS chargeback_amount
FROM all_data
GROUP BY 1, 2

