# Write your MySQL query statement below
WITH 
    RECURSIVE 
        recursive_year_report AS (
            SELECT 
                product_id
                , period_start
                , period_end
                , YEAR(period_start) AS min_period
                , GREATEST(YEAR(period_start), YEAR(period_end)) AS max_period
                , YEAR(period_start) AS report_year
                , average_daily_sales
            FROM Sales

            UNION ALL

            SELECT 
                product_id
                , period_start
                , period_end
                , min_period
                , max_period
                , report_year + 1
                , average_daily_sales
            FROM recursive_year_report
            WHERE report_year < max_period
        ),
        sales_by_period AS (
            SELECT 
                product_id
                , report_year
                , GREATEST(period_start, CONCAT(report_year, '-01-01')) AS report_period_start
                , LEAST(period_end, CONCAT(report_year, '-12-31')) AS report_period_end
                , average_daily_sales
            FROM recursive_year_report
        ),
        sales_by_day AS (
            SELECT 
                product_id
                , report_year
                , DATEDIFF(report_period_end, report_period_start) + 1 AS sales_day
                , average_daily_sales
            FROM sales_by_period
        )

SELECT 
    s.product_id
    , p.product_name
    , CAST(s.report_year AS CHAR) AS report_year
    , (s.sales_day * s.average_daily_sales) AS total_amount
FROM sales_by_day s
JOIN Product p
ON s.product_id = p.product_id
ORDER BY s.product_id ASC, report_year ASC