# Write your MySQL query statement below
WITH 
    sales_cte AS (
        SELECT
            sale_date
            , fruit
            , CASE
                WHEN fruit = 'oranges' THEN sold_num*-1
                ELSE sold_num
            END AS sold_num
        FROM Sales
    )

SELECT 
    sale_date
    , SUM(sold_num) AS diff
FROM sales_cte
GROUP BY 1

