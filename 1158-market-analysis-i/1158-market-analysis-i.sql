# Write your MySQL query statement below

WITH grouped_cte AS (
    SELECT u.user_id as buyer_id, 
        u.join_date, 
        CASE
            WHEN o.order_date LIKE "2019%" THEN 1
            ELSE 0
        END AS orders_in_2019
    FROM Users u
    LEFT JOIN Orders o 
        ON o.buyer_id = u.user_id
    )
SELECT buyer_id, join_date, SUM(orders_in_2019) as orders_in_2019
FROM grouped_cte
GROUP BY 1, 2
ORDER BY 1
