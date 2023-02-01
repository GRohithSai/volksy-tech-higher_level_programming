-- It is used to creata the user with password
CREATE USER 
    IF NOT EXISTS 'user_0d_1'@'localhost' 
    IDENTIFIED BY 'user_0d_1_pwd';
SHOW GRANTS ALL ON *.* TO 'user_0d_1'@'localhost';
