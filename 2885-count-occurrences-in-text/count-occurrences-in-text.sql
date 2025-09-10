# Write your MySQL query statement below
WITH bull_bear_cte AS (
    SELECT
        SUM(CASE
            WHEN content REGEXP ' bull ' THEN 1
            ELSE 0
        END) AS bull_cnt
        , SUM(CASE
            WHEN content REGEXP ' bear ' THEN 1
            ELSE 0
        END) AS bear_cnt
    FROM Files
)

SELECT 
    'bull' AS word,
    bull_cnt AS count
FROM bull_bear_cte

UNION ALL

SELECT 
    'bear' AS word,
    bear_cnt AS count
FROM bull_bear_cte