# Write your MySQL query statement below
WITH order_customers AS (
    SELECT 
        DISTINCT visited_on
        , SUM(amount) AS amount
    FROM Customer
    GROUP BY 1
), 
moving_customer_avg AS (
    SELECT
        visited_on
        , SUM(amount) OVER(
            ORDER BY visited_on ASC 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount
        , ROUND(AVG(amount) OVER(
            ORDER BY visited_on ASC 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS average_amount
        , ROW_NUMBER() OVER(ORDER BY visited_on ASC) AS day_avg
    FROM order_customers
)

SELECT 
    visited_on
    , amount
    , average_amount
FROM moving_customer_avg
WHERE day_avg > 6

