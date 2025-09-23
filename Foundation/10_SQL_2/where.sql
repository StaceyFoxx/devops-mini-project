-- Refer to the table 'projects' and return all projects that are run in London

SELECT p.*
FROM PROJECT p
WHERE p.city = 'LONDON';