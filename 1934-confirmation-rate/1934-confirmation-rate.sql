# Write your MySQL query statement below
WITH timeout_cte AS (
    SELECT user_id, COUNT(action) as action
    FROM Confirmations 
    WHERE action = 'timeout'
    GROUP BY 1
),
confirmed_cte AS (
    SELECT user_id, COUNT(action) as action
    FROM Confirmations 
    WHERE action = 'confirmed'
    GROUP BY 1
),
grouped_cte AS (
    SELECT s.user_id, 
        CASE 
            WHEN t.action IS null THEN 0
            ELSE t.action 
        END AS timeout_counts, 
        CASE 
            WHEN c.action IS null THEN 0
            ELSE c.action
        END AS confirmed_counts
    FROM Signups s
    LEFT JOIN timeout_cte t
        ON s.user_id = t.user_id
    LEFT JOIN confirmed_cte c
        ON s.user_id = c.user_id
    ORDER BY 1 ASC
)
SELECT g.user_id, 
    CASE 
        WHEN g.timeout_counts = 0 AND g.confirmed_counts = 0 THEN 0.00
        ELSE ROUND((g.confirmed_counts / (g.timeout_counts + g.confirmed_counts)), 2)
    END AS confirmation_rate
FROM grouped_cte g

