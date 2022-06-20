CREATE TABLE public.users (
	id serial PRIMARY KEY,
	fullname VARCHAR ( 100 ) NOT NULL,
	username VARCHAR ( 50 ) NOT NULL,
	password VARCHAR ( 255 ) NOT NULL
);

INSERT INTO public.users values (1, 'Desmond Chan', 'username', 'password');

#testing
