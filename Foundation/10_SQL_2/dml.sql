-- update a table using the alter table command to turn a column into a foreign key
ALTER TABLE email_address
ADD CONSTRAINT
FK_email_address_customer
FOREIGN KEY
(email_address_customer_id)
REFERENCES
customer
(customer_id);

ALTER TABLE phone_number
ADD CONSTRAINT
FK_phone_number_customer
FOREIGN KEY
(phone_number_customer_id)
REFERENCES
customer
(customer_id);

-- delete a table and any data it holds
DROP TABLE orders;

-- delete rows targeted by where clause
DELETE FROM orders
WHER order_id = 1