-- This creates a database hbtn_0d_usa
-- and also table states in the hbtn_0d_usa datatbase
-- with id INT auto genereated with unique, name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
