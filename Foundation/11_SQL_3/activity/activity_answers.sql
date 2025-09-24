
--Find all savoury items that have either pork or beef filling.

SELECT
    sav.item_name
FROM
    savoury sav
WHERE
    sav.main_ingredient = 'pork'
        OR sav.main_ingredient = 'beef';


--Find all sweet items that cost 50 cents or cheaper.

SELECT
    sw.item_name, sw.price
FROM
    sweet sw
WHERE
    sw.price <= 0.5;


--Find all sweet items and their price, except for cannoli.


SELECT
    sw.item_name, sw.price
FROM
    sweet sw
WHERE
    sw.item_name <> 'cannoli';



--Find all sweet items that start with the letter ‘c’



SELECT
    sw.item_name, sw.price
FROM
    sweet sw
WHERE
    sw.item_name like 'c%';


--Find all savoury items that cost more than £1, but less than £3
--NB: note to students that operator BETWEEN includes the range values, so if we want to exclude them, we need to provide numbers that are just before or after the range values.


SELECT
    sav.item_name, sav.price
FROM
    savoury sav
WHERE
    sav.price between 1.01 and 2.99;


-- NOTE TO STUDENTS THE ACTIVITY ANSWERS FROM BELOW ARE FOR THE LAST AGGREGATION QUESTIONS


use shop;

-- check how our table looks in order to proceed with queries
select * from SALES1;

-- Find all sales records (and all columns) that took place in the London store, not in December,
-- but sales concluded by Bill or Frank for the amount higher than Â£50.
SELECT
    *
FROM
    SALES1
WHERE
    STORE = 'LONDON' AND MONTH <> 'dec'
        AND SalesAmount > 50.00
        AND (SalesPerson = 'BILL'
        OR SalesPerson = 'FRANK');

-- Find out how many sales took place each week (in no particular order)
SELECT
    WEEK, COUNT(*)
FROM
    SALES1
GROUP BY WEEK;


-- Find out how many sales took place each week (and present data by week in descending and then in ascending order)
SELECT
    WEEK, COUNT(week) AS 'NUM_sales'
FROM
    SALES1
GROUP BY WEEK
ORDER BY WEEK;
-- ORDER BY WEEK DESC;


