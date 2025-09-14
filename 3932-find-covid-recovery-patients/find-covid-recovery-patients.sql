# Write your MySQL query statement below
WITH
    pos_patient_with_covid_cte AS (
        SELECT
            patient_id
            , MIN(test_date) AS test_date
            , result
        FROM covid_tests
        WHERE result = 'Positive'
        GROUP BY patient_id
        ORDER BY 2, 3
    ),
    neg_patient_with_covid_cte AS (
        SELECT
            c.patient_id
            , MIN(c.test_date) AS test_date
            , c.result
        FROM covid_tests AS c
        JOIN pos_patient_with_covid_cte AS pos
        ON c.patient_id = pos.patient_id
        WHERE c.result = 'Negative' AND c.test_date > pos.test_date
        GROUP BY patient_id
        ORDER BY 2, 3
    )    

SELECT 
    pos.patient_id
    , p.patient_name
    , p.age
    , DATEDIFF(neg.test_date, pos.test_date) AS recovery_time
FROM pos_patient_with_covid_cte AS pos
JOIN neg_patient_with_covid_cte AS neg
ON pos.patient_id = neg.patient_id
JOIN patients AS p
ON p.patient_id = pos.patient_id
ORDER BY 4 ASC, 2 ASC