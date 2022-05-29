-- CRIAÇÃO DO BANCO DE DADOS
create database desafio;
use desafio;

create table if not exists sites(
	title text,
	author text,
	site text,
	date_pub text,
	body text,
	tag text,
    url varchar(700),
	UNIQUE (url)
);


select * from sites;
drop table sites;
-- -----------------------------------------------------------------MÉTRICAS----------------------------------------------------------------------------

-- QUANTIDADE DE CARACTERES DO CORPO DO TEXTO POR CADA NOTICIA
select title, author as autores_Band, date_pub, site, body as corpo_do_texto_da_noticia, length(body) as quantidade_caracteres_body, tag, url from sites;

-- MÉDIA DE CARACTERES POR SITE
select site, avg(length(body)) as média_caracteres_body from sites group by site;
