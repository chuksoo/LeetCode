# Write your MySQL query statement below
SELECT 
    date_id
    , make_name
    , COUNT(DISTINCT lead_id) AS unique_leads
    , COUNT(DISTINCT partner_id) AS unique_Partners
FROM DailySales
GROUP BY 1, 2