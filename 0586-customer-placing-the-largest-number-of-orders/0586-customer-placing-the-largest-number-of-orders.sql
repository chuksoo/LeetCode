# Write your MySQL query statement below
WITH customer_count AS (
    SELECT customer_number, COUNT(customer_number) AS order_count
    FROM Orders
    GROUP BY 1
    )
SELECT customer_number FROM customer_count ORDER BY order_count DESC LIMIT 1
