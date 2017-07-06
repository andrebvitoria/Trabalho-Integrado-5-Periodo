### 3.5.2	SELECT DAS TABELAS COM PRIMEIROS 10 REGISTROS INSERIDOS
 
 
     SELECT * FROM PESSOA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/pessoa.PNG)

    SELECT * FROM ALUNO LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/aluno.PNG)

    SELECT * FROM PROFESSOR LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/professor.PNG)

    SELECT * FROM VENDEDOR LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/vendedor.PNG)

    SELECT * FROM SERVICO LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/servico.PNG)

    SELECT * FROM GUARDERIA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/guarderia.PNG)

    SELECT * FROM ITEM_GUARDERIA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/item_guarderia.PNG)

    SELECT * FROM ITEM_ALUGUEL LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/item_aluguel.PNG)

    SELECT * FROM ITEM_AULA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/item_aula.PNG)

    SELECT * FROM ITEM LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/item.PNG)

    SELECT * FROM PRANCHA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/prancha.PNG)

    SELECT * FROM AULA_MARCADA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/aula_marcada.PNG)

    SELECT * FROM TIPO_PRANCHA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/contato.PNG)

    SELECT * FROM TIPO_CONTATO LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/select_tipo_prancha.PNG)

    SELECT * FROM CONTATO_ALUNO LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/contato_aluno.PNG)

    SELECT * FROM CONTATO_VENDEDOR LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/contato_vendedor.PNG)

    SELECT * FROM CONTATO_PROFESSOR LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/contato_professor.PNG)

    SELECT * FROM TIPO_PRANCHA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/select/tipo_prancha.PNG)


    SELECT * FROM TIPO_CAMISA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/loja/select_camisa.png)


    SELECT * FROM CANTINA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/loja/select_cantina.png)


    SELECT * FROM VENDA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/loja/select_venda.png)


    SELECT * FROM PRODUTO LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/loja/select_produto_2.png)


    SELECT * FROM ENTRADA LIMIT 10;
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/loja/select_entrada.png)


### 3.5.3	SELECT DAS VISÕES COM PRIMEIROS 10 REGISTROS<br>

#### Visão 1
 - Essa view serve para visualizar os dados de servicos (aluguel, aula e guarderia) com todos os dados, no lugar dos ID's é mostrado o nome da pessoa. <br>
 - View:  [Dados Serviços](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Views/dados_servico.sql)<br>
 
 `SELECT * FROM DADOS_GUARDERIA;                                                               `
    
![Dados Guarderia](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/view_dados_servico.PNG)<br>


#### Visão 2
 - Essa view serve para visualizar os dados da loja (camisa, prancha e venda) com todos os dados, no lugar dos ID's é mostrado o nome da categoria, cliente, tipo do produto e etc . <br>
 - View:  [Dados Loja](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Views/dados_loja.sql)<br>
 
 `SELECT * FROM DADOS_CAMISA;                                                                 `
    
![Dados Camisa](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/loja/view_dados_camisa.png)<br>

#### Visão 3
 - Essa view serve para visualizar os dados de contato de pessoa <br>
 - View:  [view_contato_pessoa](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Views/view_contato_pessoa.sql)<br>
 
 `SELECT * FROM view_contato_aluno;                                                                 `
    
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/view_contato.PNG)<br>



### 3.5.4	LISTA DE CODIGOS DAS FUNÇÕES, ASSERÇOES E TRIGGERS<br>

#### Função 1
 - Essa função tem o objetivo de calcular o valor total de um seriço
 - Função: [calcula_valor_servico](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Functions/calcula_valor_servico.sql)<br>
 
`select *from item_aluguel where id_servico = 2000001 ;`<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/fun%C3%A7%C3%A3o/calcula_total1.PNG)<br>

`select soma_item_aluguel (2000001);`<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/fun%C3%A7%C3%A3o/calcula_total2.PNG)<br>


#### Função 2
 - Essa função tem o objetivo de calcular quantos dias faltam para uma guarderia expirar.
 - Função: [calcula_validade_guarderia](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Functions/calcula_validade_guarderia.sql)<br>
 
`select *from guarderia where id_servico = 1000001 ;`<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/fun%C3%A7%C3%A3o/vencimento_guarderia1.PNG)<br>

`select validade_guarderia(1000001);` <br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/Servi%C3%A7os/fun%C3%A7%C3%A3o/vencimento_guarderia2.PNG)<br>

#### Trigger 1
 - Essa trigger impõe que o desconte deve ser igual ou maior que zero.
 - Trigger: [valor_desconto_minimo](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Triggers/valor_desconto_minimo.sql)<br>
 
`INSERT INTO GUARDERIA (data,valor,desconto,id_vendedor,id_aluno,vencimento) VALUES ('2017-05-28',30,-5,41404,55862,'2017-06-28');`

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/imagens/trigger_desconto_minimo.PNG)<br>

#### Trigger 2
 - Essa trigger impõe que o valor de venda dos produtos deve ser maior que o valor de custo.
 - Trigger: [limite_valor_custo_produto](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Triggers/limite_valor_custo_produto.sql)<br>
 
 'INSERT INTO CAMISA VALUES('CAMISA MOULLIN',100,1,1,1,1,10);'

#### Trigger 3
 - Essa trigger impõe que o valor dos produtos deve ser maior que zero.
 - Trigger: [valor_venda_produto_minimo](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Triggers/valor_venda_produto_minimo.sql)<br>
 
 'INSERT INTO CAMISA VALUES('CAMISA MOULLIN',0,1,1,1,1,0);'

