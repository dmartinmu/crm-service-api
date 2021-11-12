-- Creación de la BBDD crm
CREATE DATABASE crm;

CREATE TABLE public.users (
	user_id serial NOT NULL,
	email varchar(50) NOT NULL,
    "admin" boolean NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY (user_id)
);

CREATE TABLE public.customers (
	customer_id serial NOT NULL,
	"name" varchar(50) NOT NULL,
	surname varchar(50) NOT NULL,
	id varchar(10) NOT NULL,
    photo_url varchar(50) NULL,
    creator_user_id int4 NOT NULL,
    editor_user_id int4 NOT NULL,
	CONSTRAINT customers_pk PRIMARY KEY (customer_id),
    CONSTRAINT customers_users_fk FOREIGN KEY (creator_user_id) REFERENCES public.users(user_id),
    CONSTRAINT customers_users_fk_2 FOREIGN KEY (editor_user_id) REFERENCES public.users(user_id)
);

-- Users
insert into public.users (email, "admin") values ('admin@theagilemonkeys.com', true); 
insert into public.users (email, "admin") values ('user@theagilemonkeys.com', false); 

-- Customers
insert into public.customers ("name", surname, id, creator_user_id, editor_user_id) values ('John M.', 'Neal', '12345689A', 1, 1);
insert into public.customers ("name", surname, id, creator_user_id, editor_user_id) values ('Vernon J.', 'Harrison', '50123123X', 2, 2);
insert into public.customers ("name", surname, id, creator_user_id, editor_user_id) values ('Flora D.', 'Glazer', '23456189P', 2, 1);