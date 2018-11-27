-- Initialize the database.
-- Drop any existing data and create empty tables.
-- Create the admin user

DROP TABLE IF EXISTS user;

CREATE TABLE user
(
  id       INTEGER PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT        NOT NULL,
  is_admin BIT         NOT NULL
);


INSERT INTO user VALUES(NULL, 'admin', 'admin', 1)