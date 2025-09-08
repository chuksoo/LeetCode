# Write your MySQL query statement below
WITH
    transaction_payment_cte AS (
        SELECT 
            t.paid_by AS user_id
            , u.user_name
            , (t.amount * -1) AS amount
        FROM Transactions t
        JOIN Users u
        ON u.user_id = t.paid_by

        UNION ALL
        SELECT 
            t.paid_to AS user_id
            , u.user_name
            , t.amount 
        FROM Transactions t
        JOIN Users u
        ON u.user_id = t.paid_to       

        UNION ALL
        SELECT
            user_id
            , user_name
            , credit AS amount
        FROM Users 
    )

SELECT 
    user_id
    , user_name
    , SUM(amount) AS credit
    , CASE
        WHEN SUM(amount) <= 0 THEN 'Yes'
        ELSE 'No'
    END AS credit_limit_breached
FROM transaction_payment_cte
GROUP BY 1, 2