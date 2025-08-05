# Write your MySQL query statement below
WITH unique_emails AS (
    SELECT id, email, SUBSTRING_INDEX(email, '@', -1) AS domain
    FROM Emails
)

SELECT domain AS email_domain, COUNT(domain) AS count
FROM unique_emails 
WHERE domain REGEXP 'com'
GROUP BY 1
ORDER BY 1