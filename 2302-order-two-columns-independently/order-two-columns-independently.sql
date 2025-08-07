# Write your MySQL query statement below
WITH first_col_cte AS (
    SELECT first_col, ROW_NUMBER() OVER(ORDER BY first_col ASC) AS rnk_one 
    FROM Data
),
second_col_cte AS (
    SELECT second_col, ROW_NUMBER() OVER(ORDER BY second_col DESC) AS rnk_two 
    FROM Data
)

SELECT fc.first_col, sc.second_col
FROM first_col_cte fc
JOIN second_col_cte sc
ON fc.rnk_one = sc.rnk_two
