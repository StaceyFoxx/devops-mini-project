USE customers;
SELECT * FROM customer;
SELECT * FROM email_address;
INSERT INTO customer 
(customer_id, first_name, last_name) 
VALUES 
(3, 'Poly', 'Marks'),
(4, 'Jenny', 'King');
INSERT INTO email_address 
(email_address_id, customer_id, email_address)
 VALUES 
 (3, NULL, 'someone@mail.com');
 
 SELECT * FROM customer;
 SELECT * FROM email_address;
 
 
 -- INNER JOIN
SELECT c.first_name, c.last_name, e.email_address
FROM
customer c INNER JOIN email_address e
ON c.customer_id = e.customer_id;

 -- LEFT JOIN
SELECT c.first_name, c.last_name, e.email_address
FROM
customer c LEFT JOIN email_address e
ON c.customer_id = e.customer_id;

 -- RIGHT JOIN
SELECT c.first_name, c.last_name, e.email_address
FROM
customer c RIGHT JOIN email_address e
ON c.customer_id = e.customer_id;


 -- FULL JOIN
SELECT c.first_name, c.last_name, e.email_address
FROM customer c LEFT JOIN email_address e ON c.customer_id = e.customer_id
UNION
SELECT c.first_name, c.last_name, e.email_address 
FROM customer c RIGHT JOIN email_address e ON c.customer_id = e.customer_id;

-- Natural JOIN
SELECT c.first_name, c.last_name, e.email_address
FROM
customer c NATURAL JOIN email_address e;


 -- clean-up
DELETE FROM customer WHERE (customer_id = '3');
DELETE FROM customer WHERE (customer_id = '4');
DELETE FROM email_address WHERE (email_address_id = '3');
 