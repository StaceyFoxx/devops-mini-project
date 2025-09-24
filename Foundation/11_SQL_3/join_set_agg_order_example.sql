-- SORRY!! You have not been taught JOINS yet! This is for tmrw's class
SELECT  h.name, COUNT(*) AS total_students
FROM students s
JOIN houses h ON s.house = h.House_id
GROUP BY h.name
ORDER BY total_students ASC;