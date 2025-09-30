CREATE DATABASE property_reviews;

USE property_reviews;

-- Properties Table
CREATE TABLE properties (
    property_id INT PRIMARY KEY,
    property_name VARCHAR(255),
    city VARCHAR(100),
    price VARCHAR(10),
    company_name VARCHAR(255)
);
-- Reviews Table
CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    property_id INT,
    review_text TEXT,
    score INT,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);
-- Sample Data for Properties Table:
INSERT INTO properties (property_id, property_name, city, price, company_name)
VALUES
  (1, 'Cozy Apartment', 'CityA', "$100", 'Property Management A'),
  (2, 'Spacious Condo', 'CityB', "$150", 'Property Management B'),
  (3, 'Luxury Villa', 'CityC', "$300", 'Property Management C'),
  (4, 'Downtown Loft', 'CityA', "$120", 'Property Management A'),
  (5, 'Seaside Cottage', 'CityB', "$80", 'Property Management B');

-- Sample Data for Reviews Table with Words 'dirty,' 'cleaning,' or 'clean'
INSERT INTO reviews (review_id, property_id, review_text, score)
VALUES
  (101, 1, 'Perfect place for families. Spacious rooms and kid-friendly amenities.', 5),
  (102, 2, 'Family vacation was a delight. Beautiful view from the condo.', 4),
  (103, 3, 'Great for families. Kids loved the pool in the villa.', 5),
  (104, 4, 'Ideal for a family getaway. Downtown location added convenience.', 3),
  (105, 5, 'Family enjoyed the seaside cottage. Clean and comfortable.', 4),
  (106, 1, 'The apartment was dirty. Needs cleaning urgently!', 2),
  (107, 2, 'Clean and tidy. No issues at all.', 5),
  (108, 3, 'Just average.', 3),
  (109, 4, 'Nice place for stay. Kid friendly', 4),
  (110, 5, 'Perfect location.', 2);