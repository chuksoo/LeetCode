# Write your MySQL query statement below
WITH duplicate_numbers AS (
    SELECT num, COUNT(num) AS duplicates
    FROM MyNumbers
    GROUP BY 1
    HAVING COUNT(num) > 1
)

SELECT MAX(num) AS num 
FROM MyNumbers
WHERE num NOT IN (SELECT num FROM duplicate_numbers)