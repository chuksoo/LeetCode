# Write your MySQL query statement below
WITH 
    amount_spent_cte AS (
        SELECT 
            c.customer_id
            , c.name
            , DATE_FORMAT(o.order_date, '%Y-%m') AS order_date
        FROM Orders o
        LEFT JOIN Customers c
            ON c.customer_id = o.customer_id
        LEFT JOIN Product p
            ON p.product_id = o.product_id
        WHERE DATE_FORMAT(o.order_date, '%Y-%m') IN ('2020-06', '2020-07')
        GROUP BY 1, 2, 3
        HAVING SUM(p.price * o.quantity) >= 100
    )

SELECT 
    customer_id
    , name
FROM amount_spent_cte 
GROUP BY 1, 2
HAVING COUNT(order_date) > 1

