USE shop;

CREATE TABLE SALES2_Example AS 
SELECT  
	UPPER(store) as store,
    week,
    day,
    SalesPerson,
    SalesAmount,
    Month,
    'ENGLAND' as country
FROM SALES1;
SELECT * FROM SALES2_EXAMPLE;

CREATE TABLE SALES2_Example
(
-- define columsn and contraints
);

INSERT INTO SALES2_Example
-- LONDON	2	Monday	Frank	56.25	May	ENGLAND
-- LONDON	5	Tuesday	Frank	74.32	Sep	ENGLAND
-- LONDON	5	Monday	Bill	98.42	Sep	ENGLAND
-- LONDON	5	Saturday	Bill	73.90	Dec	ENGLAND
-- LONDON	1	Tuesday	Josie	44.27	Sep	ENGLAND
-- DUSSELDORF	4	Monday	Manfred	77.00	Jul	ENGLAND
-- DUSSELDORF	3	Tuesday	Inga	9.99	Jun	ENGLAND
-- DUSSELDORF	4	Wednesday	Manfred	86.81	Jul	ENGLAND
-- LONDON	6	Friday	Josie	74.02	Oct	ENGLAND
-- DUSSELDORF	1	Saturday	Manfred	43.11	Apr	ENGLAND

