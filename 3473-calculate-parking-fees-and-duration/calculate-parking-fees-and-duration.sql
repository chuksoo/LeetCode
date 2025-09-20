# Write your MySQL query statement below
WITH
    total_fee_cte AS (
        SELECT
            car_id
            , SUM(fee_paid) AS total_fee_paid
            , SUM(TIMESTAMPDIFF(MINUTE, entry_time, exit_time) / 60) AS total_time
        FROM ParkingTransactions
        GROUP BY 1
    ),
    most_time_lot_cte AS (
        SELECT
            lot_id
            , car_id
            , SUM(TIMESTAMPDIFF(MINUTE, entry_time, exit_time) / 60) AS time_diff_hrs
            , RANK () OVER(PARTITION BY car_id ORDER BY car_id, SUM(TIMESTAMPDIFF(MINUTE, entry_time, exit_time) / 60) DESC) AS time_rnk
        FROM ParkingTransactions
        GROUP BY 1, 2
    )
    
SELECT 
    a.car_id
    , a.total_fee_paid
    , ROUND((a.total_fee_paid / a.total_time), 2) AS avg_hourly_fee
    , b.lot_id AS most_time_lot
FROM total_fee_cte a
JOIN most_time_lot_cte b
ON a.car_id = b.car_id
WHERE b.time_rnk = 1