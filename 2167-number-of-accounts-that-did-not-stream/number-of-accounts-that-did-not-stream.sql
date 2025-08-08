# Write your MySQL query statement below
WITH subscribed_2021 AS (
    SELECT sub.account_id, sub.start_date, sub.end_date, str.session_id, str.stream_date
    FROM Subscriptions sub
    JOIN Streams str
    ON sub.account_id = str.account_id
    HAVING EXTRACT(YEAR FROM sub.end_date) = '2021'
)

SELECT COUNT(account_id) AS accounts_count
FROM subscribed_2021
WHERE EXTRACT(YEAR FROM stream_date) != '2021'
