-- Users
insert into users (email, "admin") values ('admin@theagilemonkeys.com', true); 
insert into users (email, "admin") values ('user@theagilemonkeys.com', false); 

-- Customers
insert into customers ("name", surname, id, creator_user_id, editor_user_id) values ('John M.', 'Neal', '12345689A', 1, 1);
insert into customers ("name", surname, id, creator_user_id, editor_user_id) values ('Vernon J.', 'Harrison', '50123123X', 2, 2);
insert into customers ("name", surname, id, creator_user_id, editor_user_id) values ('Flora D.', 'Glazer', '23456189P', 2, 1);