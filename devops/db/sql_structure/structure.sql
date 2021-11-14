CREATE TABLE users (
	user_id serial NOT NULL,
	email varchar(50) NOT NULL,
    password_hash varchar(200) NOT NULL,
    "admin" boolean NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY (user_id)
);

CREATE TABLE customers (
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
