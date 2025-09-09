# Write your MySQL query statement below
SELECT
    patient_id
    , patient_name
    , conditions
FROM Patients
WHERE REGEXP_LIKE(conditions, '(^|\\s)DIAB1')
-- WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'