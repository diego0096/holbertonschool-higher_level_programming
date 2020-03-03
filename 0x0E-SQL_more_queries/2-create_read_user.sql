--create a new user and gives it only select priviliges
--create a new user and gives it only select priviliges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIDED BY 'user_0d_2_pwd'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost'
FLUSH PRIVILIGES;
