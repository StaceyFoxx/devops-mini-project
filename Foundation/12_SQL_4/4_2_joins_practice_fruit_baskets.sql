CREATE DATABASE JOINS_PRACTICE;

USE JOINS_PRACTICE;

-- Create table 1
CREATE TABLE fruit_basket_1
(ID INT, Fruit VARCHAR(50));
INSERT INTO fruit_basket_1
(ID, Fruit)
VALUES
(1, 'pear'),
(2, 'apple'),
(3, 'kiwi'),
(4, 'orange'),
(5, 'banana');


-- Create table 2
CREATE TABLE fruit_basket_2
(ID INT, Fruit VARCHAR(50));
INSERT INTO fruit_basket_2
(ID, Fruit)
VALUES
(1, 'pear'),
(2, 'apple'),
(3, 'kiwi'),
(6, 'melon'),
(7, 'peach'),
(8, 'plum');


SELECT *
FROM fruit_basket_1;
SELECT *
FROM fruit_basket_2;


/* INNER JOIN */
SELECT 
    t1.*, t2.*
FROM
    fruit_basket_1 t1
        INNER JOIN
    fruit_basket_2 t2 
		ON 
        t1.ID = t2.ID;


/* INNER JOIN */
SELECT 
    t1.ID AS T1ID,
    t1.Fruit AS T1Fruit,
    t2.ID AS T2ID,
    t2.Fruit AS T2Fruit
FROM
    fruit_basket_1 t1
        INNER JOIN
    fruit_basket_2 t2 
		ON 
        t1.ID = t2.ID;

/* LEFT JOIN */
SELECT 
    t1.*, t2.*
FROM
    fruit_basket_1 t1
        LEFT JOIN
    fruit_basket_2 t2 
		ON 
        t1.ID = t2.ID;

/* RIGHT JOIN */
SELECT 
    t1.*, t2.*
FROM
    fruit_basket_1 t1
        RIGHT JOIN
    fruit_basket_2 t2 
		ON 
        t1.ID = t2.ID;

/* OUTER JOIN */
-- Throws an error !!!!!!!!
SELECT 
	t1.*,t2.*
FROM 
	fruit_basket_1 t1
		FULL OUTER JOIN 
	fruit_basket_2 t2 
		ON 
        t1.ID = t2.ID;

/* LEFT JOIN - WHERE NULL */
SELECT 
    t1.*, t2.*
FROM
    fruit_basket_1 t1
        LEFT JOIN
    fruit_basket_2 t2 ON t1.ID = t2.ID
WHERE
    t2.ID IS NULL;



-- PRACTICE DEMO CONTINUES

/* CROSS JOIN */
SELECT t1.*,t2.*
FROM fruit_basket_1 t1
CROSS JOIN fruit_basket_2 t2;
