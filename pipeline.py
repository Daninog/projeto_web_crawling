import os  
import pandas as pd

'''
    Pipeline dos dados:

    1. Execução dos códigos de crawler dos arquivos.py
    2. Importe dos arquivos.csv com os dados raspados
    3. Tratamento dos dados

'''

def execucao_spiders(cmd):

    try:

        '''
            Função que executa o comando das spiders em um subshell.
        '''

        os.system(cmd)
    
    except Exception as e:
        print('Erro na pipeline na execução das spiders: ', str(e))

def tratamento_dados(arquivo):

    '''
        Função que: 
        1. Importa os arquivos.csv 
        2. Faz tratamento dos dados
        3. Exporta os arquivos tratados em formato csv
    '''
    
    try:
        
            df_dados = pd.read_csv(arquivo, sep=',')
            
            #removendo linhas duplicadas
            df_dados = df_dados.drop_duplicates()

            #limpeza de dados desnecessários na data
            if arquivo == 'dados_band.csv' or arquivo == 'dados_cnn.csv':
              
                df = df_dados['date'].str.split(' ', n= 2, expand= True)
                df_dados['date'] = df[1]
            
            else:
                df = df_dados['date'].str.split(' ', n= 1, expand= True)
                df_dados['date'] = df[0]
            
            #mudança de cast
            df_dados['date'] = pd.to_datetime(df_dados.date)

            #ordenando pelo dia 
            df_dados = df_dados.sort_values(['date'])   

            #removendo as linhas que contém algum dado faltante
            df_dados = df_dados.dropna()
            
            #limpeza do corpo do texto           
            if arquivo == 'dados_band.csv':
            
                nump_dados = df_dados.to_numpy()
                for word in nump_dados:
                    word[3] =word[3].replace('<p>', '').replace('class', '').replace('app', '').replace('html', '').replace('/', '').replace('//a', '').replace('-', '').replace('=', '').replace('simple', '').replace('/-', '').replace('a =', '').replace('strong', '').replace('-simple', '').replace('/p', '').replace('/div', '').replace('/app', '').replace('-html', '').replace('/strong', '').replace('div', '').replace('-html', '').replace('app-', '').replace('href', '').replace('<', '').replace('>', '').replace('class=', '').replace('media', '').replace('</>', '').replace('figure', '').replace('</app', '').replace('</div> ', '').replace('', '').replace('<app-', '').replace('simple-', '').replace('html>', '').replace('<p', '').replace('<div>', '').replace('', '').replace('', '').replace('align:', '').replace('style=', '').replace('noopener', '').replace('rel=', '').replace('target=', '').replace('_blank', '').replace('<a href=', '').replace('""', '').replace('" <span>', '').replace('<span>', '').replace('</span>', '').replace('<a href=""', '').replace('</strong></a>', '').replace('<strong>', '').replace('</strong>', '').replace('</p>', '').replace('</a>', '')

                
            elif arquivo == 'dados_cnn.csv':
                
                nump_dados = df_dados.to_numpy()
                for word in nump_dados:
                    word[3] = word[3].replace('https://www.cnnbrasil.com.br/tudo-sobre/luis-carlos-heinze/', '').replace('<a href="">', '').replace('<p>', '').replace('</a>', '').replace('https://www.cnnbrasil.com.br/tudo-sobre/supremo-tribunal-federal-stf/', '').replace('<strong>', '').replace('</strong>', '').replace('</p>', '').replace('https://www.cnnbrasil.com.br/tudo-sobre/estados-unidos/', '').replace('https://www.cnnbrasil.com.br/politica/bolsonaro-diz-que-pode-nao-cumprir-decisao-do-supremo-sobre-marco-temporal/', '')

                           
            elif arquivo == 'dados_exame.csv':
                
                nump_dados = df_dados.to_numpy()
                for word in nump_dados:
                    word[3] =word[3].replace('<p>', '').replace('Conteúdo)', '').replace('<p', '').replace('"', '').replace('text-', '').replace('center', '').replace('align:', '').replace('style=', '').replace('noopener', '').replace('rel=', '').replace('target=', '').replace('_blank', '').replace('<a href=', '').replace('""', '').replace('" <span>', '').replace('<span>', '').replace('</span>', '').replace('<a href=""', '').replace('https://exame.com/noticias-sobre/joao-doria-junior/""', '').replace('target=""_blank"" rel=""noopener""><strong>', '').replace('</strong></a>', '').replace('<strong>', '').replace('</strong>', '').replace('</p>', '').replace('<p><a href=""https://exame.com/brasil/doria-deixa-corrida-presidencial/"" target=""_blank"" rel=""noopener"">', '').replace('</a>', '').replace('(Estadão', '').replace('LEIA', '').replace('TAMBÉM:', '').replace('</strong></p>,<p><a href=""https://exame.com/brasil/cupula-do-psdb-diz-que-ala-de-aecio-esta-isolada-e-doria-tera-protagonismo/"" target=""_blank"" rel=""noopener""><strong>', '').replace('<a href=""https://exame.com/brasil/pela-1a-vez-na-historia-psdb-desiste-de-eleicao-presidencial-veja-quem-fica/"" target=""_blank"" rel=""noopener""><strong>', '').replace('<p><a href=""https://exame.com/brasil/o-que-levou-doria-a-desistir-de-concorrer-a-presidencia/"" target=""_blank"" rel=""noopener""><strong>', '').replace('https://exame.com/brasil/doria-diz-que-tomara-decisao-sobre-futuro-na-vida-publica-apos-viagem/', '')

            df_dados = pd.DataFrame(nump_dados)

            #renomeando as colunas
            df_dados.columns = ['title', 
                               'author', 
                               'date_pub',
                               'body', 
                               'tag',
                               'url']

            df_dados = df_dados.set_index('title')

            #adicionando coluna para identificar cada site e exportando os arquivos
            if arquivo == 'dados_band.csv':
                df_dados.insert(1, 'site', 'Band', allow_duplicates=False)
                df_dados.to_csv('dados_band_tratado.csv') 
            elif arquivo == 'dados_cnn.csv':
                df_dados.insert(1, 'site', 'CNN', allow_duplicates=False)
                df_dados.to_csv('dados_cnn_tratado.csv')
            elif arquivo == 'dados_exame.csv':
                df_dados.insert(1, 'site', 'Exame', allow_duplicates=False)
                df_dados.to_csv('dados_exame_tratado.csv')  

    except Exception as e:
        print('Erro na pipeline no tratamento dos dados: ', str(e))







    