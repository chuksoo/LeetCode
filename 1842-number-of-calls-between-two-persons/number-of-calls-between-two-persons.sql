# Write your MySQL query statement below
WITH
    calls_cte AS (
        SELECT 
            from_id
            , to_id
            , duration
        FROM Calls
        WHERE from_id < to_id

        UNION ALL
        SELECT
            to_id
            , from_id
            , duration
        FROM Calls
        WHERE from_id > to_id
    )

SELECT 
    DISTINCT from_id AS person1
    , to_id AS person2
    , COUNT(duration) OVER(PARTITION BY from_id, to_id) AS call_count
    , SUM(duration) OVER(PARTITION BY from_id, to_id) AS total_duration
FROM calls_cte
