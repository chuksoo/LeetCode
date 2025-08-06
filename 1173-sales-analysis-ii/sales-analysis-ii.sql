# Write your MySQL query statement below
WITH s8_buyers AS (
    SELECT DISTINCT s.buyer_id
    FROM Sales s
    JOIN Product p ON s.product_id = p.product_id
    WHERE p.product_name = 'S8'
),
iphone_buyers AS (
    SELECT DISTINCT s.buyer_id
    FROM Sales s
    JOIN Product p ON s.product_id = p.product_id
    WHERE p.product_name = 'iPhone'
)
SELECT buyer_id
FROM s8_buyers
WHERE buyer_id NOT IN (
    SELECT buyer_id 
    FROM iphone_buyers 
    WHERE buyer_id IS NOT NULL
)
