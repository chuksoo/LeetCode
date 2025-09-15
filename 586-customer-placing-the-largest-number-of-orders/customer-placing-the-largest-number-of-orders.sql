# Write your MySQL query statement below
WITH all_orders AS (
    SELECT 
        customer_number
        , COUNT(customer_number) as customer_orders
    FROM Orders
    GROUP BY 1
    ORDER BY 2 DESC
)

SELECT 
    customer_number 
FROM all_orders 
LIMIT 1
