# Write your MySQL query statement below
WITH order_above_twenty_cte AS (
    SELECT order_id, order_date, customer_id
    FROM Orders
    WHERE invoice > 20
)
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, 
    COUNT(order_id) AS order_count, 
    COUNT(DISTINCT customer_id) AS customer_count
FROM order_above_twenty_cte
GROUP BY 1 
ORDER BY 1 


