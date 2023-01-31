-- It is used to display the values in a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
SELECT id, name FROM cities WHERE state_id IN(SELECT id FROM states WHERE name = "California") ORDER BY id;
