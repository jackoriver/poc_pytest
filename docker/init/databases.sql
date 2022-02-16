# create databases
CREATE DATABASE IF NOT EXISTS `wordpress`;
CREATE DATABASE IF NOT EXISTS `testlink`;

# create root user and grant rights
CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'local';
CREATE USER 'tl_user'@'localhost' IDENTIFIED BY 'local';
ALTER USER 'wp_user'@'localhost' IDENTIFIED BY 'Sentalf12!';
ALTER USER 'tl_user'@'localhost' IDENTIFIED BY 'Sentalf12!';

GRANT ALL PRIVILEGES ON wordpress.* TO 'wp_user'@'%' IDENTIFIED BY 'Sentalf12!';
GRANT ALL PRIVILEGES ON testlink.* TO 'tl_user'@'%' IDENTIFIED BY 'Sentalf12!';

FLUSH PRIVILEGES;