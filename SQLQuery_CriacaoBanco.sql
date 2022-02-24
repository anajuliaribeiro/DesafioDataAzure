-- Criação da dabase do banco 

create database banco_transacao
use banco_transacao

-- Criacao da tabela de Clientes
create table Cliente (
id int not null primary key,
nome varchar(255) not null,
email varchar(255),

);

create table Telefone (
id_telefone int not null identity(1,1) primary key ,
cliente_id int not null,
data_de_cadastro datetime,
pais_telefone varchar(5),
ddd_telefone varchar(5),
telefone varchar(10)
);

--Criacao da tabela de Transa��es-IN  

create table Transacoes_in (
id int not null primary key, 
cliente_id int not null, 
valor float, 
data_transacao_in datetime not null
);

-- Criacao da tabela de Transa��es-OUT

create table Transacoes_out (
id int not null primary key, 
cliente_id int not null, 
valor float, 
data_transacao_out datetime not null
);
