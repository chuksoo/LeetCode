# Write your MySQL query statement below
SELECT id, movie, description, rating
FROM Cinema
WHERE MOD(id, 2) <> 0 AND description != 'boring' ## MOD() returns remainder of a number divided by another number
ORDER BY -rating 