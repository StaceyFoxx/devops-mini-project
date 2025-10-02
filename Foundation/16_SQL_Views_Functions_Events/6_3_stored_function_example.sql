USE bank;
SELECT * FROM accounts;
-- write a stored function that accepts customer account’s balance as a parameter and is assessing whether he/she is eligible for a credit
-- ----------------------------------------------------------------
-- |    balance > 100     | 100 >= balance >= 50  |  balance < 50 |
-- |----------------------|-----------------------|---------------|
-- |         YES          |          MAYBE        |       NO      |
-- ----------------------------------------------------------------
DELIMITER //
CREATE FUNCTION is_eligible(balance INT)
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
	DECLARE customer_status VARCHAR(10);
    IF balance > 100 THEN
		SET customer_status = 'YES';
	ELSEIF (balance >= 50 AND balance <= 100) THEN
		SET customer_status = 'MAYBE';
	ELSEIF balance < 50 THEN
		SET customer_status = 'NO';
	END IF;
    RETURN customer_status;
END//

DELIMITER ;

-- use function in SELECT

SELECT account_holder_name, 
		account_holder_surname, 
        balance, is_eligible(balance) as 'credit allowed'
FROM accounts;