SELECT *FROM PESSOA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_pessoa.PNG)

SELECT *FROM ALUNO LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_aluno.PNG)

SELECT *FROM PROFESSOR LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_professor.PNG)

SELECT *FROM VENDEDOR LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_vendedor.PNG)

SELECT *FROM SERVICO LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_servico.PNG)

SELECT *FROM GUARDERIA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_guarderia.PNG)

SELECT *FROM ALUGUEL LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_aluguel.PNG)

SELECT *FROM AULA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_aula.PNG)

SELECT *FROM DETALHE_GUARDERIA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_detalhe_guarderia.PNG)

SELECT *FROM DETALHE_ALUGUEL LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_detalhe_aluguel.PNG)

SELECT *FROM DETALHE_AULA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_detalhe_aula.PNG)

SELECT *FROM ITEM LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_item.PNG)

SELECT *FROM PRANCHA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_prancha.PNG)

SELECT *FROM AULA_MARCADA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_aula_marcada.PNG)

SELECT *FROM TIPO_PRANCHA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_tipo_prancha.PNG)


### 3.5.3	SELECT DAS VISÕES COM PRIMEIROS 10 REGISTROS<br>

select *from dados_guarderia;
### 3.5.4	LISTA DE CODIGOS DAS FUNÇÕES, ASSERÇOES E TRIGGERS<br>

INSERT INTO GUARDERIA (data,valor,desconto,id_vendedor,id_aluno,vencimento) VALUES ('2017-05-28',30,-5,41404,55862,'2017-06-28');

INSERT INTO GUARDERIA (data,valor,desconto,id_vendedor,id_aluno,vencimento) VALUES ('2017-05-28',30,0,41404,55862,'2017-06-28');
select aumenta_valor_guarderia(500002, 10);
select *from guarderia where id_guarderia = 500002;

INSERT INTO GUARDERIA (data,valor,desconto,id_vendedor,id_aluno,vencimento) VALUES ('2017-05-28',30,0,41404,55862,'2017-06-28');
select reduz_valor_guarderia(500003, 10);
select *from guarderia where id_guarderia = 500003;
