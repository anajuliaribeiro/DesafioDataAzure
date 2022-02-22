import pandas as pd
import numpy as np
from datetime import datetime

#teste de recebimento dos dados 
dados_recebidos = np.array( pd.read_csv('./transaction-in-001.csv', sep=';'))

#criação de um contador para verificar a transação atual 
cont_tran = 0

#leitura do array para analise das transações
for transacao in dados_recebidos:

    #captura da transação atual e conversão de string para datetime
    transacao_atual = dados_recebidos[cont_tran, 3]
    date_time_a = datetime.strptime(transacao_atual,'%Y-%m-%d %H:%M:%S %z')
     
    #captura da próxima transação da lista e conversão de string para datetime
    transacao_prox = dados_recebidos[cont_tran+1, 3]
    date_time_b= datetime.strptime(transacao_prox,'%Y-%m-%d %H:%M:%S %z')

    #calculo de diferença de tempo entre as transações
    result = date_time_a - date_time_b

    #exibição do resultado 
    # print(result.seconds)

    #Conversão para inteiro e validação da fraude ( se o tempo entre as transações forem de 120segundos - 2 minutos)
    if int(result.seconds) <= 120:
        print(f"A transacao {transacao_atual} é fraude")
    else:
        print(f"A transacao {transacao_atual} NÃO é fraude")

    #aumentar o contador da linha da transação 
    cont_tran += 1
    