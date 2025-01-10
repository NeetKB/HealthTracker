DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  fullname text,
  email text,
  password text
);

INSERT INTO users (fullname, email, password) VALUES ('Sam', 'sam@example.com', 'a109e36947ad56de1dca1cc49f0ef8ac9ad9a7b1aa0df41fb3c4cb73c1ff01ea');
-- Sam password is password123!
INSERT INTO users (fullname, email, password) VALUES ('Mary Contrary', 'mc@example.com', 'f9d769e4798dee8ebeb55b2075ca9d44bb573248ee60f972e00ae3157bf636c7');
-- Mary password is passing12!
