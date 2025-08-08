# Write your MySQL query statement below
SELECT 
    id, 
    CASE 
        WHEN p_id IS NULL THEN "Root"
        WHEN id IS NOT NULL AND id IN (SELECT DISTINCT p_id FROM TREE) THEN "Inner"
        ELSE "Leaf"
    END AS type
FROM Tree