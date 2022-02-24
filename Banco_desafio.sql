

-- Criacao da dabase do banco 

create database banco_transacao;
use banco_transacao;
go


-- Criacao da tabela de Clientes

create table Clientes (
id int not null primary key,
nome varchar(255) not null,
email varchar(255),
data_de_cadastro datetime
);
go

--Criacao da tabela telefone

create table Telefones(
id int not null identity(1,1) primary key,
cliente_id int not null,
cod_pais varchar(5),
ddd varchar(3),
numero_telefone varchar(20)
);
go

-- Criacao da constraint da foreign key 

alter table Telefones add foreign key (cliente_id) references Clientes(id)
go

--Criacao da tabela de Transacoes-IN  

create table Transacoes_in (
id int not null primary key, 
cliente_id int not null, 
valor float, 
data_transacao_in datetime not null
);
go

-- Criacao da constraint da foreign key 

alter table Transacoes_in add foreign key (cliente_id) references Clientes(id)
go

-- Criacao da tabela de Transacoes-OUT

create table Transacoes_out (
id int not null primary key, 
cliente_id int not null, 
valor float, 
data_transacao_out datetime not null
);
go

-- Criacao da constraint da foreign key 

alter table Transacoes_out add foreign key (cliente_id) references Clientes(id)
go

-- Criacao da tabela de Fraudes

create table Fraudes (
id int not null identity(1,1) primary key, 
id_transacao int not null,
tipo_transacao char(3) 
);
go 

create table Fraudes_in (
id int not null identity(1,1) primary key, 
id_transacao int not null,
);
go 

-- Criacao da constraint da foreign key 
alter table Fraudes_in add foreign key (id_transacao) references Transacoes_in(id)
go


create table Fraudes_out (
id int not null identity(1,1) primary key, 
id_transacao int not null,
);
go

-- Criacao da constraint da foreign key 
alter table Fraudes_out add foreign key (id_transacao) references Transacoes_out(id)
go



-- INSERIR AUTOMATICAMENTE DADOS NA TABELA UNIFICADA
  CREATE TRIGGER TRG_FRAUDES_IN ON Fraudes_in
	FOR INSERT
AS BEGIN 
DECLARE @id int;
	select @id = id_transacao from INSERTED ;
	INSERT INTO Fraudes (id_transacao, tipo_transacao) 
	VALUES ( @id, 'IN')
END

go 

  CREATE TRIGGER TRG_FRAUDES_OUT ON Fraudes_out
	FOR INSERT
AS BEGIN 
DECLARE @id int;
	select @id = id_transacao from INSERTED ;
	INSERT INTO Fraudes (id_transacao, tipo_transacao) 
	VALUES ( @id, 'OUT')
END


