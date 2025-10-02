use practice;
-- Create a simple greetings stored procedure
DELIMITER //
CREATE PROCEDURE greetings(greeting_word VARCHAR(20), first_name VARCHAR(20))
BEGIN
	DECLARE full_greeting VARCHAR(40);
    SET full_greeting = CONCAT(greeting_word, ' ', first_name);
    SELECT full_greeting;
END//
DELIMITER ;
CALL greetings('Hello', 'Sara');
CALL Greetings('Bonjour,', 'Dave');
CALL Greetings('Hola,', 'Dora');

-- Write a stored procedure that accepts parameters and inserts values into a table in the bakery database
USE bakery;
SELECT * FROM SWEET;
DELIMITER //
CREATE PROCEDURE Insert_sweet(
				IN id INT, 
				IN sweetItem VARCHAR(100),
				IN price FLOAT)
BEGIN

INSERT INTO sweet(id,item_name, price)
VALUES (id,sweetItem, price);
END//
DELIMITER ;

CALL Insert_sweet (11, 'cherry_cake', 5);
CALL insert_sweet(12, 'ice cream', 0.5);

select * from sweet;

-- optional clean-up 
DROP PROCEDURE Insert_sweet;