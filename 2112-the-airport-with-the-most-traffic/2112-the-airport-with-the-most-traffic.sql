# Write your MySQL query statement below
WITH joined_airport_cte AS (
    SELECT departure_airport as airport_id, SUM(flights_count) as flight_counts
    FROM Flights 
    GROUP BY 1
        UNION ALL
    SELECT arrival_airport, SUM(flights_count) 
    FROM Flights
    GROUP BY 1
),
grouped_cte AS (
    SELECT airport_id, SUM(flight_counts) as flights
    FROM joined_airport_cte
    GROUP BY 1
),
ranked_cte AS (
    SELECT airport_id, flights, RANK () OVER (ORDER BY flights DESC) as 'rank' FROM grouped_cte
)

SELECT airport_id FROM ranked_cte WHERE ranked_cte.rank = 1

