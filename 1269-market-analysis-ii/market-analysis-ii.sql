# Write your MySQL query statement below
WITH report_cte AS (
    SELECT 
        o.seller_id
        , u.favorite_brand
        , o.order_date
        , i.item_brand
        , RANK () OVER(PARTITION BY o.seller_id ORDER BY o.order_date ASC) AS row_rnk
    FROM Users u 
    JOIN Orders o 
    ON u.user_id  = o.seller_id 
    JOIN Items i 
    ON o.item_id = i.item_id 
),
result_cte AS (
    SELECT  
        seller_id
        , CASE
            WHEN (favorite_brand = item_brand) THEN 'yes'
            ELSE 'no'
        END AS 2nd_item_fav_brand
    FROM report_cte 
    WHERE row_rnk = 2
)

SELECT 
    DISTINCT u.user_id AS seller_id
    , COALESCE(r.2nd_item_fav_brand, 'no') AS 2nd_item_fav_brand
FROM Users u 
LEFT JOIN result_cte r 
ON u.user_id = r.seller_id