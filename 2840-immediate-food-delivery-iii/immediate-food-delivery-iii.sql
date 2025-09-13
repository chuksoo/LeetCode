# Write your MySQL query statement below
-- WITH
--     customer_delivery_cte AS (
--         SELECT
--             order_date
--             , customer_pref_delivery_date
--             , CASE
--                 WHEN order_date = customer_pref_delivery_date THEN 'immediate'
--                 ELSE 'scheduled'
--             END AS delivery_preference
--         FROM Delivery
--     ),
--     get_immediate_count_cte AS (
--         SELECT
--             order_date
--             , COUNT(*) AS imm_cnt
--         FROM customer_delivery_cte
--         WHERE delivery_preference = 'immediate'
--         GROUP BY 1
--     ),
--     get_orders_cte AS (
--         SELECT
--             order_date
--             , COUNT(*) AS total_orders
--         FROM Delivery
--         GROUP BY 1   
--     )

-- SELECT
--     go_cte.order_date
--     , ROUND(IFNULL(gi_cte.imm_cnt, 0) / go_cte.total_orders * 100, 2) AS immediate_percentage
-- FROM get_orders_cte go_cte
-- LEFT JOIN get_immediate_count_cte gi_cte
-- ON go_cte.order_date = gi_cte.order_date
-- ORDER BY 1 ASC

SELECT
    order_date
    , ROUND(IFNULL(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END) / COUNT(*), 0)*100, 2) AS immediate_percentage
FROM Delivery
GROUP BY 1
ORDER BY 1 ASC