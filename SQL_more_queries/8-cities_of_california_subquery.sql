-- It is used to display the values in a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_od_usa;
CREATE TABLE IF NOT EXISTS states(id INT, name VARCHAR(256));
INSERT INTO states VALUES(1, "California"), (2, "Arizona"), (3, "Texas"), (4, "Utah");
CREATE TABLE IF NOT EXISTS cities(id INT, state_id INT, name VARCHAR(256));
INSERT INTO cities values(1, 1, "San Fransico"), (2, 1, i"San Jose"), (4, 2, "Page"), (6, 3, "Paris"), (7, 3, "Houston"), (8, 3, "Dallas"));
SELECT id, name FROM cities where state_id IN (select id from states where name = "California") ORDER BY id;
