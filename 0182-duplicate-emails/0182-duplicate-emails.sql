# Write your MySQL query statement below
WITH email_counts AS (
    SELECT id, email, COUNT(email) as count_email
    FROM Person 
    GROUP BY 2
)
SELECT email AS Email
FROM email_counts
WHERE count_email > 1