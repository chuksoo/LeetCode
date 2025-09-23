# Write your MySQL query statement below
WITH
    order_details_cte AS (
        SELECT
            order_id
            , AVG(quantity) AS avg_qty
            , MAX(quantity) AS max_qty
        FROM OrdersDetails
        GROUP BY 1
    )

SELECT 
    order_id
FROM order_details_cte
WHERE max_qty > (SELECT MAX(avg_qty) FROM order_details_cte)
