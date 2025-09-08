# Write your MySQL query statement below
WITH 
    ranked_product_orders_cte AS (
        SELECT
            p.product_name
            , o.product_id
            , o.order_id
            , o.order_date
            , RANK () OVER(PARTITION BY o.product_id ORDER BY o.order_date DESC) AS order_rnk
        FROM Orders o
        JOIN Products p
        ON o.product_id = p.product_id
    )

SELECT 
    product_name
    , product_id
    , order_id
    , order_date 
FROM ranked_product_orders_cte
WHERE order_rnk = 1
ORDER BY product_name ASC, order_id ASC