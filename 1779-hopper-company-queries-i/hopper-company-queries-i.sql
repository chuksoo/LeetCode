# Write your MySQL query statement below
WITH
    RECURSIVE month_generator AS (
        SELECT 
            1 AS month
        UNION ALL
        SELECT month + 1 AS month
        FROM month_generator
        WHERE month < 12
    ),
    month_generator_with_end_month_cte AS (
        SELECT
            month
            , CASE
                WHEN month IN (1, 3, 5, 7, 8, 10, 12) THEN CONCAT('2020-', month, '-31')
                WHEN month IN (4, 6, 9, 11) THEN CONCAT('2020-', month, '-30')
                ELSE CONCAT('2020-', month, '-29')
            END AS end_month
        FROM month_generator
    ),
    active_drivers_cte AS (
        SELECT 
            m.month
            , COUNT(*) AS active_drivers
        FROM Drivers d
        JOIN month_generator_with_end_month_cte m
        ON d.join_date <= m.end_month
        GROUP BY m.month
    ),
    accepted_rides_cte AS (
        SELECT
            m.month
            , COUNT(ar.driver_id) AS accepted_rides
        FROM month_generator_with_end_month_cte m
        JOIN Rides AS r
        ON m.month = MONTH(r.requested_at)
        JOIN AcceptedRides AS ar
        ON ar.ride_id = r.ride_id
        WHERE YEAR(r.requested_at) = '2020'
        GROUP BY 1
    )

SELECT 
    m.month
    , IFNULL(ad_cte.active_drivers, 0) AS active_drivers
    , IFNULL(ar_cte.accepted_rides, 0) AS accepted_rides
FROM month_generator AS m
LEFT JOIN active_drivers_cte AS ad_cte
ON m.month = ad_cte.month
LEFT JOIN accepted_rides_cte AS ar_cte
ON ad_cte.month = ar_cte.month
ORDER BY ad_cte.month ASC
