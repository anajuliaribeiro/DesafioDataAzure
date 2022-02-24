import pyodbc
import numpy as np
from datetime import datetime

#conexão com o banco para fazer a seleção das tabelas 

server = 'RIBEIROAJ' 
database = 'banco_transacao' 
username = '' 
password = ''

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()

# fazendo a seleção de TRANSAÇÕES IN 
cursor.execute("SELECT cliente_id, id, data_transacao_out FROM Transacoes_out  GROUP BY cliente_id, id, data_transacao_out ORDER BY  cliente_id, data_transacao_out")

#capturando os dados retornados do banco em um array 
row = cursor.fetchall()


array_dados = np.array(row)

cont_tran = 0

#leitura do array de resultados do banco
for transacao in array_dados:

        #comparando se o cliente atual e o próximo cliente da lisat de transações são os mesmos
        cliente_atual = array_dados[cont_tran, 0]
        prox_cliente = array_dados[cont_tran+1, 0]
        if cliente_atual == prox_cliente :

            #Se o cliente for o mesmo, captura a data e hora da transação 
            transacao_atual = array_dados[cont_tran, 2]
            transacao_prox = array_dados[cont_tran+1, 2]

            id_transacao = array_dados[cont_tran, 1]

            #calculo de diferença de tempo entre as transações
            result = transacao_atual - transacao_prox
            id = array_dados[cont_tran, 1]
            
            x = int(result.seconds)
            h = 86400
            res_hora = h - x

            if int(res_hora) <= 120:
                #se a transação for suspeita de fraude insere no banco
                print(f"A transacao {id} é fraude")         
                cursor.execute("INSERT INTO Fraudes (id_transacao, tipo_transacao) VALUES ( ? , 'OUT' )", id)
                cnxn.commit()
            else:
                #se não for fraude, apenas pula
                print(f"A transacao {transacao_atual} NÃO é fraude")
        else:
            #validando a mudança de cliente antes de iniciar a nova verificação
            print("Novo cliente")
        cont_tran += 1
     

    

