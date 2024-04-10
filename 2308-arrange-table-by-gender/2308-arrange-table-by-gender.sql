# Write your MySQL query statement below

WITH rank_gender_cte AS (
    SELECT user_id, gender, 
        RANK () OVER (PARTITION BY gender ORDER BY user_id) AS rnk,
        IF(gender='female', 0, IF(gender='other', 1, 2)) AS rnk2
    FROM Genders
)

SELECT user_id, gender
FROM rank_gender_cte AS g
ORDER BY rnk, rnk2
