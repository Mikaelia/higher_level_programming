-- Creates a database hbtn_0d_2 and user_0d_2
-- user_0d_2 has only SELECT privileges in the database
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost' IDENTIFIED BY'user_0d_2_pwd';
