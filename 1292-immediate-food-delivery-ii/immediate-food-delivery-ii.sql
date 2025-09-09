# Write your MySQL query statement below
WITH ranked_delivery AS (
    SELECT 
        customer_id,
        delivery_id,
        order_date,
        customer_pref_delivery_date,
        RANK() OVER(PARTITION BY customer_id ORDER BY order_date ASC) AS row_rnk
    FROM Delivery
),
get_order_details AS (
    SELECT 
        customer_id,
        CASE 
            WHEN (order_date = customer_pref_delivery_date) THEN 'immediate'
            ELSE 'schedule'
        END AS order_detail 
    FROM ranked_delivery
    WHERE row_rnk = 1
)

SELECT 
    ROUND(((SELECT COUNT(customer_id) FROM get_order_details WHERE order_detail = 'immediate') / (SELECT COUNT(customer_id) FROM get_order_details) * 100), 2) AS immediate_percentage