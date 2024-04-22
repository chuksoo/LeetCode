# Write your MySQL query statement below
WITH counter_cte AS (
    SELECT num, COUNT(num) as num_count FROM MyNumbers
    GROUP BY 1
    HAVING COUNT(num) = 1
)

SELECT MAX(num) AS num FROM counter_cte