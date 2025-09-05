# Write your MySQL query statement below
WITH 
    person_country_code AS (
        SELECT 
            c.name
            , c.country_code
            , p.id
        FROM Country c
        JOIN Person p
        ON c.country_code = SUBSTRING(phone_number, 1, 3)
    ),
    total_calls_cte AS (
        SELECT 
            pc.name
            , pc.country_code
            , SUM(cs.duration) AS total_calls
            , COUNT(name) AS total_calls_sent
        FROM Calls cs
        LEFT JOIN person_country_code pc
        ON cs.caller_id = pc.id
        GROUP BY 1

        UNION ALL

        SELECT 
            pc.name
            , pc.country_code
            , SUM(cs.duration) AS total_recieved
            , COUNT(name) AS total_calls_sent
        FROM Calls cs
        LEFT JOIN person_country_code pc
        ON cs.callee_id = pc.id
        GROUP BY 1
    ),
    country_average_duration AS (
        SELECT
            name
            , SUM(total_calls) AS duration
            , SUM(total_calls_sent) AS calls
            , (SUM(total_calls) / SUM(total_calls_sent)) AS avg_duration
        FROM total_calls_cte
        GROUP BY 1
    )

SELECT name AS country
FROM country_average_duration
WHERE avg_duration > (SELECT AVG(duration) FROM Calls)
