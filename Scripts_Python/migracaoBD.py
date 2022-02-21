import pandas as pd
import pyodbc
import numpy as np
from os.path import exists
from datetime import datetime


###############################################################
        ###### Usando Pandas e recursidade  #####
def lerCSV(nomeArq,i=1):
    if(i<9):
        l='0'+str(i)
    else:
        l=str(i)
    pd_arquivo=pd.read_csv(nomeArq+l+'.csv',sep=';')
    gravandoBD('Cliente',pd_arquivo)
   
    #print(type(pd_arquivo))
    #if exists((nomeArq+'0'+str(i+1)+'.csv') or (nomeArq+str(i+1)+'.csv')):
    #    lerCSV(nomeArq,i+1)
    
###############################################################
# Connect to SQL Server
#https://docs.microsoft.com/pt-br/sql/machine-learning/data-exploration/python-dataframe-sql-server?view=sql-server-ver15
def gravandoBD(tabela, df):
    
    server = 'LAPTOP-149LUH3Q' 
    database = 'banco_transacao' 
    username = '' 
    password = ''
    #Quando tiver senha usar esta linha 
    #cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    # Trusted Connection to Named Instance
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQL2K19;DATABASE=SampleDB;Trusted_Connection=yes;')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    query='INSERT INTO ' +tabela+'('
    for i in range(qtdecampos):
        query=query+campos[i]+','
    query=query[:-1]+')'
    query=query+' values('
    for i in range(qtdecampos):
        query=query+'?,'
    query=query[:-1]+')'
    
    # Insert Dataframe into SQL Server:

    for index, row in df.iterrows():
        #print (df.loc[index,'id'])
        #print(row.id)
        cursor.execute(query, row.id, row.nome,row.email,row.data_cadastro,row.telefone)
        # separar o fuso em uma coluna a partir.
        #cursor.execute(query, row.id, row.nome,row.email,datetime.strptime(row.data_cadastro, '%Y-%m-%d %H:%M:%S -%I%I%I'),row.telefone)
        #cursor.execute("INSERT INTO HumanResources.DepartmentTest (DepartmentID,Name,GroupName) values(?,?,?)", row.DepartmentID, row.Name, row.GroupName)
    cnxn.commit()
    cursor.close()




###################################################################################

global campos
global qtdecampos

campos=[]
campos.append('id')
campos.append('nome') 
campos.append('email') 
campos.append('data_de_cadastro') 
campos.append('telefone')
qtdecampos=5
lerCSV("./arquivos_carga_csv/clients-0")
