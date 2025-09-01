# Write your MySQL query statement below
WITH
    contact_count AS (
        SELECT
            user_id
            , COUNT(user_id) AS contacts_cnt
        FROM Contacts
        GROUP BY 1
    ),
    trusted_contact_cte AS (
        SELECT 
            c.user_id
            , COUNT(c.user_id) AS trusted_contacts_cnt
        FROM Contacts c
        WHERE c.contact_name IN (
            SELECT customer_name FROM Customers
        )
        GROUP BY 1 
    )

SELECT inv.invoice_id
    , cust.customer_name
    , inv.price
    , COALESCE(cc.contacts_cnt, 0) AS contacts_cnt
    , COALESCE(tc.trusted_contacts_cnt, 0) AS trusted_contacts_cnt
FROM Invoices inv
JOIN Customers cust
    ON inv.user_id = cust.customer_id
LEFT JOIN contact_count cc
    ON cc.user_id = inv.user_id
LEFT JOIN trusted_contact_cte tc
    ON tc.user_id  = inv.user_id
ORDER BY 1 ASC