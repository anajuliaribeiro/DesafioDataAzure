import pyodbc
import numpy as np
from datetime import datetime


server = 'DESKTOP-VMM36BB'
database = 'banco_transacao'
username = ''
password = ''

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()

cursor.execute("SELECT cliente_id, id, data_transacao_in FROM Transacoes_in  GROUP BY cliente_id, id, data_transacao_in ORDER BY  cliente_id, data_transacao_in")

row = cursor.fetchall()
array_dados = np.array(row)

print(array_dados)

#criação de um contador para verificar a transação atual
cont_tran = 0

#leitura do array para analise das transações
for transacao in array_dados:
    #captura da transação atual e conversão de string para datetime
    transacao_atual = array_dados[cont_tran, 2]

    transacao_prox = array_dados[cont_tran+1, 2]

    #calculo de diferença de tempo entre as transações
    result = transacao_atual - transacao_prox

    #exibição do resultado
    # print(result.seconds)
    id = array_dados[cont_tran, 1]

    #Conversão para inteiro e validação da fraude ( se o tempo entre as transações forem de 120segundos - 2 minutos)
    if int(result.seconds) <= 120:
        print(f"A transacao {id} é fraude")
        cursor.execute("INSERT INTO Fraudes (id_transacao, tipo_transacao) VALUES ( ? , 'IN' )", id)
        cnxn.commit()
    #else:
        #print(f"A transacao {transacao_atual} NÃO é fraude")

    #aumentar o contador da linha da transação
    cont_tran += 1
