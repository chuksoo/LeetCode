# Write your MySQL query statement below
SELECT 
    product_id
    , CASE
        WHEN store1 = 0 THEN NULL
        ELSE store1
    END AS store1
    , CASE
        WHEN store2 = 0 THEN NULL
        ELSE store2
    END AS store2
    , CASE
        WHEN store3 = 0 THEN NULL
        ELSE store3
    END AS store3
FROM (
    SELECT 
        DISTINCT product_id
        , SUM(IFNULL((CASE
            WHEN store = 'store1' THEN price
            ELSE 0
        END), 0)) AS store1
        , SUM(IFNULL((CASE
            WHEN store = 'store2' THEN price
            ELSE 0
        END), 0)) AS store2
        , SUM(IFNULL((CASE
            WHEN store = 'store3' THEN price
            ELSE 0
        END), 0)) AS store3
    FROM Products
    GROUP BY 1
) AS product_store
