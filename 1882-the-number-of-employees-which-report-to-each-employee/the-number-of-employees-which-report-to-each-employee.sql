# Write your MySQL query statement below
WITH report_count_age_cte AS (
    SELECT
        reports_to AS employee_id
        , COUNT(reports_to) AS reports_count
        , ROUND(AVG(age), 0) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY 1
)

SELECT 
    e.employee_id
    , e.name
    , r.reports_count
    , r.average_age
FROM Employees e
JOIN report_count_age_cte r
ON e.employee_id = r.employee_id
ORDER BY 1


