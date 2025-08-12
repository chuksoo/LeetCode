# Write your MySQL query statement below
WITH all_data AS (
    SELECT 
        CASE
            WHEN continent = 'America' THEN name
            ELSE NULL
        END AS America,
        CASE
            WHEN continent = 'Asia' THEN name
            ELSE NULL
        END AS Asia,
        CASE
            WHEN continent = 'Europe' THEN name
            ELSE NULL
        END AS Europe
    FROM Student
),
america_cte AS (
    SELECT 
        ROW_NUMBER() OVER(ORDER BY America ASC) as row_num,
        America
    FROM all_data
    WHERE America IS NOT NULL
),
asia_cte AS (
    SELECT 
        ROW_NUMBER() OVER(ORDER BY Asia ASC) as row_num,
        Asia
    FROM all_data
    WHERE Asia IS NOT NULL
),
europe_cte AS (
    SELECT 
        ROW_NUMBER() OVER(ORDER BY Europe ASC) as row_num,
        Europe
    FROM all_data
    WHERE Europe IS NOT NULL
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