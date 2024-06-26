# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.customer_id) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS null
GROUP BY 1
ORDER BY 2 DESC