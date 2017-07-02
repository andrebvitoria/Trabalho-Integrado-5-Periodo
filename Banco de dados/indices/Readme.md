**TABELA DE INDICES**

NOME| 
 TABELA| 
 COLUNA|
  | --- | --- | --- |
 ID_VENDA| ITEM_VENDA | ID_VENDA |
 ID_PRODUTO| ITEM_VENDA | ID_PRODUTO |
 ID_PRODUTO| ITEM_ENTRADA | ID_PRODUTO |
 ID_ENTRADA| ITEM_ENTRADA | ID_ENTRADA |

<br>
 
 **Índice da tabela ITEM_VENDA:**<br>
  
 *CREATE INDEX id_venda ON item_venda USING
 BTREE (id_venda);*<br>
  
 **Hipótese Inicial:** A criação deste índice partiu da ideia que a coluna id_venda sempre será utilizada nas consultas da venda. Sendo que a tabela item_venda armazena os itens que compõem uma venda, a consulta:
 <br>
 *select id_produto, quantidade, valor_venda
 from item_venda
 inner join venda on id_venda = venda.id
 where date(data) between '2016-01-01' and '2017-12-31';*
 <br>
 será uma consulta realizada constantemente, para identificação das vendas realizada em um período
 <br> 
 **Desempenho:** O desempenho real não foi o esperado, apesar de estarmos fazendo uma atribuição *inner join venda on id_venda = venda.id* o planejador não utilizou o índice criado.
 ![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indices/item_venda_com_indice.png)<br> 
 Embora o planejador não tenha utilizado  o índice do modo que pensamos, ainda podemos “sugerir” que ele use, limitando o campo de pesquisa através do índice que criamos com a atribuição:
  <br>
 *and id_venda < 1000;*
 <br>
 **comando completo:***<br>
 *select id_produto, quantidade, valor_venda
 from item_venda
 inner join venda on id_venda = venda.id
 where date(data) between '2016-01-01' and '2017-12-31' and id_venda < 1000;*
 <br>
 
 ![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indices/item_venda_com_indice_usando.png)
 
 <br>**resultados Obtidos:**<br>
 O desempenho dos índices é proporcional ao limite que impomos.
 Ou seja, quanto mais limitado é o meu intervalo melhor é o desempenho da busca pelos índices. Podemos testar isso mudando o valor das limitações.<br>
  
  
  id_venda < X|
 SEM ÍNDICES|
 COM ÍNDICES|
 | --- | --- | --- |
 X = 100| Nested Loop (cost=0.43..2631.55 rows=1 width=13) | Nested Loop (cost=4.88..65.75 rows=1 width=13) |
 X = 1000| Nested Loop (cost=0.43..2970.15 rows=1 width=13) | Nested Loop (cost=5.45..902.51 rows=1 width=13) |
 X = 10000| Nested Loop (cost=0.43..8493.32 rows=4 width=13) | Nested Loop (cost=19.13..7416.13 rows=4 width=13)|
 X = 100000| Hash Join (cost=2626.90..42322.95 rows=42 width=13) | Hash Join (cost=1305.75..41001.79 rows=42 width=13)|
 <br> 
 Assim, podemos concluir que o desempenho do índice criado foi bastante satisfatório melhorando consideravelmente o desempenho de uma busca por um intervalo específico de dados.<br>
 Gráfico Sem Índices:<br>
 
 ![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indices/item_venda_sem_indice_grafico.png)
 
 <br>
 Gráfico Com Índices:<br>
 
 ![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indices/item_venda_com_indice_grafico.png)
 
 <br>
