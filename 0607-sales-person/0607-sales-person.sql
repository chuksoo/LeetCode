# Write your MySQL query statement below

SELECT name 
FROM SalesPerson 
WHERE name NOT IN (
    SELECT s.name 
    FROM SalesPerson s
    JOIN Orders o
        ON s.sales_id = o.sales_id
    JOIN Company c
        ON c.com_id = o.com_id
    WHERE c.name = 'RED'
)