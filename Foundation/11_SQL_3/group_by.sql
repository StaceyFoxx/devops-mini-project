SELECT Class, COUNT(*) as total_students
FROM students
WHERE Class != "Potions"
GROUP BY Class
HAVING total_students > 1
ORDER BY total_students DESC;