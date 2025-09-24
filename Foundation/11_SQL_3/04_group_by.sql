-- Students per house
SELECT House, COUNT(*)
FROM Students
GROUP BY House;

-- Average IQ per house
SELECT House, AVG(IQ)
FROM Students
GROUP BY House;

-- Count by subject
SELECT Class, COUNT(*)
FROM Students
GROUP BY Class;