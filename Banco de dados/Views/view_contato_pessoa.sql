CREATE VIEW view_contato_aluno AS
SELECT  V.nome as aluno, VC.contato_pessoa, TC.descricao
FROM contato_aluno AS VC
INNER JOIN aluno AS V ON VC.id_pessoa = V.id_pessoa
INNER JOIN tipo_contato AS TC ON TC.id_tipo_contato = VC.id_tipo_contato;


CREATE VIEW view_contato_professor AS
SELECT  V.nome as professor, VC.contato_pessoa, TC.descricao
FROM contato_professor AS VC
INNER JOIN professor AS V ON VC.id_pessoa = V.id_pessoa
INNER JOIN tipo_contato AS TC ON TC.id_tipo_contato = VC.id_tipo_contato;



CREATE VIEW view_contato_vendedor AS
SELECT  V.nome as vendedor, VC.contato_pessoa, TC.descricao
FROM contato_vendedor AS VC
INNER JOIN vendedor AS V ON VC.id_pessoa = V.id_pessoa
INNER JOIN tipo_contato AS TC ON TC.id_tipo_contato = VC.id_tipo_contato;