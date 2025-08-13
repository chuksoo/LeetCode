# Write your MySQL query statement below
-- Step 1: Find each player's first login date (install date)
WITH player_install_dates AS (
    SELECT 
        player_id,
        MIN(event_date) as install_dt
    FROM Activity
    GROUP BY player_id
),

-- Step 2: Find all players who logged in the day after their install date
next_day_logins AS (
    SELECT 
        DISTINCT player_id,
        event_date AS next_day_login_date
    FROM Activity
),

-- Step 3: Check which players actually returned the day after install
retention_check AS (
    SELECT
        p.player_id,
        p.install_dt,
        n.next_day_login_date,
        CASE
            WHEN n.next_day_login_date = DATE_ADD(p.install_dt, INTERVAL 1 DAY) THEN 1
            ELSE 0
        END AS returned_next_day
    FROM player_install_dates p
    LEFT JOIN next_day_logins n
    ON p.player_id = n.player_id
    AND n.next_day_login_date = DATE_ADD(p.install_dt, INTERVAL 1 DAY)
),

-- Step 4: Count installs and returnees per install date
install_summary AS (
    SELECT
        install_dt,
        COUNT(*) AS total_installs,
        SUM(returned_next_day) AS players_returned_next_day
    FROM retention_check
    GROUP BY install_dt
)

-- Step 5: Calculate final retention rate
SELECT 
    install_dt,
    total_installs AS installs,
    ROUND(players_returned_next_day / total_installs, 2) AS Day1_retention
FROM install_summary
ORDER BY install_dt


