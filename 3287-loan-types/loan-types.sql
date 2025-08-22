# Write your MySQL query statement below
WITH distint_loans AS (
    SELECT 
        DISTINCT user_id
    FROM Loans
    WHERE loan_type = 'Mortgage' 
    UNION ALL
    SELECT  
        DISTINCT user_id
    FROM Loans
    WHERE loan_type = 'Refinance'
), 
loan_count AS (
    SELECT user_Id, COUNT(user_id) AS counts
    FROM distint_loans
    GROUP BY 1
)

SELECT 
    user_id 
FROM loan_count
WHERE counts = 2
ORDER BY 1 ASC


