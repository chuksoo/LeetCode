# Write your MySQL query statement below
SELECT
    user_id
    , last_stamp
FROM (
    SELECT 
        user_id
        , time_stamp AS last_stamp
        , RANK () OVER(PARTITION BY user_Id ORDER BY time_stamp DESC) AS rnk
    FROM Logins 
    WHERE DATE_FORMAT(time_stamp, '%Y') = '2020'
) AS ranked_timestamp
WHERE rnk = 1


