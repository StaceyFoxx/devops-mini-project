CREATE DATABASE harry_potter;
USE harry_potter;

CREATE TABLE Houses
(
  House_id INT NOT NULL,
  Name VARCHAR(20) NOT NULL UNIQUE,  -- No duplicate house names
  Head VARCHAR(30),
  PRIMARY KEY (House_id)
);

CREATE TABLE Students
(
  Student_id INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(30) NOT NULL,
  Class VARCHAR(30),
  IQ INT,
  House INT NOT NULL,  -- Students must belong to a house
  Quidditch BOOLEAN DEFAULT FALSE,  -- Default to not playing
  PRIMARY KEY (Student_id),
  CONSTRAINT fk_student_house FOREIGN KEY (House) REFERENCES Houses(House_id)
);

INSERT INTO Houses (House_id, Name, Head)
VALUES
(1, "Gryffindor", "McGonagall"),
(2, "Slytherin", "Snape"),
(3, "Hufflepuff", "Sprout"),
(4, "Ravenclaw", "Flitwick");

INSERT INTO Students (Name, Class, IQ, House, Quidditch)
VALUES
("Harry", "Defence", 8, 1, TRUE),
("Hermione", "Charms", 10, 1, FALSE),
("Ron", "Divination", 6, 1, TRUE),
("Cedric", "Charms", 7, 3, TRUE),
("Draco", "Potions", 7, 2, TRUE),
("Neville", "Herbology", NULL, 1, FALSE),
("Cho", "Potions", 8, 4, NULL);
