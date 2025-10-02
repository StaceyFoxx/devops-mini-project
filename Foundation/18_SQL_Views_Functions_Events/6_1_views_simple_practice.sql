USE shop;
SELECT * FROM sales1;

-- Create a simple view that contains the SalesPerson and SalesAmount

CREATE VIEW vw_sales_men
AS
SELECT SalesPerson, SalesAmount
FROM sales1;

SELECT * From vw_sales_men;

-- You can query the view in exactly the same way as a table
SELECT SalesPerson, Max(SalesAmount) as max_amount
From vw_sales_men
GROUP BY SalesPerson
HAVING max_amount > 80;

-- let's create a view that contains only London related data
CREATE VIEW vw_London_access
AS
SELECT * FROM sales1 WHERE Store = 'London';

-- Create a nested view based on vw_sales_men
CREATE VIEW vw_totals
As
SELECT SalesPerson, SUM(SalesAmount) as total
FROM vw_sales_men
GROUP BY SalesPerson;
SELECT * FROM vw_totals;

-- to delete a view use DROP
DROP VIEW vw_london_access;

