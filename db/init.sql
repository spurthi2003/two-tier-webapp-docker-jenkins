CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

CREATE TABLE IF NOT EXISTS greetings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    message VARCHAR(255)
);

INSERT INTO greetings (message)
VALUES ('Hello from MySQL Database!');
