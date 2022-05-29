import scrapy

''' 
    1. Estrutura de código aberto para extrair dados do site de notícias da Exame

    2. Execução do código via cmd
    
'''

class ExameSpider(scrapy.Spider):

    '''
        Configuração do spider que irá visitar a página da web e extrair os dados 

    '''

    name = 'exame'
  
    start_urls = ['https://exame.com/eleicoes/'] 

    
    def parse(self, response):

        '''
            1. Método que envia uma request para cada página que contém uma noticia,
            e direciona o retorno das requests para o Método parse_new

            2. Extração de informações de fonte HTML realizada por seletores Xpath via cmd

        '''

        news =  response.xpath('//h3//a[re:test(@href, "brasil")]/@href').getall()        
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

        title = response.xpath('//div//h1/text()').get()
        author = response.xpath('//span//a/text()').get()
        date = response.xpath('//span[@class="sc-59870fc3-7 ibUGUv"]/text()').getall()
        body = response.xpath('//div/p').getall()
        tag = response.xpath('//a[@class="sc-93b4aacb-2 dOJSrp"]/text() ').getall()
        url = response.url
        
        yield {
               'title':title, 
               'author':author, 
               'date':date[1],
               'body':body,
               'tag':tag,
               'url':url
            }

    