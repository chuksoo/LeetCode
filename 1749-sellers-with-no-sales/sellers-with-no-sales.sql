# Write your MySQL query statement below
SELECT
    s.seller_name
FROM Seller s
LEFT JOIN Orders o
ON s.seller_id = o.seller_id
WHERE s.seller_id NOT IN (
    SELECT 
        DISTINCT seller_id
    FROM Orders 
    WHERE DATE_FORMAT(sale_date, '%Y') = '2020'
)
ORDER BY 1 ASC
