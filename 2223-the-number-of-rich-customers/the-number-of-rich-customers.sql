# Write your MySQL query statement below
SELECT COUNT(DISTINCT customer_id) AS rich_count
FROM (
    SELECT bill_id, customer_id, amount
    FROM Store
    WHERE amount > 500
) AS rich_customers