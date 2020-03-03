--Create a new user in mysql and granted all priviliges
--Create a new user in mysql and granted all priviliges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost'; 
