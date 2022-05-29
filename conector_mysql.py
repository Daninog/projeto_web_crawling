import pandas as pd
import mysql.connector

'''
    Cria conexão com o SGBD my SQL e insere dados no banco

'''

user = ''
password = ''
host = ''
database = ''


def inserir(tabela, coluna, inserir_valores):
    try:
        con = mysql.connector.connect(user=user, password=password, host=host, database=database)
        cursor = con.cursor()
        query = f"INSERT INTO {tabela} ({coluna}) VALUES {inserir_valores};"     
        cursor.execute(query)
        cursor.close()
        con.commit()
        con.close()
    except Exception as e:
        print("Errona função inserir: ", str(e))

def importe_arquivo(caminho, tabela, coluna):

    '''
        Função para ler os arquivos e inserir os dados no banco de dados MySQL
    
    '''
    try:
        df_dado = pd.read_csv(caminho, sep=',')
          
        for i in range(len(df_dado)):
            inserir_valores = df_dado.iloc[i,0], df_dado.iloc[i,1], df_dado.iloc[i,2], \
                              df_dado.iloc[i,3], df_dado.iloc[i,4], df_dado.iloc[i,5], df_dado.iloc[i,6]
                  
            inserir(tabela, coluna, inserir_valores)
                
    except Exception as e:
        print('Erro na função importe_arquivo:', str(e))
    



   
        
    

