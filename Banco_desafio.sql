-- Criação da dabase do banco 

create database banco_transacao;
use banco_transacao;
--drop table Cliente;
--drop table Transacoes_in;
--drop table Transacoes_out;


-- Criacao da tabela de Clientes

create table Cliente (
id int not null primary key,
nome varchar(255) not null,
email varchar(255),
data_de_cadastro datetime,
fuso_horario varchar(5)
);

--Criacao da tabela telefone

create table Telefone(
id int not null identity(1,1) primary key,
cliente_id int not null,
cod_pais varchar(5),
ddd varchar(3),
numero_telefone varchar(20)
);

--Criacao da tabela de Transações-IN  

create table Transacoes_in (
id int not null primary key, 
cliente_id int not null, 
valor float, 
data_transacao_in datetime not null,
fuso_horario varchar(5)
);


-- Criacao da tabela de Transações-OUT

create table Transacoes_out (
id int not null primary key, 
cliente_id int not null, 
valor float, 
data_transacao_out datetime not null,
fuso_horario varchar(5)
);

-- Criacao da tabela Fraudes_In

create table Fraudes_in(
id int not null identity(1,1) primary key, 
id_transacao_in int not null
);

-- Criacao da tabela Fraudes_OUT

create table Fraudes_out(
id int not null identity(1,1) primary key, 
id_transacao_out int not null
);


select * from Cliente;
select *from Transacoes_out;
select *from Transacoes_in;

