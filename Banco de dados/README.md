### 3.5.2	SELECT DAS TABELAS COM PRIMEIROS 10 REGISTROS INSERIDOS
SELECT *FROM PESSOA LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_pessoa.PNG)

SELECT *FROM ALUNO LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_aluno.PNG)

SELECT *FROM PROFESSOR LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_professor.PNG)

SELECT *FROM VENDEDOR LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_vendedor.PNG)

SELECT *FROM SERVICO LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_servico.PNG)

SELECT *FROM GUARDERIA LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_guarderia.PNG)

SELECT *FROM ALUGUEL LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_aluguel.PNG)

SELECT *FROM AULA LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_aula.PNG)

SELECT *FROM DETALHE_GUARDERIA LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_detalhe_guarderia.PNG)

SELECT *FROM DETALHE_ALUGUEL LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_detalhe_aluguel.PNG)

SELECT *FROM DETALHE_AULA LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_detalhe_aula.PNG)

SELECT *FROM ITEM LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_item.PNG)

SELECT *FROM PRANCHA LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_prancha.PNG)

SELECT *FROM AULA_MARCADA LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_aula_marcada.PNG)

SELECT *FROM TIPO_PRANCHA LIMIT 10;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_tipo_prancha.PNG)


### 3.5.3	SELECT DAS VISÕES COM PRIMEIROS 10 REGISTROS<br>

#### Visão 1
 - Essa view serve para visualizar os dados de servicos (aluguel, aula e guarderia) com todos os dados, no lugar dos ID's é mostrado o nome da pessoa. <br>
 - View:  [Dados Serviços](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Views/dados_servico.sql)<br>
select *from dados_guarderia;<br>
![Dados Guarderia](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/view_dados_guarderia.PNG)<br>


### 3.5.4	LISTA DE CODIGOS DAS FUNÇÕES, ASSERÇOES E TRIGGERS<br>

#### Função 1
 - Essa função tem o objetivo de aumentar o valor do serviço informado.
 - Função: [Aumenta Valor Serviços](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Functions/aumenta_valor_servico.sql)<br>
INSERT INTO GUARDERIA (data,valor,desconto,id_vendedor,id_aluno,vencimento) VALUES ('2017-05-28',30,0,41404,55862,'2017-06-28');<br>
select aumenta_valor_guarderia(500002, 10);<br>
select *from guarderia where id_guarderia = 500002;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/function_aumenta_valor_servico.PNG)<br>


#### Função 2
 - Essa função tem o objetivo de diminuir o valor do serviço informado.
 - Função: [Reduz Valor Serviços](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Functions/reduz_valor_servico.sql)<br>
INSERT INTO GUARDERIA (data,valor,desconto,id_vendedor,id_aluno,vencimento) VALUES ('2017-05-28',30,0,41404,55862,'2017-06-28');<br>
select reduz_valor_guarderia(500003, 10);<br>
select *from guarderia where id_guarderia = 500003;<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/function_reduz_valor_servico.PNG)<br>

#### Trigger 1
 - Essa trigger impõe que o desconte deve ser igual ou maior que zero.
 - Trigger: [valor_desconto_minimo](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Triggers/valor_desconto_minimo.sql)<br>
INSERT INTO GUARDERIA (data,valor,desconto,id_vendedor,id_aluno,vencimento) VALUES ('2017-05-28',30,-5,41404,55862,'2017-06-28');<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/trigger_desconto_minimo.PNG)<br>

#### Trigger 2
 - Essa trigger impõe que o valor de venda dos produtos deve ser maior que o valor de custo.
 - Trigger: [limite_valor_custo_produto](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Triggers/limite_valor_custo_produto.sql)<br>

#### Trigger 3
 - Essa trigger impõe que o valor dos produtos deve ser maior que zero.
 - Trigger: [valor_venda_produto_minimo](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Triggers/valor_venda_produto_minimo.sql)<br>

