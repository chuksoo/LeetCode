# Write your MySQL query statement below
# Using self join
SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a
INNER JOIN Activity b
    ON a.machine_id = b.machine_id
WHERE a.activity_type = 'start' AND b.activity_type = 'end'
GROUP BY 1
ORDER BY 1




