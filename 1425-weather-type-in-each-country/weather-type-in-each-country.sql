# Write your MySQL query statement below
WITH avg_weather_cte AS (
    SELECT 
        country_id
        , AVG(weather_state) AS avg_weather
    FROM Weather
    WHERE day BETWEEN "2019-11-01" AND "2019-11-30"
    GROUP BY 1
)

SELECT 
    c.country_name
    , CASE
        WHEN a.avg_weather <= 15 THEN 'Cold'
        WHEN a.avg_weather >= 25 THEN 'Hot'
        ELSE 'Warm'
    END AS weather_type
FROM Countries c
JOIN avg_weather_cte a
ON c.country_id = a.country_id
