/* Write your T-SQL query statement below */
WITH DepartmentSalaries AS (
    SELECT
        departmentId,
        [name],
        salary,
        DENSE_RANK() OVER (
            PARTITION BY departmentId 
            ORDER BY salary DESC
            ) AS salary_rank
    FROM Employee
)

SELECT
    d.name AS Department,
    ds.name AS Employee,
    ds.salary AS Salary
FROM DepartmentSalaries ds
INNER JOIN Department d
    ON d.id = ds.departmentId
WHERE ds.salary_rank <= 3;

-- SELECT * FROM DepartmentSalaries