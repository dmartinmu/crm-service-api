-- Users
insert into users (email, password_hash, "admin") values ('admin@theagilemonkeys.com', 'pbkdf2:sha256:260000$hoKrZ7Q7deiCdAPR$814a4c573bd283bbfd3f1c005c67f90a44c26a0cd416591b494daaaec1c1c848', true); 
insert into users (email, password_hash, "admin") values ('user@theagilemonkeys.com', 'pbkdf2:sha256:260000$30gaGIVfEscDAznM$26bb1cbc0081d0edc1663656e1b07fb9261b677921155c6f6db42830b1dd4687', false); 
insert into users (email, password_hash, "admin") values ('test1@test.com', 'pbkdf2:sha256:260000$30gaGIVfEscDAznM$26bb1cbc0081d0edc1663656e1b07fb9261b677921155c6f6db42830b1dd4687', false); 
insert into users (email, password_hash, "admin") values ('test2@test.com', 'pbkdf2:sha256:260000$30gaGIVfEscDAznM$26bb1cbc0081d0edc1663656e1b07fb9261b677921155c6f6db42830b1dd4687', false); 

-- Customers
insert into customers ("name", surname, id, creator_user_id, editor_user_id) values ('John M.', 'Neal', '12345689A', 1, 1);
insert into customers ("name", surname, id, creator_user_id, editor_user_id) values ('Vernon J.', 'Harrison', '50123123X', 2, 2);
insert into customers ("name", surname, id, creator_user_id, editor_user_id) values ('Flora D.', 'Glazer', '23456189P', 2, 1);