# Write your MySQL query statement below
WITH 
    logged_row_numbers AS (
        SELECT
            log_id
            , ROW_NUMBER() OVER (ORDER BY log_id ASC) AS row_num
        FROM Logs
    ),
    row_difference AS (
        SELECT 
            log_id
            , row_num
            , (log_id - row_num) AS row_diff
        FROM logged_row_numbers
    )

SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id 
FROM row_difference
GROUP BY row_diff
ORDER BY 1