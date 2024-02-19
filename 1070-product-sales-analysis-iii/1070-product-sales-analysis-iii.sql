# Write your MySQL query statement below
WITH first_product_year AS (
    SELECT product_id, MIN(year) AS year FROM Sales
    GROUP BY product_id
)

SELECT f.product_id, f.year AS first_year, s.quantity, s.price
FROM first_product_year f
INNER JOIN Sales s
    ON f.product_id = s.product_id AND f.year = s.year

