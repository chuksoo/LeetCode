# Write your MySQL query statement below
WITH
    sessions_with_yes As (
        SELECT session_id
        FROM (
            SELECT 
                p.session_id, p.customer_id, p.start_time, p.end_time
                , CASE
                    WHEN a.timestamp BETWEEN p.start_time AND p.end_time THEN 'Yes'
                    ELSE 'No'
                END AS has_ads
            FROM Playback p
            JOIN Ads a
            ON p.customer_id = a.customer_id
        ) As playback_ads
        WHERE has_ads = 'Yes'
    )

SELECT DISTINCT session_id
FROM Playback
WHERE session_id NOT IN (SELECT session_id FROM sessions_with_yes)

