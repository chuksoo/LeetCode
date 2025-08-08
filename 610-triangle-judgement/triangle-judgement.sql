# Write your MySQL query statement below
-- Sum the two shorter line segment
-- If the sum of the two shorter side is greater than the longest side, a triangle can be formed
SELECT x, y, z, 
    IF(x + y > z AND y + z > x AND z + x > y, 'Yes', 'No') AS triangle
FROM Triangle