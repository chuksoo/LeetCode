# Write your MySQL query statement below
SELECT 
    CASE
        WHEN ROUND(AVG(sessions_per_user), 2) IS NULL THEN 0
        ELSE ROUND(AVG(sessions_per_user), 2) 
    END AS average_sessions_per_user
FROM (
    SELECT user_id, COUNT(DISTINCT session_id) AS sessions_per_user
    FROM Activity
    WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
    GROUP BY 1
) AS avg_sess_user
