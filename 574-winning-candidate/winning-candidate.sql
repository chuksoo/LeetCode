# Write your MySQL query statement below
WITH vote_casted AS (
    SELECT candidateId, COUNT(*) AS votes
    FROM Vote
    GROUP BY 1
    ORDER BY 1
),
ranked_votes AS (
    SELECT c.name, v.votes, RANK () OVER(ORDER BY v.votes DESC) as ranked
    FROM Candidate c
    JOIN vote_casted v
    ON c.id = v.candidateId
)

SELECT name FROM ranked_votes WHERE ranked = 1