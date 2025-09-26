USE JOINS_PRACTICE;

-- Create a Table
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name NVARCHAR(55),
    ManagerID INT
);

-- Insert Sample Data
INSERT INTO Employee
(EmployeeID, Name, ManagerID)
VALUES
(1, 'Mike', 3),
(2, 'David', 3),
(3, 'Roger', NULL),
(4, 'Marry',2),
(5, 'Joseph',2),
(7, 'Ben',2);

-- Check the data
SELECT * FROM Employee;

-- Inner Join
SELECT e.Name AS employee, m.Name AS manager
FROM Employee e INNER JOIN Employee m
ON e.ManagerID = m.EmployeeID;

-- Outer Join
SELECT e.Name AS employee, m.Name AS manager
FROM Employee e LEFT JOIN Employee m
ON e.ManagerID = m.EmployeeID;

SELECT e.Name AS employee,
		IFNULL(m.Name, 'Top Manager') AS manager
FROM Employee e LEFT JOIN Employee m
ON e.ManagerID = m.EmployeeID;
-- Clean up (optional)
DROP TABLE Employee;
