# Write your MySQL query statement below
WITH unpopular_books_cte AS (
    SELECT DISTINCT
        b.book_id,
        b.name,
        SUM(o.quantity) OVER(
            PARTITION BY o.book_id
            ORDER BY o.book_id DESC
        ) AS qty_sold,
        CASE
            WHEN TIMESTAMPDIFF(month, b.available_from, '2019-06-23') < 1 THEN 'Exclude'
            ELSE 'Include' 
        END AS books_to_include
    FROM Books b
    LEFT JOIN Orders o
    ON b.book_id = o.book_id
    AND o.dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
)

SELECT 
    book_id,
    name
FROM unpopular_books_cte
WHERE (qty_sold < 10 OR qty_sold IS NULL)
    AND books_to_include = 'Include'
