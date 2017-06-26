CREATE VIEW dados_camisa AS 
SELECT nome, valor_venda, quantidade, categoria.descricao AS nome_categoria,cor.descricao AS nome_cor, tamanho.descricao AS nome_tamanho FROM camisa
INNER JOIN categoria ON camisa.id_categoria = categoria.id
INNER JOIN tipo_camisa ON camisa.id_tipo_camisa = tipo_camisa.id
INNER JOIN cor ON camisa.id_cor = cor.id
INNER JOIN tamanho ON camisa.id_tamanho = tamanho.id

CREATE VIEW dados_prancha AS 
SELECT nome, valor_venda, quantidade, litragem, altura, categoria.descricao AS nome_categoria, tipo_prancha.descricao AS tipo_da_prancha FROM prancha
INNER JOIN categoria ON prancha.id_categoria = categoria.id
INNER JOIN tipo_prancha ON prancha.id_tipo_prancha = tipo_prancha.id;

CREATE VIEW dados_venda AS 
SELECT venda.data, desconto, nome, idade FROM venda 
INNER JOIN cliente ON venda.id_cliente = cliente.id;



