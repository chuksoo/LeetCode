# Write your MySQL query statement below
WITH product_sales_cte AS (
    SELECT s.seller_id, p.product_name, s.sale_date, s.quantity, s.price
    FROM Sales s
    JOIN Product p
    ON s.product_id = p.product_id
),
sum_product_seller AS (
    SELECT seller_id, SUM(price) AS total_sales_price
    FROM product_sales_cte
    GROUP BY 1
    ORDER BY 1
)

SELECT seller_id
FROM (
    SELECT seller_id
    FROM sum_product_seller
    WHERE total_sales_price = (SELECT MAX(total_sales_price) FROM sum_product_seller)
) AS best_sellers