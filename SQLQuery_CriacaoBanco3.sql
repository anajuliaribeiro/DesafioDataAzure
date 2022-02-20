-- Criação da dabase do banco 

create database banco_transacao;
use banco_transacao;

--drop table Transacoes_in;
--drop table Transacoes_out;
--drop table Cliente;

-- Criacao da tabela de Clientes
create table Cliente (
id int not null primary key,
nome varchar(255) not null,
email varchar(255),
data_de_cadastro datetime,
telefone varchar(30),
);



--Criacao da tabela de Transações-IN  

create table Transacoes_in (
id int not null primary key, 
cliente_id int not null, 
valor float, 
data_transacao_in datetime not null,
--CONSTRAINT FK_Transacoes_in_Cliente FOREIGN KEY (cliente_id)
       -- REFERENCES Cliente (id)
       -- ON DELETE CASCADE
       -- ON UPDATE CASCADE
);



-- Criacao da tabela de Transações-OUT

create table Transacoes_out (
id int not null primary key, 
cliente_id int not null, 
valor float, 
data_transacao_out datetime not null,
--CONSTRAINT FK_Transacoes_out_Cliente FOREIGN KEY (cliente_id)
       -- REFERENCES Cliente (id)
       -- ON DELETE CASCADE
       -- ON UPDATE CASCADE
);


select * from Cliente;
select *from Transacoes_out;
select *from Transacoes_in;

