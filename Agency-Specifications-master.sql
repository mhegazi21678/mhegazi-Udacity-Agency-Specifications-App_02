GET https://hij-fsnd.eu.auth0.com/authorize?
  audience=API_IDENTIFIER&
  response_type=code&
  client_id=SecWtYHGlbQtw5GgffJ25KEPAYJFOBsz&
  redirect_uri=undefined
  
Client ID = yENoy6uO91hJVbLWNOKEzuPyDi3ysDbX

lOGiN: https://hij-fsnd.eu.auth0.com/authorize?audience=Agency_Specifications&response_type=token&client_id=yENoy6uO91hJVbLWNOKEzuPyDi3ysDbX&redirect_uri=http://localhost:8080/login-results

LogOut: https://hij-fsnd.eu.auth0.com/v2/logout?client_id=yENoy6uO91hJVbLWNOKEzuPyDi3ysDbX&returnTo=http://localhost:8080/logout

************************************************************************************************************************

Roles:
Casting Assistant
	Can view actors and movies

Casting Director
	All permissions a Casting Assistant has and…
	Add or delete an actor from the database
	Modify actors or movies

Executive Producer
	All permissions a Casting Director has and…
	Add or delete a movie from the database


GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/


***********************************************************************************************************************

Users: 

CastingAssistant@gmail.com
CastingAssistant!


CastingDirector@gmail.com
CastingDirector!

executiveproducer@gmail.com
ExecutiveProducer!

**********************************************************************************************************************
class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime)

release_date timestamp without time zone NOT NULL,

-- SEQUENCE: public.Movie_id_seq

-- DROP SEQUENCE public.Movie_id_seq;

CREATE SEQUENCE public.Movie_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.Movie_id_seq
    OWNER TO postgres;
	
	

-- Table: public.Movie

-- DROP TABLE public.Movie;

CREATE TABLE public.Movie
(
    id integer NOT NULL DEFAULT nextval('Movie_id_seq'::regclass),
    title character varying COLLATE pg_catalog."default",
    release_date timestamp without time zone NOT NULL,
    CONSTRAINT Movie_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.Movie
    OWNER to postgres;
	
---------------------------------------------------------------------------------------------
class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)

-- SEQUENCE: public.Actor_id_seq

-- DROP SEQUENCE public.Actor_id_seq;

CREATE SEQUENCE public.Actor_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.Actor_id_seq
    OWNER TO postgres;
	
	

-- Table: public.Actor

-- DROP TABLE public.Actor;

