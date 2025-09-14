# Write your MySQL query statement below
WITH 
    medals_table_cte AS (
        SELECT
            contest_id
            , gold_medal As medals_won
        FROM Contests
        UNION ALL
        SELECT
            contest_id
            , silver_medal As medals_won
        FROM Contests
        UNION ALL
        SELECT
            contest_id
            , bronze_medal As medals_won
        FROM Contests
        ORDER BY 2, 1
    ),
    winning_users_cte AS (
        SELECT 
            DISTINCT a.medals_won AS user_id
        FROM medals_table_cte AS a
        JOIN medals_table_cte AS b
        ON a.medals_won = b.medals_won AND a.contest_id + 1 = b.contest_id
        JOIN medals_table_cte AS c
        ON b.medals_won = c.medals_won AND b.contest_id + 1 = c.contest_id        
        
        UNION

        SELECT
            DISTINCT gold_medal AS user_id
        FROM Contests
        GROUP BY 1
        HAVING COUNT(gold_medal) >= 3
    )

SELECT 
    u.name
    , u.mail
FROM Users AS u
JOIN winning_users_cte AS w
ON u.user_id = w.user_id
