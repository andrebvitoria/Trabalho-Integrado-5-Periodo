## Procedimento de Geração de dados Simulados

### Dados Serviço

1° Execute os 3 códigos de Geração de dados.<br><br>

2º Crie um banco e execute o script de criação das tabelas.<br>
* ATENÇÃO: É recomendado o uso de um banco limpo, sem nenhum dado dentro das tabelas, pois pode interferir no resultado da inserção. <br>

3° No pentaho coloque os respectivos csv's em suas entradas e execute os processos em 4 etapas:<br>
* 1° Execute a 1° fileira ela não possui dependências.<br>
* 2° Execute a 2° fileira ela depende da 1°.<br>
* 3° Execute a 3° fileira ela depende da 1° e da 2°.<br>
* 4º Execute a Ultima fileira, ela depende das anteriores. <br>


### Dados Loja

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
