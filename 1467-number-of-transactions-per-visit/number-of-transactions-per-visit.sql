# Write your MySQL query statement below
WITH 
    RECURSIVE transaction_numbers AS (
        SELECT 
            0 AS transactions_count
        UNION ALL
        SELECT transactions_count + 1
        FROM transaction_numbers
        WHERE transactions_count < 
            (
                SELECT MAX(transactions_count)
                FROM 
                    (SELECT 
                        v.user_id 
                        , v.visit_date
                        , COUNT(t.amount) AS transactions_count
                    FROM Visits v
                    LEFT JOIN Transactions t
                        ON v.user_id = t.user_id AND v.visit_date = t.transaction_date
                    GROUP BY 1, 2
                    ) AS trans_visit
            )
    ),
    transactions_per_visit AS (
        SELECT 
            v.user_id 
            , v.visit_date
            , COUNT(t.amount) AS transactions_count
        FROM Visits v
        LEFT JOIN Transactions t
            ON v.user_id = t.user_id AND v.visit_date = t.transaction_date
        GROUP BY 1, 2
    ),
    visits_by_transaction_count AS (
        SELECT
            transactions_count
            , COUNT(transactions_count) AS visits_count
        FROM transactions_per_visit
        GROUP BY 1
    )
    
SELECT 
    tn.transactions_count
    , COALESCE(vc.visits_count, 0) AS visits_count
FROM transaction_numbers tn
LEFT JOIN visits_by_transaction_count vc
ON tn.transactions_count = vc.transactions_count
ORDER BY tn.transactions_count 

