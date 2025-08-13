# Write your MySQL query statement below
WITH first_time_login AS (
    SELECT 
        user_id,
        MIN(activity_date) AS first_login_date
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY 1
),
login_within_date AS (
    SELECT 
        user_id,
        first_login_date 
    FROM first_time_login
    WHERE first_login_date BETWEEN DATE_ADD('2019-06-30', INTERVAL -90 DAY) AND '2019-06-30'
)

SELECT 
    first_login_date AS login_date,
    COUNT(first_login_date) AS user_count
FROM login_within_date
GROUP BY 1
