# Write your MySQL query statement below
SELECT 
    u.name, 
    CASE 
        WHEN SUM(r.distance) IS null THEN 0
        ELSE SUM(r.distance) 
    END AS travelled_distance
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY r.user_id
ORDER BY travelled_distance DESC, name ASC