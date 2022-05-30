# Projeto Web Crawling

## Objetivo

O objetivo do projeto foi desenvolver um código em linguagem python capaz de raspar 
dados de sites de notícias concorrentes e ao final realizar algumas métricas.

### Motivação: Por que criar web crawlers?

Nem todo site tem API's de onde podemos extrair dados de forma organizada e simplificada, como no formato JSON por exemplo, 
por isso se faz necessário o desenvolvimento de ferramentas para a extração de dados. Os web crawlers, também conhecidos por spiders, colhem as informações que estão espalhadas pelos sites e as organiza de forma estruturada para podermos utilizá-las.

### Etapas do projeto

- Pesquisa das páginas da internet de interesse que permitissem a extração de dados de forma efetiva e 
seleção das informações que seriam extraídas:

	- Sites: Band, CNN e Exame.
	- Raspagem: título, autor, data da publicação, corpo do texto, tag e url.


- Criação de três spiders, uma para cada site de notícia, através do Scrapy um framework de 
web crawling gratuíto e de código aberto. Nesse processo de raspagem 
das páginas da internet é necessário extrair dados de fontes HTML e o scrapy tem
seu próprio mecanismo de extração através de seletores css e xpath.

- Tratamento de dados realizada através de Data Frame Pandas e Numpy.

- Criação de um banco de dados MySQL e tabela em linguagem SQL.

- Ingestão automatizada dos dados tratados no SGBD.

- Métricas realizadas no banco de dados.

### Análise dos dados:

- Medição do tamanho do texto da notícia veículada a quantidade de caracteres contabilizados:

  - Band: 2548
  - CNN: 3910
  - Exame: 4157

O tamanho da noticia pode interferir no tempo de leitura e interesse do leitor na página, as notícias
do site Exame revelaram que a média supera em quase o dobro a concorrente Band.


### Requerimentos para realização do código

- Pyhton 3.10.1
- Scrapy 2.6.1
- Pandas 1.4.2
- Numpy 1.21.4
- Mysql conector 2.2.9




