# Write your MySQL query statement below
WITH customer_orders_cte AS (
    SELECT c.name, c.customer_id, o.order_id, o.order_date, o.cost, 
        DENSE_RANK () OVER (PARTITION BY c.customer_id ORDER BY order_date DESC) AS 'order_rank'
    FROM Customers c
    JOIN Orders o
    ON c.customer_id = o.customer_id
)
SELECT name AS customer_name, customer_id, order_id, order_date
FROM customer_orders_cte 
WHERE order_rank <= 3
ORDER BY 1 ASC, 2 ASC, 4 DESC