CREATE VIEW dados_servico AS
SELECT A.data, A.desconto, V.nome as vendedor, C.nome as aluno 
FROM servico AS A
INNER JOIN vendedor AS V ON A.id_vendedor = V.id_pessoa
INNER JOIN aluno AS C ON A.id_aluno = C.id_pessoa;

CREATE VIEW dados_guarderia AS
SELECT A.data, A.desconto, A.vencimento, V.nome as vendedor, C.nome as aluno 
FROM guarderia AS A
INNER JOIN vendedor AS V ON A.id_vendedor = V.id_pessoa
INNER JOIN aluno AS C ON A.id_aluno = C.id_pessoa;

