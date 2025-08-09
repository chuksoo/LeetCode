# Write your MySQL query statement below
WITH all_data AS (
    SELECT 
        user_id, 
        spend, 
        transaction_date, 
        RANK () OVER(PARTITION BY user_id ORDER BY transaction_date ASC) AS trans_rnk
    FROM Transactions
    ORDER BY 1  
),
third_transaction_cte AS (
    SELECT user_id, spend, transaction_date, trans_rnk
    FROM all_data
    WHERE trans_rnk = 3
),
preceding_two_transaction AS (
    SELECT 
        user_id, 
        SUM(CASE
            WHEN trans_rnk = 1 THEN spend
            ELSE 0
        END) AS first_spend,
        SUM(CASE
            WHEN trans_rnk = 2 THEN spend
            ELSE 0
        END) AS second_spend
    FROM all_data
    GROUP BY user_id
)

SELECT 
    t.user_id, 
    t.spend AS third_transaction_spend, 
    t.transaction_date AS third_transaction_date  
FROM third_transaction_cte t
JOIN preceding_two_transaction p
ON t.user_id = p.user_id
WHERE t.spend > p.first_spend AND t.spend > p.second_spend
ORDER BY 1 ASC
