import scrapy

''' 
    1. Estrutura de código aberto para extrair dados do site de notícias da Band 

    2. Execução do código via cmd
    
'''

class BandSpider(scrapy.Spider): 

    '''
        Configuração do spider que irá visitar a página da web e extrair os dados 

    '''
    
    name = 'band'
  
    start_urls = ['https://band.uol.com.br/eleicoes/'] 

    
    def parse(self, response):

        '''
            1. Método que envia uma request para cada página que contém uma noticia,
            e direciona o retorno das requests para o Método parse_new

            2. Extração de informações de fonte HTML realizada por seletores Xpath via cmd

        '''

        news =   response.xpath('//li//a[re:test(@href, "eleicoes/noticias/")]/@href').getall()
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
        author = response.xpath('//i[@class="author__name"]/text()').get()
        date = response.xpath('//i[@class="author__date-hour"]/text()').get()
        body = response.xpath('//div[@class="text"]/app-simple-html').getall()
        tag =  response.xpath('//li//a[@class="tag"]/text()').getall()
        url =  response.url

        yield {
               'title':title, 
               'author':author, 
               'date':date,
               'body':body, 
               'tag':tag,
               'url':url
            }