CREATE TABLE public.Actor
(
    id integer NOT NULL DEFAULT nextval('Actor_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default"  NOT NULL,
	age integer,
	gender character varying COLLATE pg_catalog."default",
    CONSTRAINT Actor_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.Actor
    OWNER to postgres;



-------------------------------------------------

python -m unittest test_my_app_02.py

pg_dump -U postgres agencyspecifications > agencyspecifications_test.pgsql

DROP DATABASE [IF EXISTS] agencyspecifications_test;

psql -U postgres agencyspecifications_test < agencyspecifications_test.pgsql
	
	
--*****************************************************************************************

heroku create agencyspecificationsmasterapp	

$ heroku create agencyspecificationsmasterapp
 »   Warning: heroku update available from 7.52.0 to 7.53.0.
Creating agencyspecificationsmasterapp... done
https://agencyspecificationsmasterapp.herokuapp.com/ | https://git.heroku.com/agencyspecificationsmasterapp.git

-------------------------------
first need to make the directory repository in git:

https://github.com/mhegazi21678/mhegazi-Udacity-Agency-Specifications-App.git

echo "# mhegazi-Udacity-Agency-Specifications-App" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mhegazi21678/mhegazi-Udacity-Agency-Specifications-App.git
git push -u origin main


git remote add heroku https://git.heroku.com/agencyspecificationsmasterapp.git
------------------------------------------------
heroku addons:create heroku-postgresql:hobby-dev --app agencyspecificationsmasterapp

$ heroku addons:create heroku-postgresql:hobby-dev --app agencyspecificationsmasterapp
 »   Warning: heroku update available from 7.52.0 to 7.53.0.
Creating heroku-postgresql:hobby-dev on agencyspecificationsmasterapp... free
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-closed-62716 as DATABASE_URL
Use heroku addons:docs heroku-postgresql to view documentation

-------------------------------------------------

heroku config --app agencyspecificationsmasterapp	

$ heroku config --app agencyspecificationsmasterapp
 »   Warning: heroku update available from 7.52.0 to 7.53.0.
=== agencyspecificationsmasterapp Config Vars
DATABASE_URL: postgres://rnnhdflqtiexnl:6efe0b38acaa99100c0e9ebda8ba45c5b816519b7321a0e02d985a459ff95c1a@ec2-18-215-111-67.compute-1.amazonaws.com:5432/d1fr05l88m7v03


git push heroku main


# CASTINGASSISTANT_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVlbkNtRTgtcDExRTg1QjZod1JfNiJ9.eyJpc3MiOiJodHRwczovL2hpai1mc25kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDkwNWM4ZmFkNzg0ZTAwNjkzY2Q0YTUiLCJhdWQiOiJBZ2VuY3lfU3BlY2lmaWNhdGlvbnMiLCJpYXQiOjE2MjEwMTY5NTEsImV4cCI6MTYyMTAyNDE1MSwiYXpwIjoieUVOb3k2dU85MWhKVmJMV05PS0V6dVB5RGkzeXNEYlgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.kSOe0n8auuboSHAd9eLlWZIXOCSiF-keaV380Sm3Z44yjGIXyad3XRNL_pBmwjomnuoj7qGGpVa1l9tTGgjycguXsDN-oyHjCUwmgRYOnwvQ27ZLP9E4hI_U8BKjeINmw7ScFYgGf1P6rUq3K_lfezRLBuW7dhU47gHKE-YzDA7b7M461fSEEw9_NLFzaLIlFN2xdLKFFOPF3AlZNEzkC5M2bZdTihskNxXno5fZv03LyIaOdJO1iiscvzBkD0PYMTta3itMkmHlE2teCwKysC3yfgdv6Z9gywouuebfovtF4Rk2dLodjkzZmz1YlgTUDj9mBCC3jCKfAn61TY2bXQ"
# EXECUTIVEPRODUCER_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVlbkNtRTgtcDExRTg1QjZod1JfNiJ9.eyJpc3MiOiJodHRwczovL2hpai1mc25kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDkwNWQ0ZGJmM2FkMDAwNzBjZDczOTMiLCJhdWQiOiJBZ2VuY3lfU3BlY2lmaWNhdGlvbnMiLCJpYXQiOjE2MjEwOTg2NTAsImV4cCI6MTYyMTEwNTg1MCwiYXpwIjoieUVOb3k2dU85MWhKVmJMV05PS0V6dVB5RGkzeXNEYlgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.lG69Ar9Dxe14ErlG3tvaPaKwbzxiK-Z_jFpdxTUhjAAF8KkgigTfkaTNVNDItOAGdzjSz1YbzHXKMtA1cOVYpHUfKgL_MRtS8TAurZr4YkpFix3-3JjELbd2tObKWsZgnqDLK5qxsIYF8u3X_2CmNhUoGMOA7hGZLGo69c0wcEbE9cjB6H1c3LlucfX0v7tWXTxs2Bz_9xuFV9kicyI02CUpfPpN_WFT2u-CBqOt2zKOGqbPaPG1I2Ynw1FHrr5tJvuIBAlcjywcr0-S33pI9t-PPWIbJ0xBEpgc9erLTuT3LCexz07SbFs7f3PTx3nHaV9hPFeJNMaX3gE7kY0mcw"
# CASTINGDIRECTOR_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVlbkNtRTgtcDExRTg1QjZod1JfNiJ9.eyJpc3MiOiJodHRwczovL2hpai1mc25kLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDkwNWNmNTk3MDVjNjAwNzFhYzJjNjgiLCJhdWQiOiJBZ2VuY3lfU3BlY2lmaWNhdGlvbnMiLCJpYXQiOjE2MjA0ODg3MjEsImV4cCI6MTYyMDQ5NTkyMSwiYXpwIjoieUVOb3k2dU85MWhKVmJMV05PS0V6dVB5RGkzeXNEYlgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.vszoiwubQlzAiR8TlB0wYJLFEVpkFOR0TdDSEvd-zKrgGnMbZLweqs6-KLb7pR3ZYaNJ1jamjKKtI8UtilZX0N84WT_VfCxHr3VUwPyDvGSNcCBq8iUd6KgA1EO7CwNFfPUwu-IBAMiKDapi4oGxtoTGzahQbOVZ-8yEMFNPCXWXH5TVCMMwntbWsIXL9oxZsgnId8DpqBfXhqZMAWTYwJw5HVuJYKgkgv1rqUBF6tqCbq4e4fVzqZ8_fLvIVLx2dtVB6KNmy0dvEf-6pQCrm6DAaiUAb2wnZxNUJXoY8ohhlsOUYC0ECkoxVwrOlcwNXqYyi8uxX9TS1W-SKJMrMQ"



