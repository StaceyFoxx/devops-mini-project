USE bakery;

SELECT *
FROM Sweet
WHERE price BETWEEN 0 AND 0.5;


USE harry_potter;

SELECT *
FROM students
WHERE House IN (1, 2);

SELECT Name
FROM students
WHERE IQ IS NOT NULL;
-- WHERE IQ IS NULL;