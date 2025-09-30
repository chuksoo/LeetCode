CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	# Write your MySQL query statement below.
    SELECT
        DISTINCT user_id
    FROM Purchases
    WHERE time_stamp BETWEEN TIMESTAMP(startDate) AND TIMESTAMP(endDate)
    AND amount >= minAmount
    ORDER BY user_id ASC;
END