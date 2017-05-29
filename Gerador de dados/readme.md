Procedimento de Geração de dados Simulados

1° Execute os 2 códigos de Geração de dados.

2° Verifique a existência de datas em 02-29 e substitua por outra data 
	(aparentemente a biblioteca faker não verifica a ocorrência correta de anos bissextos)
	
3° No pentaho coloque os respectivos csv's em suas entradas e execute os processos em 3 etapas:
	1° Execute a 1° fileira ela não possui dependências.
	2° Execute a 2° fileira ela depende da 1°.
	3° Execute a 3° fileira ela depende da 1° e da 2°.
