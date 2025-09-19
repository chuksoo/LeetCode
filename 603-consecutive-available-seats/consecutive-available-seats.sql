# Write your MySQL query statement below
WITH seating AS (
    SELECT *,
        LEAD(free, 1) OVER (ORDER BY seat_id) AS next_free,
        LAG(free, 1) OVER (ORDER BY seat_id) AS prev_Free
    FROM Cinema
)

SELECT 
    seat_id
FROM seating
WHERE free = 1 AND (next_free = 1 OR prev_free = 1)
ORDER BY seat_id