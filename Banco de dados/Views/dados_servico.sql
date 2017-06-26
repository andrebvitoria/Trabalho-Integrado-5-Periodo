CREATE VIEW dados_aluguel AS 
SELECT A.data, A.valor, A.desconto, V.nome as vendedor, C.nome as aluno 
FROM aluguel AS A
INNER JOIN vendedor AS V ON A.id_vendedor = V.id_vendedor
INNER JOIN aluno AS C ON A.id_vendedor = C.id_aluno;

CREATE VIEW dados_aula AS 
SELECT A.data, A.valor, A.desconto, V.nome as vendedor, C.nome as aluno 
FROM aula AS A
INNER JOIN vendedor AS V ON A.id_vendedor = V.id_vendedor
INNER JOIN aluno AS C ON A.id_vendedor = C.id_aluno;

CREATE VIEW dados_guarderia AS 
SELECT A.data, A.vencimento, A.valor, A.desconto, V.nome as vendedor, C.nome as aluno 
FROM guarderia AS A
INNER JOIN vendedor AS V ON A.id_vendedor = V.id_vendedor
INNER JOIN aluno AS C ON A.id_vendedor = C.id_aluno;