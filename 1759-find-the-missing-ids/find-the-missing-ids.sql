# Write your MySQL query statement below
WITH
    RECURSIVE customer_ids_cte AS (
        SELECT 1 AS customer_id
        FROM Customers 

        UNION 
        SELECT 
            customer_id + 1
        FROM customer_ids_cte 
        WHERE customer_id < (SELECT MAX(customer_id) FROM Customers)
    )

SELECT customer_id AS ids
FROM customer_ids_cte
EXCEPT
SELECT customer_id
FROM Customers
