# Write your MySQL query statement below
WITH count_shows_answer AS (
    SELECT 
        question_id, 
        SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END) AS count_shows,
        SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) AS count_answer
    FROM SurveyLog
    GROUP BY 1
),
rates AS (
    SELECT 
        question_id, 
        (count_answer / count_shows) AS answer_rate
    FROM count_shows_answer
),
ranked_rates AS (
    SELECT
        question_id,
        RANK () OVER(ORDER BY answer_rate DESC, question_id ASC) AS rnk
    FROM rates
)

SELECT question_id AS survey_log FROM ranked_rates
WHERE rnk = 1