# Write your MySQL query statement below
WITH queue_fit_cte AS (
    SELECT
        turn
        , person_id
        , person_name
        , weight
        , SUM(weight) OVER(
            ORDER BY turn ASC
        ) AS total_weight
        , ROW_NUMBER() OVER(ORDER BY turn ASC) AS row_num
    FROM Queue
),
get_last_person_cte AS (
    SELECT
        turn
        , person_id
        , person_name
        , weight
        , total_weight
        , row_num
    FROM queue_fit_cte
    WHERE total_weight <= 1000
)

SELECT 
    person_name 
FROM get_last_person_cte
WHERE row_num = (
    SELECT MAX(row_num)
    FROM get_last_person_cte
)