# Write your MySQL query statement below
WITH average_event_cte AS (
    SELECT 
        event_type,
        AVG(occurrences) AS avg_activity
    FROM Events
    GROUP BY 1
),
business_strictly_greater AS (
    SELECT 
        e.business_id,
        e.event_type,
        (e.occurrences - a.avg_activity) AS diff
    FROM Events e
    LEFT JOIN average_event_cte a
    ON e.event_type = a.event_type
    HAVING diff > 0
),
active_businesses AS (
    SELECT business_id, COUNT(event_type) AS active_business
    FROM business_strictly_greater
    GROUP BY 1
)

SELECT business_id 
FROM active_businesses
WHERE active_business >= 2


