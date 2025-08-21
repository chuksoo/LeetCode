# Write your MySQL query statement below
WITH price_change_cte AS (
    SELECT 
        product_id,
        new_price,
        change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
),
ranked_changes AS (
    SELECT 
        product_id,
        new_price,
        change_date,
        ROW_NUMBER () OVER(PARTITION BY product_id ORDER BY change_date DESC) AS row_num
    FROM price_change_cte
),
latest_price AS (
    SELECT 
        product_id,
        new_price AS price
    FROM ranked_changes 
    WHERE row_num = 1
), 
all_products AS (
    SELECT DISTINCT
        product_id
    FROM Products
)

SELECT 
    all_products.product_id, 
    COALESCE(latest_price.price, 10) AS price
FROM all_products 
LEFT JOIN latest_price
ON all_products.product_id = latest_price.product_id


