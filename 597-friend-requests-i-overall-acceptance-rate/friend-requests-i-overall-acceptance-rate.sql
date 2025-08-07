# Write your MySQL query statement below
WITH requested AS (
    SELECT DISTINCT sender_id, send_to_id, ROW_NUMBER () OVER(ORDER BY sender_id ASC) as request_cnt
    FROM FriendRequest
    GROUP BY 1, 2
),
unique_accepted AS (
    SELECT DISTINCT requester_id, accepter_id, ROW_NUMBER () OVER(ORDER BY requester_id ASC) as row_cnt
    FROM RequestAccepted
    GROUP BY 1, 2
)

SELECT (
    CASE 
        WHEN ((SELECT MAX(row_cnt) FROM unique_accepted) / (SELECT MAX(request_cnt) FROM requested)) IS NULL THEN 0.00
        ELSE ROUND((SELECT MAX(row_cnt) FROM unique_accepted) / (SELECT MAX(request_cnt) FROM requested), 2)
    END 
) AS accept_rate

