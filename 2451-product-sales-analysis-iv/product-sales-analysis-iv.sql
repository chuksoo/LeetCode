# Write your MySQL query statement below
WITH product_sales AS (
    SELECT 
        s.user_id, 
        s.product_id, 
        RANK () OVER(PARTITION BY user_id ORDER BY SUM(s.quantity * p.price) DESC) As rnk
    FROM Sales s
    JOIN Product p
    ON s.product_id = p.product_id
    GROUP BY 1, 2
)

SELECT 
    user_id, product_id
FROM product_sales
WHERE rnk = 1

