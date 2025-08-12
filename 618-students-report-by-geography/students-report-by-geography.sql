# Write your MySQL query statement below
WITH america_cte AS (
    SELECT 
        name AS America,
        ROW_NUMBER() OVER(ORDER BY name ASC) as row_num
    FROM Student
    WHERE continent = 'America' 
),
asia_cte AS (
    SELECT 
        name AS Asia,
        ROW_NUMBER() OVER(ORDER BY name ASC) as row_num
    FROM Student
    WHERE continent = 'Asia' 
),
europe_cte AS (
    SELECT 
        name AS Europe,
        ROW_NUMBER() OVER(ORDER BY name ASC) as row_num
    FROM Student
    WHERE continent = 'Europe' 
)

SELECT 
    am.America,
    aa.Asia,
    eu.Europe
FROM america_cte am
LEFT JOIN asia_cte aa
    ON am.row_num = aa.row_num
LEFT JOIN europe_cte eu
    ON am.row_num = eu.row_num

