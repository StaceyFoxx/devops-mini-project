--Definitions
--WHERE: Filters individual rows before grouping occurs.
--HAVING: Filters groups after grouping and aggregation occurs.

--Difference
--WHERE operates on raw data rows, HAVING operates on grouped results.
--You use WHERE to exclude rows from groups,
--  HAVING to exclude entire groups from results.

-- WHERE: Filter students before counting
SELECT House, COUNT(*)
FROM Students
WHERE IQ > 7
GROUP BY House;

-- HAVING: Filter groups after counting
SELECT House, COUNT(*)
FROM Students
GROUP BY House
HAVING COUNT(*) > 2;

-- Both together: Filter rows first, then filter groups
SELECT House, AVG(IQ)
FROM Students
WHERE Quidditch = TRUE
GROUP BY House
HAVING AVG(IQ) > 7;


-- Can you explain to me what's happening below?
SELECT Class, COUNT(*) as total_students
FROM students
WHERE Class != "Potions"
GROUP BY Class
HAVING total_students > 1;