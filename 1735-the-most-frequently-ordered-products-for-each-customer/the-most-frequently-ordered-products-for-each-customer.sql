# Write your MySQL query statement below
WITH
    order_rnk_cte AS (
        SELECT 
            customer_id
            , product_id
            , RANK () OVER(PARTITION BY customer_id ORDER BY COUNT(product_id) DESC) AS freq_rnk
        FROM Orders
        GROUP BY customer_id, product_id
    ) 

SELECT 
    o.customer_id
    , o.product_id
    , p.product_name
FROM order_rnk_cte o
JOIN Products p
ON o.product_id = p.product_id
WHERE freq_rnk = 1
