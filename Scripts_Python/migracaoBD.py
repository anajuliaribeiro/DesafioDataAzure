import pandas as pd
import pyodbc
import numpy as np
from os.path import exists
from datetime import datetime
from funcao_separar_telefone import separar_telefone

###############################################################
        ###### Usando Pandas e recursidade  #####
def lerCSV(nomeArq,tabela='',i=1):
    if(i<10):
        l='0'+str(i)
    else:
        l=str(i)

    if(i>1):
        pd_arquivo=pd.read_csv(nomeArq+l+'.csv',sep=';',header=None)
    else:
        pd_arquivo=pd.read_csv(nomeArq+l+'.csv',sep=';')
    

    gravandoBD(tabela,pd_arquivo)
   
    ########   recursividade  *******
    if exists((nomeArq+'0'+str(i+1)+'.csv') or (nomeArq+str(i+1)+'.csv')):
       lerCSV(nomeArq,tabela,i+1)
    
#############################################################################
def constroi_query_insert(tabela, qtdecampos,campos):
    query='INSERT INTO ' +tabela+'('

    for i in range(qtdecampos):
        query=query+campos[i]+','

    query=query[:-1]+')'
    query=query+' values('

    for i in range(qtdecampos):
        query=query+'?,'
    query=query[:-1]+')'
    return query
    
    
######################################################################################################################
# Connect to SQL Server
#https://docs.microsoft.com/pt-br/sql/machine-learning/data-exploration/python-dataframe-sql-server?view=sql-server-ver15
def gravandoBD(tabela, df):
    
    
    database = 'banco_transacao' 
    try:
        if (username!=''):
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        else:
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
            
        cursor = cnxn.cursor()
        query=constroi_query_insert(tabela, qtdecampos,campos)
   
    
        # Tabela de Clientes e Telefones:
        if (tabela=='Clientes'):
            campostel=[]
            campostel.append('cliente_id')
            campostel.append('cod_pais') 
            campostel.append('ddd') 
            campostel.append('numero_telefone')
            querytel=constroi_query_insert('Telefones', 4,campostel)
            
            for index, row in df.iterrows():
                partes_telefone=separar_telefone(row[4])
                codpais = partes_telefone[0]
                ddd = partes_telefone[1]
                n_telefone = partes_telefone[2]
                dataCa=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S %z')
                cursor.execute(query, row[0], row[1],row[2],dataCa) 
                cursor.execute(querytel,row[0], codpais, ddd,n_telefone)
        else:
            # Tabelas de Transações
            for index, row in df.iterrows():
                dataTra=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S %z')
                cursor.execute(query, row[0], row[1],row[2],dataTra)
        cnxn.commit()
        cursor.close()
    except pyodbc.Error as ex:
        print("Falha na conexao")        
            
    




###################################################################################
######################## script main #######
global server 
global username 
global password

global campos
global qtdecampos

server = '' 

username = '' 
password = ''

server= input("Server:  ")
resp=int(input("Digitar usuário e senha? (1-sim  2-não)"))
if(resp==1):
    username=input('Usuário: ')
    password = input('password: ')


qtdecampos=4

campos=[]
campos.append('id')
campos.append('nome') 
campos.append('email') 
campos.append('data_de_cadastro') 


lerCSV("./arquivos_carga_csv/clients-0", 'Clientes')


campos=[]
campos.append('id')
campos.append('cliente_id') 
campos.append('valor') 
campos.append('data_transacao_in') 

lerCSV("./arquivos_carga_csv/transaction-in-0", 'Transacoes_in')

campos=[]
campos.append('id')
campos.append('cliente_id') 
campos.append('valor') 
campos.append('data_transacao_out')

lerCSV("./arquivos_carga_csv/transaction-out-0", 'Transacoes_out')