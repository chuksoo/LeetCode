# Write your MySQL query statement below
WITH clicked_ads AS (
    SELECT ad_id, user_id, 
        CASE 
            WHEN COUNT(ad_id) IS NULL THEN 0
            ELSE COUNT(ad_id) 
        END AS clicked
    FROM Ads
    WHERE action = 'Clicked'
    GROUP BY 1
    ORDER BY 1
),
viewed_ads AS (
    SELECT 
        ad_id, user_id, 
        CASE 
            WHEN COUNT(ad_id) IS NULL THEN 0
            ELSE COUNT(ad_id) 
        END AS viewed
    FROM Ads
    WHERE action = 'Viewed'
    GROUP BY 1
    ORDER BY 1
),
unique_ads AS (
    SELECT ad_id, COUNT(*) AS ads_count
    FROM Ads
    GROUP BY 1
),
stats AS (
    SELECT 
        u.ad_id, 
        CASE 
            WHEN c.clicked IS NULL THEN 0
            ELSE c.clicked
        END AS total_clicks, 
        CASE 
            WHEN v.viewed IS NULL THEN 0
            ELSE v.viewed
        END AS total_views
    FROM unique_ads u 
    LEFT JOIN clicked_ads c ON u.ad_id = c.ad_id
    LEFT JOIN viewed_ads v ON u.ad_id = v.ad_id
)

SELECT 
    ad_id,
    CASE 
        WHEN ROUND((total_clicks / (total_clicks + total_views)) * 100, 2) IS NULL THEN 0.00
        ELSE ROUND((total_clicks / (total_clicks + total_views)) * 100, 2) 
    END AS ctr
FROM stats
ORDER BY ctr DESC, ad_id ASC
