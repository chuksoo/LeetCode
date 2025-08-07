# Write your MySQL query statement below
WITH stadium_group AS (
    SELECT id, visit_date, people, id - ROW_NUMBER () OVER(ORDER BY id) as group_id
    FROM Stadium
    WHERE people >= 100
)

SELECT id, visit_date, people
FROM stadium_group
WHERE group_id IN (
    SELECT group_id
    FROM stadium_group
    GROUP BY 1
    HAVING COUNT(group_id) >= 3
)
