DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  fullname text,
  email text,
  password text
);

INSERT INTO users (fullname, email, password) VALUES ('Sam', 'sam@example.com', 'password123!');
