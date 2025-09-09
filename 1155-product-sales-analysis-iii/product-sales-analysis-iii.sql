# Write your MySQL query statement below
WITH 
    ranked_product_sales_cte AS (
        SELECT 
            product_id
            , year 
            , quantity
            , price
            , RANK () OVER (PARTITION BY product_id ORDER BY year ASC) AS prod_rnk
        FROM Sales
    )

SELECT 
    product_id
    , year AS first_year
    , quantity
    , price
FROM ranked_product_sales_cte
WHERE prod_rnk = 1