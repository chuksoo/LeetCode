# Write your MySQL query statement below
SELECT name as Customers
FROM Customers
WHERE id NOT IN (
    SELECT o.customerId
    FROM Customers c
    JOIN Orders o
        ON c.id = o.customerId
)
