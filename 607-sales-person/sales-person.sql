# Write your MySQL query statement below
WITH order_red AS (
    SELECT s.sales_id, s.name AS red_name, o.order_id, o.com_id, c.name
    FROM SalesPerson s
    LEFT JOIN Orders o ON s.sales_id = o.sales_id
    LEFT JOIN Company c ON c.com_id = o.com_id
    WHERE c.name = "RED"
)

SELECT name
FROM SalesPerson
WHERE name NOT IN (
    SELECT red_name FROM order_red
) 
