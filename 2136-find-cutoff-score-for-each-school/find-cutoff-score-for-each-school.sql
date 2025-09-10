# Write your MySQL query statement below
WITH get_capacity_score_cte AS (
    SELECT
        s.school_id
        , CASE
            WHEN s.capacity >= e.student_count THEN e.score
            ELSE NULL
        END AS new_score
    FROM Schools s
    CROSS JOIN Exam e
    ORDER BY 1
),
rank_capacity_score_cte AS (
    SELECT
        school_id
        , new_score
        , RANK () OVER (PARTITION BY school_id ORDER BY new_score ASC) AS score_rnk
    FROM get_capacity_score_cte
    WHERE new_score IS NOT NULL
), 
school_minimum_cte AS (
    SELECT 
        DISTINCT school_id
        , new_score AS score
    FROM rank_capacity_score_cte
    WHERE score_rnk = 1
)

SELECT 
    s.school_id
    , IFNULL(sm.score, -1) AS score
FROM Schools s
LEFT JOIN school_minimum_cte sm
ON s.school_id = sm.school_id

