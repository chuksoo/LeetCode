# Write your MySQL query statement below
WITH highest_february_rating_cte AS (
    SELECT m.movie_id, m.title, AVG(mr.rating) AS avg_rating
    FROM Movies m
    JOIN MovieRating mr
        ON mr.movie_id = m.movie_id
    WHERE mr.created_at LIKE "2020-02%"
    GROUP BY 1
    ORDER BY 3 DESC, 2 ASC
    LIMIT 1
), 
most_rating_user_cte AS (
    SELECT u.name, u.user_id, COUNT(u.user_id)
    FROM Users u
    JOIN MovieRating mr
        ON mr.user_id = u.user_id
    GROUP BY 2
    ORDER BY 3 DESC, 1 ASC
    LIMIT 1
)

SELECT name AS results
FROM most_rating_user_cte 
UNION ALL
SELECT title 
FROM highest_february_rating_cte 
