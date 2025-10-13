-- Create Houses table first
CREATE DATABASE Harry_potter;

USE harry_potter;

CREATE TABLE Houses
(
  House_id INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(20) NOT NULL,
  Head VARCHAR(30),
  PRIMARY KEY (House_id)
);

-- Create Students table with a foreign key referencing Houses
CREATE TABLE Students
(
  Student_id INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(20) NOT NULL,
  Class VARCHAR(20),
  IQ INT,
  House INT,
  Quidditch BOOLEAN,
  PRIMARY KEY (Student_id),
  FOREIGN KEY (House) REFERENCES Houses(House_id)
);

-- Insert data into Houses table
INSERT INTO Houses (House_id, Name, Head)
VALUES
(1, "Gryffindor", "McGonagall"),
(2, "Slytherin", "Snape"),
(3, "Hufflepuff", "Sprout"),
(4, "Ravenclaw", "Flitwick");

-- Insert data into Students table
INSERT INTO Students (Name, Class, IQ, House, Quidditch)
VALUES
("Harry", "Defence", 8, 1, TRUE),
("Hermione", "Charms", 10, 1, FALSE),
("Ron", "Divination", 6, 1, TRUE),
("Cedric", "Charms", 7, 3, TRUE),
("Draco", "Potions", 7, 2, TRUE),
("Neville", "Herbology", NULL, 1, FALSE),
("Cho", "Potions", 8, 4, NULL);