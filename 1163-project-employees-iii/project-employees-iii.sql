# Write your MySQL query statement below
SELECT 
    project_id
    , employee_id
FROM (
    SELECT
        p.project_id
        , p.employee_id
        , e.experience_years
        , RANK () OVER(PARTITION BY p.project_id ORDER BY e.experience_years DESC) AS exp_rnk
    FROM Project p
    JOIN Employee e
    ON p.employee_id = e.employee_id
) AS ranked_exp
WHERE exp_rnk = 1
