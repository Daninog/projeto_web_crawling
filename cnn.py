import scrapy

''' 
    1. Estrutura de código aberto para extrair dados do site de notícias da CNN

    2. Execução do código via cmd
    
'''

class CnnSpider(scrapy.Spider): 

    '''
        Configuração do spider que irá visitar a página da web e extrair os dados 

    '''

    name = 'cnn'
  
    start_urls = ['https://www.cnnbrasil.com.br/politica/'] 

    
    def parse(self, response):

        '''
            1. Método que envia uma request para cada página que contém uma noticia,
            e direciona o retorno das requests para o Método parse_new

            2. Extração de informações de fonte HTML realizada por seletores Xpath via cmd

        '''

        news =  response.xpath('//li//a[re:test(@href, "politica")]/@href').getall()
        for new in news:
            yield scrapy.Request(
                response.urljoin(new),  
                callback = self.parse_new
                )
    
    def parse_new(self, response):

        ''' 
            1. Método que retorna as informações de interesse de cada página de noticia

            2. Extração de dados de fonte HTML realizada por seletores Xpath via cmd

        Args:
            title (string): recebe o título da notícia
            author (string): recebe o autor da notícia
            date (string): recebe a data de publicação da notícia
            body (string): recebe o corpo do texto da notícia
            tag (string): recebe as tags da notícia
            url (string): recebe a url da página da noticia
        '''

        title = response.xpath('//header//h1/text()').get()
        author = response.xpath('//span/a/text()').get()
        author_from = response.xpath('//span[@class="tp__author"]/text()').get()
        author = author + author_from
        date = response.xpath('//span[@class="post__data"]/text()').get().split('|')
        date[0]
        body = response.xpath('//div[@class="post__content"]/p').getall()
        tag =  response.xpath('//li//a[@rel="tag"]/text()').getall()
        url =  response.url

        yield {
               'title':title, 
               'author':author, 
               'date':date[0],
               'body':body, 
               'tag':tag,
               'url':url
            }
