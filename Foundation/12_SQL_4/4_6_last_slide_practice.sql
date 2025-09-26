USE parts;
-- Find the name and status of each supplier who supplies project J2
SELECT * FROM supply;
SELECT * FROM project;

SELECT s.SNAME, s.status
FROM supplier s
WHERE S_ID IN ( SELECT s.S_ID FROM supply s WHERE J_ID = 'J2' );

SELECT DISTINCT SNAME, STATUS 
FROM supplier sr INNER JOIN supply s
ON sr.S_ID = s.S_ID
WHERE J_ID = 'J2';

-- Find the name and city of each project supplied by a London-based supplier
SELECT * FROM supplier;
SELECT * FROM supply;
SELECT JNAME, CITY FROM project WHERE J_ID IN 
			(SELECT J_ID FROM supply WHERE S_ID IN 
				(SELECT S_ID FROM supplier WHERE CITY = 'LONDON'));