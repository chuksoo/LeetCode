# Write your MySQL query statement below
WITH
    RECURSIVE tasks_cte AS (
        SELECT
            task_id
            , 1 AS subtask_id
            , subtasks_count
        FROM Tasks

        UNION ALL 
        SELECT 
            task_id
            , subtask_id + 1
            , subtasks_count
        FROM tasks_cte
        WHERE subtask_id < subtasks_count
    )
    
    SELECT 
        task_id
        , subtask_id
    FROM tasks_cte

    EXCEPT 
    
    SELECT * FROM Executed
