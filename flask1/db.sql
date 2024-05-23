create database geeklogin;
use geeklogin;

CREATE TABLE accounts
(
    id INTEGER  PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(50),
    email VARCHAR(50)
);
