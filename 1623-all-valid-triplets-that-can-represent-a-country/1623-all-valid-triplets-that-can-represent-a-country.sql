# Write your MySQL query statement below
# Using Cross JOIN
SELECT a.student_name as member_A, b.student_name as member_B, c.student_name as member_C
FROM SchoolA a, SchoolB b, SchoolC c
WHERE a.student_id!=b.student_id and b.student_id!=c.student_id and a.student_id!=c.student_id
and a.student_name!=b.student_name and b.student_name!=c.student_name and a.student_name!=c.student_name;