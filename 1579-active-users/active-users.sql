# Write your MySQL query statement below
WITH 
    ordered_logins_cte AS (
        SELECT 
            id, 
            login_date 
        FROM Logins
        GROUP BY 1, 2
        ORDER BY 1, 2
    ),
    consecutive_four_days_login_cte AS (
        SELECT
            id
            , login_date
            , LAG(login_date, 4) OVER (PARTITION BY id ORDER BY login_date) AS four_login_ago
        FROM ordered_logins_cte 
    )

SELECT DISTINCT 
    cfd_cte.id
    , a.name
FROM consecutive_four_days_login_cte AS cfd_cte
JOIN Accounts AS a 
ON cfd_cte.id = a.id
WHERE DATEDIFF(cfd_cte.login_date, cfd_cte.four_login_ago) = 4
ORDER BY 1