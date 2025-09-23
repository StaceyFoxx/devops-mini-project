USE Parts;

-- Using the table 'parts', return all unique part names.
-- What happens if we want to return all unique parts and their id number? Why?

-- get unique part names
SELECT distinct PNAME
FROM PART;

-- get unique part names and id numbers
SELECT distinct P_ID, PNAME
FROM PART;