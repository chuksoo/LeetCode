# Write your MySQL query statement below
WITH unbanned_trips AS (
    SELECT
        t.id,
        t.status,
        t.request_at
    FROM Trips t
    JOIN Users u_client ON t.client_id = u_client.users_id
    JOIN Users u_driver ON t.driver_id = u_driver.users_id
    WHERE
        u_client.banned = 'No'
        AND u_driver.banned = 'No'
        AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
),
daily_stats AS (
    SELECT
        request_at,
        COUNT(*) AS total_requests,
        SUM(CASE
                WHEN status IN ('cancelled_by_client', 'cancelled_by_driver') THEN 1
                ELSE 0
            END) AS cancelled_requests
    FROM unbanned_trips
    GROUP BY 1
)

SELECT 
    request_at AS 'Day',
    ROUND((cancelled_requests / total_requests), 2) AS 'Cancellation Rate'
FROM daily_stats
ORDER BY 1
