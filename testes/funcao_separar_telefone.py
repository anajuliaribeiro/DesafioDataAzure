#usar o split
import re

#transformar em uma função 
def separar_telefone(telefone):
    partes_telefone = re.split('[( )]', telefone) #essa função separa a string por dois ou mais caracteres que estão dentro do [ ]
    # codpais = partes_telefone[0]
    # DDD = partes_telefone[1]
    # n_telefone = partes_telefone[2]
    return partes_telefone #lista


#referência: https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python

