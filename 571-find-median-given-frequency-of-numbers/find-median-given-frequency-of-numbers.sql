# Write your MySQL query statement below
WITH expanded AS (
    SELECT num,
           SUM(frequency) OVER (ORDER BY num) - frequency AS lower_num,
           SUM(frequency) OVER (ORDER BY num) AS upper_num,
           SUM(frequency) OVER () / 2 AS medium_num
    FROM Numbers 
)

SELECT AVG(num) AS median
FROM expanded
WHERE medium_num BETWEEN lower_num AND upper_num