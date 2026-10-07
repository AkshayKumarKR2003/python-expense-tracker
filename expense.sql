CREATE DATABASE expense;
USE expense;
CREATE TABLE categories(id INT AUTO_INCREMENT PRIMARY KEY,name varchar(50));
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10,2),
    date DATE,
    category_id INT,
    payment_method VARCHAR(30),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
INSERT INTO categories (name) VALUES
('Food'),
('Travel'),
('Shopping'),
('Bills');
select * from categories;
