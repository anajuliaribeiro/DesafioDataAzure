-- Cria��o da dabase do banco 

create database banco_transacao;
use banco_transacao;

/*
drop table Transacoes_in;
drop table Transacoes_out;
drop table Fraudes;
drop table Telefones;
drop table Clientes;
*/
-- Criacao da tabela de Clientes

create table Clientes (
id int not null primary key,
nome varchar(255) not null,
email varchar(255),
data_de_cadastro datetime
);

--Criacao da tabela telefone

create table Telefones(
id int not null identity(1,1) primary key,
cliente_id int not null,
cod_pais varchar(5),
ddd varchar(3),
numero_telefone varchar(20)
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

-- Criacao da tabela de Fraudes

create table Fraudes(
id int not null identity(1,1) primary key, 
id_transacao int not null,
tipo_transacao char(3) 
);



select * from Clientes;

select *from Transacoes_out;
select *from Transacoes_in;
select * from Telefones;


