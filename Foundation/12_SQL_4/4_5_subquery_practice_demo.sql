USE customers;
-- What is the name of the customer with phone number '555-3344'?
SELECT c.first_name, c.last_name 
FROM customer c
WHERE c.customer_id IN 
	(SELECT customer_id FROM phone_number WHERE phone_number = '555-3344');