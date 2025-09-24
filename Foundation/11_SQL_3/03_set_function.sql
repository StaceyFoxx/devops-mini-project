
--IMPORTANT POINT: Set Functions = Aggregate Functions
-- Both describe the same SQL functions that summarise data
--   across multiple rows into a single result.


-- Sum of all IQ scores
SELECT SUM(IQ) FROM Students;

-- Sum of IQ per house
SELECT House, SUM(IQ)
FROM Students
GROUP BY House;

-- Average IQ of all students
SELECT AVG(IQ) FROM Students;
