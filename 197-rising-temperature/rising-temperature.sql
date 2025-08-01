# Write your MySQL query statement below
WITH temp_data AS (
    SELECT 
    id, recordDate, temperature, 
    LAG(temperature, 1, Null) OVER (ORDER BY recordDate) AS previous_temperature,
    LAG(recordDate, 1, Null) OVER (ORDER BY recordDate) AS previous_recordDate
    FROM Weather
),
diff_info AS (
    SELECT *, 
        (temperature - previous_temperature) AS temp_diff, 
        DATEDIFF(recordDate, previous_recordDate) AS date_diff
    FROM temp_data
)
SELECT id 
FROM diff_info
WHERE temp_diff > 0 AND date_diff = 1
