# Write your MySQL query statement below
WITH
    ranked_performing_drivers_cte AS (
        SELECT
            v.fuel_type
            , v.driver_id
            , t.vehicle_id
            , d.accidents
            , ROUND(AVG(t.rating), 2) AS avg_rating
            , SUM(t.distance) AS tot_dist
            , RANK() OVER(PARTITION BY v.fuel_type ORDER BY AVG(t.rating) DESC, SUM(t.distance) DESC, accidents ASC) AS rnk
        FROM Trips t
        JOIN Vehicles v
        ON t.vehicle_id = v.vehicle_id
        JOIN Drivers d 
        ON v.driver_id = d.driver_id
        GROUP BY v.driver_id, v.fuel_type
    )

SELECT 
    fuel_type
    , driver_id
    , avg_rating AS rating
    , tot_dist AS distance
FROM ranked_performing_drivers_cte
WHERE rnk = 1
ORDER BY 1 ASC
