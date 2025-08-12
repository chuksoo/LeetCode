# Write your MySQL query statement below
WITH product_sales AS (
    SELECT 
        s.user_id, 
        s.product_id, 
        (s.quantity * p.price) As spending
    FROM Sales s
    JOIN Product p
    ON s.product_id = p.product_id
),
product_analysis AS (
    SELECT 
        user_id,
        product_id,
        SUM(spending) as amount_spent
    FROM product_sales
    GROUP BY 1, 2
    ORDER BY 1 ASC, 3 DESC
), 
product_ranking AS (
    SELECT 
        *,
        RANK () OVER(PARTITION BY user_id ORDER BY amount_spent DESC) as rnk
    FROM product_analysis
)

SELECT 
    user_id, product_id
FROM product_ranking
WHERE rnk = 1

