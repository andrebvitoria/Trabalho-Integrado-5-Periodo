-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE entrada (
data VARCHAR(10),
id VARCHAR(10) PRIMARY KEY,
funcionario VARCHAR(10),
total VARCHAR(10)
);

CREATE TABLE Itens_Movimento (
desconto float(10),
valor float(10),
id serial PRIMARY KEY,
quantidade VARCHAR(10),
FOREIGN KEY(id) REFERENCES entrada (id)
);

CREATE TABLE Produto (
nome varchar(100),
custo float(10),
id serial PRIMARY KEY,
venda float(10)
);

CREATE TABLE Estoque (
aquisicao serial,
quantidade VARCHAR(10),
validade date,
id serial,
FOREIGN KEY(id) REFERENCES Produto (id)
);

CREATE TABLE Historico (
data date,
id_historico serial PRIMARY KEY,
movimento varchar(20),
id serial,
FOREIGN KEY(id) REFERENCES Produto (id)
);

CREATE TABLE Grupo (
desconto float(10),
lucro float(10),
nome varchar(100),
id serial PRIMARY KEY
);

CREATE TABLE Venda (
data date,
id serial PRIMARY KEY,
total VARCHAR(10),
vendedor VARCHAR(10),
desconto VARCHAR(10),
);

CREATE TABLE Funcionario (
cpf varchar(20),
nome varchar(100),
id serial PRIMARY KEY,
funcao varchar(50)
);

CREATE TABLE Aula (
id VARCHAR(10) PRIMARY KEY,
data VARCHAR(10),
tipo_aula VARCHAR(10)
);

CREATE TABLE aluno (
id serial PRIMARY KEY,
nome varchar(50),
cpf varchar(20),
ranking float(10)
);

CREATE TABLE esta (
id serial,
FOREIGN KEY(id) REFERENCES Grupo (id),
FOREIGN KEY(id) REFERENCES Produto (id)
);

CREATE TABLE senhoreia (
id serial,
FOREIGN KEY(id) REFERENCES Aula (id),
FOREIGN KEY(id) REFERENCES Funcionario (id)
);

CREATE TABLE faz (
id VARCHAR(10),
FOREIGN KEY(id) REFERENCES aluno (id),
FOREIGN KEY(id) REFERENCES Aula (id)
);

ALTER TABLE Itens_Movimento ADD FOREIGN KEY(id) REFERENCES Venda (id);
ALTER TABLE Itens_Movimento ADD FOREIGN KEY(id) REFERENCES Produto (id);
ALTER TABLE Venda ADD FOREIGN KEY(id) REFERENCES Funcionario (id);
ALTER TABLE Venda ADD FOREIGN KEY(id) REFERENCES aluno (id);
