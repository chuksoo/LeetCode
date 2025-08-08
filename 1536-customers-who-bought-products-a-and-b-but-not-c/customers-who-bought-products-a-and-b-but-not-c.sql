# Write your MySQL query statement below
WITH all_data AS (
    SELECT o.order_id, o.customer_id, c.customer_name, o.product_name 
    FROM Orders o
    JOIN Customers c
    ON o.customer_id = c.customer_id
), 
c_customers AS (
    SELECT customer_id, customer_name, product_name
    FROM all_data
    WHERE product_name = "C"
),
b_customers AS (
    SELECT customer_id, customer_name, product_name
    FROM all_data
    WHERE product_name = "B"
),
a_customers AS (
    SELECT customer_id, customer_name, product_name
    FROM all_data
    WHERE product_name = "A"
)

SELECT customer_id, customer_name 
FROM Customers
WHERE customer_name IN (SELECT customer_name FROM a_customers)
AND customer_name IN (SELECT customer_name FROM b_customers)
AND customer_Name NOT IN (SELECT customer_name FROM c_customers)

