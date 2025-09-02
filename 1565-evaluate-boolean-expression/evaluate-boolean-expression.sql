# Write your MySQL query statement below
WITH
    operand_value_cte AS (
        SELECT 
            e.left_operand
            , e.operator
            , e.right_operand
            , CASE
                WHEN e.operator = '>' THEN v1.value > v2.value 
                WHEN e.operator = '<' THEN v1.value < v2.value 
                WHEN e.operator = '=' THEN v1.value = v2.value 
                ELSE 'false'
            END AS value_num
        FROM Expressions e
        LEFT JOIN Variables v1
        ON e.left_operand = v1.name 
        LEFT JOIN Variables v2
        ON e.right_operand = v2.name
    )

SELECT 
    left_operand
    , operator
    , right_operand
    , CASE
        WHEN value_num = "0" THEN 'false'
        ELSE 'true'
    END AS value
FROM operand_value_cte 
