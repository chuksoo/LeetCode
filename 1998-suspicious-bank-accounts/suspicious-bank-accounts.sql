# Write your MySQL query statement below
WITH
    monthly_income_cte AS (
        SELECT
            account_id
            , DATE_FORMAT(day, '%Y%m') AS day_month
            , SUM(amount) AS income
            , max_income
        FROM Transactions
        JOIN Accounts
        USING(account_id)
        WHERE type = 'Creditor'
        GROUP BY 1, 2
        HAVING income > max_income
    )

SELECT 
    DISTINCT account_id
FROM monthly_income_cte a
JOIN monthly_income_cte b
USING(account_id)
WHERE PERIOD_DIFF(a.day_month, b.day_month) = 1
