# Write your MySQL query statement below
WITH conversion_rate_cte AS (
    SELECT m.name,
        m.member_id, 
        COUNT(p.visit_id) as purchase_count,
        COUNT(v.member_id) as visit_count,
        ROUND(((COUNT(p.visit_id)*100) / COUNT(v.member_id)), 2) AS conversion_rate
    FROM Members m
    LEFT JOIN Visits v ON m.member_id = v.member_id
    LEFT JOIN Purchases p ON v.visit_id = p.visit_id
    GROUP BY 2
)

SELECT member_id, 
       name,
       (CASE
            WHEN conversion_rate >= 80 THEN 'Diamond'
            WHEN conversion_rate >= 50 THEN 'Gold'
            WHEN conversion_rate < 50 AND visit_count > 0 THEN 'Silver'
            ELSE 'Bronze'
        END) AS category
FROM conversion_rate_cte;