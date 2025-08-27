# Write your MySQL query statement below
WITH users_cte AS (
    SELECT
        user_id 
        , join_date
    FROM Users
), 
buyers_cte AS (
    SELECT 
        buyer_id AS user_id
        , COUNT(buyer_id) AS orders_in_2019
    FROM Orders
    WHERE EXTRACT(YEAR FROM order_date) = '2019'
    GROUP BY 1
)
SELECT 
    u.user_id AS buyer_id
    , u.join_date
    , COALESCE(b.orders_in_2019, 0) AS orders_in_2019
FROM users_cte u 
LEFT JOIN buyers_cte b 
ON u.user_id = b.user_id



