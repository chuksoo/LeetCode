# Write your MySQL query statement below
WITH all_buyers_cte AS (
    SELECT s.buyer_id, s.seller_id, s.product_id, p.product_name
    FROM Sales s
    JOIN Product p
    ON s.product_id = p.product_id
),
iphone_buyers_cte AS (
    SELECT buyer_id, seller_id, product_name, product_id
    FROM all_buyers_cte
    WHERE product_name = 'iPhone'
)

SELECT DISTINCT buyer_id 
FROM all_buyers_cte
WHERE product_name = 'S8' 
    AND buyer_id NOT IN (SELECT buyer_id FROM iphone_buyers_cte);



