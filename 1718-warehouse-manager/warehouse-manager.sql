# Write your MySQL query statement below
WITH 
    product_volume_cte AS (
        SELECT
            product_id
            , product_name
            , (Width * Length * Height) AS product_volume
        FROM Products
    )

SELECT 
    w.name AS warehouse_name
    , SUM(w.units * pv.product_volume) AS volume
FROM product_volume_cte pv
JOIN Warehouse w
ON pv.product_id = w.product_id
GROUP BY w.name