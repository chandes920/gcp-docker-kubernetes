CREATE TABLE public.users (
	id serial PRIMARY KEY,
	username VARCHAR ( 50 ) NOT NULL,
	password VARCHAR ( 255 ) NOT NULL
);

INSERT INTO public.users values (1, 'username', 'password');
