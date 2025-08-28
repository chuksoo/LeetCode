# Write your MySQL query statement below
SELECT
    p.product_id
    , (p.price - COALESCE((d.discount/100)*p.price, 0)) AS final_price
    , p.category
FROM Products p 
LEFT JOIN Discounts d 
ON p.category = d.category
ORDER BY 1 ASC
