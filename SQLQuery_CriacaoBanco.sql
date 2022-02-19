-- Criação da dabase do banco 

create database banco_transacao
use banco_transacao

-- Criacao da tabela de Clientes
create table Cliente (
id int not null primary key,
nome varchar(255),
email varchar(255),
data_de_cadastro datetime,
pais_telefone varchar(5),
ddd_telefone varchar(5),
telefone varchar(10)
);

--Criacao da tabela de Transações-IN  


-- Criacao da tabela de Transações-OUT