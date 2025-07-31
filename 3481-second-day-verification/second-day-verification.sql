# Write your MySQL query statement below 
SELECT user_id 
FROM (
    SELECT 
        e.user_id, 
        t.signup_action, 
        e.signup_date, 
        t.action_date, 
        (EXTRACT(DAY FROM t.action_date) - EXTRACT(DAY FROM e.signup_date)) AS date_diff,
        (EXTRACT(MONTH FROM t.action_date) - EXTRACT(MONTH FROM e.signup_date)) AS month_diff
    FROM emails e
    LEFT JOIN texts t
    ON e.email_id = t.email_id
) as verification_table
WHERE signup_action = 'Verified' AND date_diff = 1 AND month_diff = 0
ORDER BY 1




