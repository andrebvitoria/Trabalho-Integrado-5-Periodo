### Procedimento de Geração de dados Simulados

### DADOS SERVIÇO

1° Execute os 2 códigos de Geração de dados.<br><br>

2° Verifique a existência de datas em 02-29 e substitua por outra data <br>
	(aparentemente a biblioteca faker não verifica a ocorrência correta de anos bissextos)<br><br>
	
3° No pentaho coloque os respectivos csv's em suas entradas e execute os processos em 3 etapas:<br>
	1° Execute a 1° fileira ela não possui dependências.<br>
	2° Execute a 2° fileira ela depende da 1°.<br>
	3° Execute a 3° fileira ela depende da 1° e da 2°.<br>



### DADOS LOJA

1) Execute o código gera-entrada.py para gerar os dados de entrada. <br>
   Execute todas as transformações para enviar ao banco de dados.

2) Execute o código gera-produto.py para gerar os dados de produto. <br>
   Execute todas as transformações para enviar ao banco de dados.

3) Execute o código gera-cliente.py para gerar os dados de cliente. <br>
   Execute todas as transformações para enviar ao banco de dados.
 
4) Execute o código gera-venda.py para gerar os dados de venda.<br>
   Execute todas as transformações para enviar ao banco de dados.
	1. Execute a transformação de VENDA antes do ITEM_VENDA.

5) Execute o código gera-item-entrada.py para gerar os dados de itens de entrada. <br>
   Execute todas as transformações para enviar ao banco de dados.




