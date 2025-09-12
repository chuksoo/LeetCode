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
    ),
    get_all_tasks_cte AS (
        SELECT 
            task_id
            , subtask_id
        FROM tasks_cte
    )

SELECT * FROM get_all_tasks_cte EXCEPT SELECT * FROM Executed