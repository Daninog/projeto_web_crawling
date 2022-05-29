from pipeline import execucao_spiders
from pipeline import tratamento_dados
from conector_mysql import importe_arquivo


if __name__ == '__main__':

    try:

        '''
            Chamando a função para executar o código das spiders
        
        '''

        cmd_band = 'scrapy runspider band.py --nolog -O dados_band.csv'
        band = execucao_spiders(cmd_band)

        cmd_cnn = 'scrapy runspider cnn.py --nolog -O dados_cnn.csv'
        cnn = execucao_spiders(cmd_cnn)

        cmd_exame = 'scrapy runspider exame.py --nolog -O dados_exame.csv'
        exame = execucao_spiders(cmd_exame)
    
    except Exception as e:
        print('Erro no main na execução das spiders: ', str(e))

    try:

        '''
             Chamando a função para:
             1. Tratamento dos dados
             2. Geração arquivo csv
        
        '''

        arquivo_band = 'dados_band.csv'
        band = tratamento_dados(arquivo_band)

        arquivo_cnn = 'dados_cnn.csv'
        cnn = tratamento_dados(arquivo_cnn)

        arquivo_exame = 'dados_exame.csv'
        exame = tratamento_dados(arquivo_exame)

    except Exception as e:
        print('Erro no main no tratamento de dados: ', str(e))


    try:

        '''
             Chamando a função para inserção dos dados no MySQL
        
        '''

        caminho = 'dados_band_tratado.csv'
        tabela = 'sites'
        coluna = 'title, author, site, date_pub, body, tag, url'
        band_inserir = importe_arquivo(caminho, tabela, coluna)

        caminho = 'dados_cnn_tratado.csv'
        tabela = 'sites'
        coluna = 'title, author, site, date_pub, body, tag, url'
        cnn_inserir = importe_arquivo(caminho, tabela, coluna)

        caminho = 'dados_exame_tratado.csv'
        tabela = 'sites'
        coluna = 'title, author, site, date_pub, body, tag, url'
        exame_inserir = importe_arquivo(caminho, tabela, coluna)

       
    except Exception as e:
        print('Erro no main na inserção de dados: ', str(e))






