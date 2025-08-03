# Write your MySQL query statement below
WITH avg_city_prices AS (
    SELECT city, AVG(price) AS city_avg FROM Listings
    GROUP BY 1
),
national_average AS (
    SELECT SUM(price) / COUNT(listing_id) AS home_avg
    FROM Listings
)
SELECT city FROM avg_city_prices
WHERE city_avg > (SELECT home_avg FROM national_average)
ORDER BY 1 ASC
