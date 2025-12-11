# Write your MySQL query statement below
WITH
    candidate_info_cte AS (
        SELECT
            c.candidate_id
            , p.project_id
            , COUNT(c.skill) AS candidate_skill_cnt
            , 100 + SUM(CASE
                WHEN c.proficiency > p.importance THEN 10
                WHEN c.proficiency < p.importance THEN -5
                ELSE 0
            END) AS score
        FROM Projects AS p
        JOIN Candidates AS c
        ON p.skill = c.skill
        GROUP BY 1, 2
        ORDER BY 1
    ),
    project_info_cte AS (
        SELECT
            project_id
            , COUNT(skill) AS project_skill_cnt
        FROM Projects
        GROUP BY 1
    ),
    ranked_candidate_score_cte AS (
        SELECT
            ci_cte.project_id
            , ci_cte.candidate_id
            , ci_cte.score
            , RANK () OVER (
                PARTITION BY ci_cte.project_id ORDER BY ci_cte.score DESC, ci_cte.candidate_id ASC
            ) AS score_rnk
        FROM candidate_info_cte AS ci_cte
        JOIN project_info_cte AS pi_cte
        ON ci_cte.candidate_skill_cnt = pi_cte.project_skill_cnt
        AND ci_cte.project_id = pi_cte.project_id
    )

SELECT 
    project_id
    , candidate_id
    , score
FROM ranked_candidate_score_cte
WHERE score_rnk = 1


