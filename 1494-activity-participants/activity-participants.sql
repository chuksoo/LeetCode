# Write your MySQL query statement below
WITH 
    activity_count AS (
        SELECT
            activity
            , COUNT(activity) AS act_cnt
        FROM Friends
        GROUP BY 1
    )
    
SELECT activity
FROM activity_count
WHERE act_cnt < (SELECT MAX(act_cnt) FROM activity_count)
AND act_cnt > (SELECT MIN(act_cnt) FROM activity_count)

