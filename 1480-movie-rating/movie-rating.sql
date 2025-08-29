# Write your MySQL query statement below
WITH rated_user AS (
    SELECT 
        DISTINCT u.name
        , mr.user_id
        , COUNT(mr.user_id) AS movies_rated
        , ROW_NUMBER() OVER(ORDER BY COUNT(mr.user_id) DESC, u.name ASC) AS row_u
    FROM MovieRating mr 
    JOIN Users u
    ON u.user_id = mr.user_id
    GROUP BY 2
),
rated_movies AS (
    SELECT 
        DISTINCT m.title
        , mr.movie_id
        , AVG(mr.rating) AS avg_rating
        , ROW_NUMBER() OVER(ORDER BY AVG(mr.rating) DESC, m.title ASC) AS row_m
    FROM MovieRating mr 
    JOIN Movies m 
    ON m.movie_id = mr.movie_id 
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY 2
)

SELECT 
    name AS results
FROM rated_user
WHERE row_u = 1
UNION ALL
SELECT
    title AS results
FROM rated_movies
WHERE row_m = 1