# Write your MySQL query statement below
SELECT 
    DISTINCT c.title
FROM Content c
JOIN TVProgram t
ON c.content_id = t.content_id
WHERE c.Kids_content = 'Y'
AND c.content_type = 'Movies'
AND DATE_FORMAT(t.program_date, '%Y-%m') = '2020-06'