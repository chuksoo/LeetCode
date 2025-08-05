# Write your MySQL query statement below
WITH employee_positions AS (
    SELECT 
        id, 
        company, 
        salary,
        ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary ASC, id ASC) AS row_position,
        COUNT(*) OVER (PARTITION BY company) AS company_size
    FROM Employee
),
median_calculations AS (
    SELECT
        id,
        company, 
        salary,
        row_position,
        company_size,
        CASE
            WHEN company_size % 2 = 1 THEN (company_size + 1) / 2 -- Odd: single median
            ELSE company_size / 2 -- Even: first median position 
        END AS median_pos1,
        CASE
            WHEN company_size % 2 = 1 THEN (company_size + 1) / 2 -- Odd: single median
            ELSE (company_size / 2) + 1 -- Even: second median position 
        END AS median_pos2
    FROM employee_positions
)


SELECT id, company, salary FROM median_calculations
WHERE row_position = median_pos1 OR row_position = median_pos2