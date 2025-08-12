# Write your MySQL query statement below
SELECT 
    am.America,
    aa.Asia,
    eu.Europe 
FROM 
    (
        SELECT 
            name AS America,
            ROW_NUMBER() OVER(ORDER BY name ASC) as row_num
        FROM Student
        WHERE continent = 'America' 
    ) AS am
LEFT JOIN 
    (
        SELECT 
            name AS Asia,
            ROW_NUMBER() OVER(ORDER BY name ASC) as row_num
        FROM Student
        WHERE continent = 'Asia' 
    ) AS aa
ON am.row_num = aa.row_num
LEFT JOIN 
    (
        SELECT 
            name AS Europe,
            ROW_NUMBER() OVER(ORDER BY name ASC) as row_num
        FROM Student
        WHERE continent = 'Europe' 
    ) AS eu
ON am.row_num = eu.row_num

