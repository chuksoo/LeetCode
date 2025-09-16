# Write your MySQL query statement below
WITH 
    high_balance_account_cte AS (
        SELECT
            account
            , SUM(amount) AS balance
        FROM Transactions 
        GROUP BY 1
        HAVING balance > 10000
    )

SELECT
    u.name
    , h.balance
FROM Users u
JOIN high_balance_account_cte h
ON u.account = h.account

