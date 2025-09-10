# Write your MySQL query statement below
-- SELECT
--     id
--     , drink
--     , ROW_NUMBER() OVER()
--     , LAG(drink, 1) OVER(ORDER BY id) AS prev_drink
-- FROM CoffeeShop

WITH 
    row_counter_cte AS (
        SELECT 
            id
            , drink
            , ROW_NUMBER() OVER() AS row_cnt
        FROM CoffeeShop
    )

SELECT 
    rc.id
    , CASE
        WHEN rc.drink IS NOT NULL THEN rc.drink
        ELSE (SELECT drink FROM row_counter_cte WHERE row_cnt < rc.row_cnt AND drink IS NOT NULL ORDER BY row_cnt DESC LIMIT 1)
    END AS drink
FROM row_counter_cte rc