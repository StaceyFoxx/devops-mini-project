use joins_practice;

-- USE THE SAME FRUIT TABLES THAT WE PRACTICED WITH FOR JOINS

/* UNION */
SELECT t1.ID AS ID1, t1.Fruit AS Fruit1
FROM Table1_fruit_basket t1 
UNION
SELECT t2.ID AS ID2, t2.Fruit AS Fruit2
FROM Table2_fruit_basket t2;


/* UNION ALL*/
SELECT t1.ID AS ID1, t1.Fruit AS Fruit1
FROM Table1_fruit_basket t1 
UNION ALL
SELECT t2.ID AS ID2, t2.Fruit AS Fruit2
FROM Table2_fruit_basket t2;