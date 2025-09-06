# Write your MySQL query statement below
WITH 
    amount_spent_cte AS (
        SELECT 
            c.customer_id
            , c.name
            , o.product_id
            , p.price
            , DATE_FORMAT(o.order_date, '%Y-%m') AS order_date
            , o.quantity
            , (p.price * o.quantity) AS amount_spent
        FROM Orders o
        LEFT JOIN Customers c
            ON c.customer_id = o.customer_id
        LEFT JOIN Product p
            ON p.product_id = o.product_id
    ),
    monthly_spend_cte AS (
        SELECT 
            customer_id
            , name
            , order_date
            , SUM(amount_spent) AS monthly_spent
        FROM amount_spent_cte
        WHERE order_date = '2020-06' OR order_date = '2020-07'
        GROUP BY 1, 3
    )
SELECT 
    customer_id
    , name
FROM (
    SELECT 
        DISTINCT customer_id
        , name
    FROM monthly_spend_cte
    WHERE monthly_spent >= 100
    AND order_date = '2020-06'
    UNION ALL 
    SELECT 
        DISTINCT customer_id
        , name
    FROM monthly_spend_cte
    WHERE monthly_spent >= 100
    AND order_date = '2020-07'
) AS freq
GROUP BY 1
HAVING COUNT(*) = 2

