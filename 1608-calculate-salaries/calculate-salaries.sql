# Write your MySQL query statement below
WITH 
    company_salary_rank AS (
        SELECT
            company_id
            , employee_id
            , salary
            , DENSE_RANK () OVER(PARTITION BY company_id ORDER BY salary DESC) AS salary_rnk
        FROM Salaries
    ),
    company_max_salary_cte AS (
        SELECT
            company_id
            , salary AS max_salary
        FROM company_salary_rank
        WHERE salary_rnk = 1
    ),
    company_tax_rate AS (
        SELECT
            company_id
            , max_salary
            , CASE
                WHEN max_salary < 1000 THEN 0.0
                WHEN (max_salary >= 1000 AND max_salary <= 10000) THEN 0.24
                WHEN max_salary > 10000 THEN 0.49
            END AS salary_rate
        FROM company_max_salary_cte
    )

SELECT
    s.company_id
    , s.employee_id
    , s.employee_name
    , ROUND((s.salary - s.salary * ctr.salary_rate), 0) AS salary
FROM Salaries AS s
JOIN company_tax_rate AS ctr
ON s.company_id = ctr.company_id
