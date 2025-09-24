-- dont forget BETWEEN, LIKE, IN, IS (NULL)

SELECT * 
FROM students
WHERE IQ > 7;

SELECT *
FROM students
WHERE House IN (1, 2);

SELECT Name
FROM students
WHERE IQ IS NOT NULL;
-- WHERE IQ IS NULL;