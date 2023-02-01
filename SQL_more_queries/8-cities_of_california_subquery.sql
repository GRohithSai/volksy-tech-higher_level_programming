-- It is used to display the values in a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities(id INT, state_id INT, name VARCHAR(256));
INSERT INTO cities VALUES(1, 1, "San Francisco"), (2, 1, "San Jose"), (4, 2, "Page"), (6, 3, "Paris"), (7, 3, "Houston"), (8, 3, "Dallas");
SELECT id, name FROM cities WHERE state_id IN(SELECT id FROM states WHERE name = "California") ORDER BY id;
