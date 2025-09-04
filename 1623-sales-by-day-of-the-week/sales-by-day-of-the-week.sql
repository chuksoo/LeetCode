# Write your MySQL query statement below
WITH 
    all_item_orders_cte AS (
        SELECT
            DAYOFWEEK(o.order_date) AS day_week
            , o.quantity
            , i.item_category
        FROM Orders o
        LEFT JOIN Items i 
        ON o.item_id = i.item_id
    ),
    item_day_week_cte AS (
        SELECT 
            day_week
            , item_category
            , SUM(quantity) AS total_sales
        FROM all_item_orders_cte
        GROUP BY 1, 2
    ),
    sales_by_week AS (
        SELECT 
            item_category 
            , SUM(CASE 
                WHEN day_week = 2 THEN total_sales
                ELSE 0
            END) AS 'Monday'
            , SUM(CASE 
                WHEN day_week = 3 THEN total_sales
                ELSE 0
            END) AS 'Tuesday'
            , SUM(CASE 
                WHEN day_week = 4 THEN total_sales
                ELSE 0
            END) AS 'Wednesday'
            , SUM(CASE 
                WHEN day_week = 5 THEN total_sales
                ELSE 0
            END) AS 'Thursday'
            , SUM(CASE 
                WHEN day_week = 6 THEN total_sales
                ELSE 0
            END) AS 'Friday'
            , SUM(CASE 
                WHEN day_week = 7 THEN total_sales
                ELSE 0
            END) AS 'Saturday'
            , SUM(CASE 
                WHEN day_week = 1 THEN total_sales
                ELSE 0
            END) AS 'Sunday'
        FROM item_day_week_cte
        GROUP BY 1
    )

SELECT DISTINCT 
    ic.item_category AS Category
    , IFNULL(sw.Monday, 0) AS Monday
    , IFNULL(sw.Tuesday, 0) As Tuesday
    , IFNULL(sw.Wednesday, 0) AS Wednesday
    , IFNULL(sw.Thursday, 0) AS Thursday
    , IFNULL(sw.Friday, 0) AS Friday
    , IFNULL(sw.Saturday, 0) AS Saturday
    , IFNULL(sw.Sunday, 0) AS Sunday
FROM Items ic
LEFT JOIN sales_by_week sw
ON ic.item_category = sw.item_category
ORDER BY 1 ASC


