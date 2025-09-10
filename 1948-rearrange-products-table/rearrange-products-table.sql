# Write your MySQL query statement below
WITH 
    all_store_cte AS (
        SELECT
            product_id
            , 'store1' AS store
            , CASE  
                WHEN store1 IS NOT NULL THEN store1
                ELSE NULL
            END AS price
        FROM Products
        
        UNION ALL
        SELECT
            product_id
            , 'store2' AS store
            , CASE  
                WHEN store2 IS NOT NULL THEN store2
                ELSE NULL
            END AS price
        FROM Products

        UNION ALL
        SELECT
            product_id
            , 'store3' AS store
            , CASE  
                WHEN store3 IS NOT NULL THEN store3
                ELSE NULL
            END AS price
        FROM Products
    )

SELECT * 
FROM all_store_cte
WHERE price is NOT NULL

