# Write your MySQL query statement below
SELECT 
    tweet_id
FROM Tweets
WHERE LENGTH(content) > 140
OR content LIKE '%@%@%@%@%'
OR content LIKE '%#%#%#%#%'
ORDER BY 1 ASC