CREATE DATABASE flask_auth;

USE flask_auth;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    carid INT,
    carname VARCHAR(100),
    name VARCHAR(100),
    age INT,
    booking_date DATE,
    return_date DATE,
    amount int,
    email varchar(40),
    text varchar(60)
);
ALTER TABLE bookings ADD UNIQUE (name, booking_date);
select * from users;
select * from bookings;