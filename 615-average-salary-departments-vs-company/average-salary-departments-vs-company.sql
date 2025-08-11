# Write your MySQL query statement below
WITH all_data AS (
    SELECT s.id, e.employee_id, e.department_id, s.amount, s.pay_date
    FROM Employee e
    JOIN Salary s
    ON e.employee_id = s.employee_id
),
company_average_sal AS (
    SELECT 
        DATE_FORMAT(pay_date, '%Y-%m') AS pay_month,
        AVG(amount) AS coy_avg_sal
    FROM Salary
    GROUP BY 1
    ORDER BY 1
), 
dept_monthly_avg AS (
    SELECT 
        DISTINCT department_id, 
        DATE_FORMAT(pay_date, '%Y-%m') AS pay_month,
        AVG(amount) OVER (
            PARTITION BY department_id, DATE_FORMAT(pay_date, '%Y-%m')
        ) AS avg_monthly_sal
    FROM all_data
    ORDER BY DATE_FORMAT(pay_date, '%Y-%m') ASC
)

SELECT 
    d.pay_month, 
    d.department_id,  
    CASE    
        WHEN d.avg_monthly_sal > c.coy_avg_sal THEN 'higher'
        WHEN d.avg_monthly_sal < c.coy_avg_sal THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM dept_monthly_avg d
JOIN company_average_sal c
ON d.pay_month = c.pay_month




