# Write your MySQL query statement below
SELECT 
    transaction_id
FROM (
    SELECT 
        transaction_id
        , day
        , amount
        , RANK () OVER(PARTITION BY day ORDER BY amount DESC) AS amt_rnk
    FROM Transactions
) AS rnked_trans
WHERE amt_rnk = 1
ORDER BY 1 ASC