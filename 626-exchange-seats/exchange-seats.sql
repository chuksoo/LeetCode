# Write your MySQL query statement below
WITH prev_next_student AS (
    SELECT 
        id, student, 
        LAG(student, 1) OVER (ORDER BY id) AS prev_student,
        LEAD(student, 1) OVER (ORDER BY id) AS next_student
    FROM Seat
)

SELECT 
    id, 
    CASE
        WHEN (id % 2 != 0 AND next_student IS NOT NULL) THEN next_student
        WHEN (id % 2 = 0 AND next_student IS NOT NULL) THEN prev_student
        WHEN (id % 2 != 0 AND next_student IS NULL) THEN student
        ELSE prev_student
    END AS student
FROM prev_next_student

