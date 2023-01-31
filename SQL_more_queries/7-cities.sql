-- It is used to create a database and the table in the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
