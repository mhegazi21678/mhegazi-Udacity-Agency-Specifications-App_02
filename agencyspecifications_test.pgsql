--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Actor" (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer,
    gender character varying
);


ALTER TABLE public."Actor" OWNER TO postgres;

--
-- Name: Actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Actor_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actor_id_seq" OWNER TO postgres;

--
-- Name: Actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Actor_id_seq" OWNED BY public."Actor".id;


--
-- Name: Movie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Movie" (
    id integer NOT NULL,
    title character varying NOT NULL,
    release_date timestamp without time zone
);


ALTER TABLE public."Movie" OWNER TO postgres;

--
-- Name: Movie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Movie_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movie_id_seq" OWNER TO postgres;

--
-- Name: Movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Movie_id_seq" OWNED BY public."Movie".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: Actor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actor" ALTER COLUMN id SET DEFAULT nextval('public."Actor_id_seq"'::regclass);


--
-- Name: Movie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movie" ALTER COLUMN id SET DEFAULT nextval('public."Movie_id_seq"'::regclass);


--
-- Data for Name: Actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Actor" (id, name, age, gender) FROM stdin;
2	Sawsan Hetto	30	Female
3	Adel Emam	75	Male
1	Saleem Aaga	42	Male
4	Hanan Tork	46	Female
5	Ahmed Helmy	51	Male
6	Ahmed El Sakka	48	Male
7	Mohamed Ramadan	32	Male
8	Hend Sabry	41	Female
9	Donia Samir Ghanem	36	Female
10	Ghada Abdel Razek	55	Female
11	Yasmin Abdulaziz	41	Female
12	Mona Zaki	44	Female
13	Mai Ezz Eldin	41	Female
14	Mais Hamdan	38	Female
15	Ayten Amer	34	Female
16	Nesreen Tafesh	39	Female
17	Sameer Ganem	95	Male
18	Nancy Ajram	35	Female
19	Elissa	49	Female
20	Kadim Al Shahir	63	Male
21	Najwa Karam	55	Female
22	Assala Nasri	51	Female
23	Ahlam Al Shamsi	53	Female
24	Ragheb Alama	58	Male
25	Georges Wassouf	59	Male
26	Tamer Hosny	43	Male
\.


--
-- Data for Name: Movie; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Movie" (id, title, release_date) FROM stdin;
2	Hanafe el Obaha	1982-04-22 00:00:00
1	my story	1978-06-21 00:00:00
3	Theeb	2014-01-01 00:00:00
4	Broken Cameras	2011-01-01 00:00:00
5	The Day I Lost My Shadow	2018-01-01 00:00:00
6	The Time That Remains	2009-01-01 00:00:00
7	Amreeka	2009-01-01 00:00:00
8	Very Big Shot	2015-01-01 00:00:00
9	Under the Bombs	2007-01-01 00:00:00
10	Ajami	2009-05-01 00:00:00
11	Photocopy	2017-09-23 00:00:00
12	Barakah Meets Barakah	2016-07-15 00:00:00
13	Wadjda	2012-08-10 00:00:00
14	Where Do We Go Now	2011-05-20 00:00:00
15	Sheikh Jackson	2017-02-04 00:00:00
16	Clash	2016-01-09 00:00:00
17	Blessed Benefit	2016-09-09 00:00:00
18	Very Big Shot	2015-10-01 00:00:00
19	Six Windows in the Desert	2016-10-01 00:00:00
21	Villa 69	2013-11-11 00:00:00
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Name: Actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Actor_id_seq"', 26, true);


--
-- Name: Movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Movie_id_seq"', 21, true);


--
-- Name: Actor Actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actor"
    ADD CONSTRAINT "Actor_pkey" PRIMARY KEY (id);


--
-- Name: Movie Movie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movie"
    ADD CONSTRAINT "Movie_pkey" PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- PostgreSQL database dump complete
--

