# Write your MySQL query statement below
WITH even_transaction_cte AS (
    SELECT SUM(amount) AS even_sum, transaction_date AS even_transaction_date
    FROM transactions
    WHERE amount % 2 = 0
    GROUP BY transaction_date
),
odd_transaction_cte AS (
    SELECT SUM(amount) AS odd_sum, transaction_date AS odd_transaction_date
    FROM transactions
    WHERE amount % 2 != 0
    GROUP BY transaction_date
), 
transaction_table_cte AS (
    SELECT * FROM even_transaction_cte ec 
    LEFT JOIN odd_transaction_cte oc
    ON ec.even_transaction_date = oc.odd_transaction_date
    UNION 
    SELECT * FROM even_transaction_cte ec 
    RIGHT JOIN odd_transaction_cte oc
    ON ec.even_transaction_date = oc.odd_transaction_date
),
main_table_cte AS (
SELECT 
    CASE
        WHEN even_transaction_date IS NULL THEN odd_transaction_date
        ELSE even_transaction_date
    END AS even_transaction_date,
    CASE
        WHEN odd_transaction_date IS NULL THEN even_transaction_date
        ELSE odd_transaction_date
    END AS odd_transaction_date,
    CASE
        WHEN odd_sum IS NULL THEN 0
        ELSE odd_sum
    END AS odd_sum, 
    CASE 
        WHEN even_sum IS NULL THEN 0
        ELSE even_sum 
    END AS even_sum
FROM transaction_table_cte
)

SELECT DISTINCT a.even_transaction_date AS transaction_date, a.odd_sum, a.even_sum
FROM main_table_cte a
JOIN main_table_cte b
ON a.even_transaction_date = b.odd_transaction_date
ORDER BY 1 ASC



