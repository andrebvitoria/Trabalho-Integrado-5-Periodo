# 1. Considerações Iniciais



### 1.1 Origem dos Dados
Os dados usados nessa analise foram gerados aleatóriamente usando a biblioteca Faker da Linguagem de Programação Python. Fora iserido lotes de 100.000 itens em cada tabela, com exceção as realcionadas diretamente a tabela serviço, nestas fora inserido lotes de 500.000. Como o subsistema de Serviços possui 3 Serviços que compartilham uma tabela no banco, fora inserido nessa tabela 500.000 itens para cada serviço. Totalizando 1.500.000 de linhas na tabela servico.

### 1.2  Algoritmos Utilizados
Para analise do banco de dados foi usado o Orange Data Mining. Foram testado alguns recursos de analise, mas dado que os dados simulados ficaram com uma distribuição homogenea o algoritmo que obtera resultados significativos foi o Sieve Diagram. <br>
O Sieve Diagram é um metodo gráfico de visualização  de frequencias em uma tabela de contigência bidirecinal. Abaixo temos um exemplo do diagrama. 

[IMAGEM EXEMPLO]

"A area de cada retangulo é proporcional à freqüência esperada, enquanto a freqüência observada é mostrada pelo número de quadrados em cada retângulo. A diferença entre a freqüência observada e esperada (proporcional ao padrão Pearson residual) aparece como a densidade do sombreamento, usando cor para indicar se o desvio da independência é positivo (azul) ou negativo (vermelho)." <br>
No exemplo acima é apresentado dados quanto das pessoas que estavam no Titanic. Os campos de classificação são Sexo e Sobreviveu.
"O gráfico mostra que as duas variáveis estão altamente associadas, pois existem diferenças substanciais entre frequências observadas e esperadas em todos os quatro quadrantes. Por exemplo, e como destacado no balão, a chance de sobreviver ao acidente foi muito maior para passageiros do que o esperado."

### 1.3 Analise dos Dados
Para realizar a analise fora analisados os serviços de Aluguel e Aula, pois este apresentavam uma maior variabilidade dos dados.

Na maioria das analises realizadas os resultados obtidos seguiram o padrão acima. Como os dados gerados possuem uma distribuição homogêneas não foi possivel tirar conclusões com uma base forte. <br>
Mas em casos reais podem indicar uma propensão que se estimulada pode gerar resultados positivos.
A imagem abaixo apresenta a relação entre a altura das pranchas e o genero que mais aluga cada altura.

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Analise%20de%20dados%20-%20Servicos/Servicos/Prancha%20mais%20alugada.png)

Em situações onde a variação dos dados é maior a utilização de ferramentas que apontam determinado comportamento e preferecias dos clientes se faz proveitosa por mostrar informações que podem ser usadas como base para investimento de recursos. <br>

Em uma segunda analise foi feita uma filtragem incial e uma preparação dos dados. Visto que o software usado teve problemas em reconhecer datas. Dificultando a analise.
A Imagem a seguir apresenta a relação entre faixa etária e os tipos de pranchas mais alugados.

![](https://raw.githubusercontent.com/andrebvitoria/Trabalho-Integrado-5-Periodo/master/Banco%20de%20dados/Analise%20de%20dados%20-%20Servicos/Servicos/Idade%20Aluno%20x%20Prancha%20Alugada.png)

Nesse caso foi possivel observar determinados comportamentos. Por exemplo: <br>
 * Alunos com 35 anos ou mais quase não alugam pranchas Longboard, tendo uma maior tendencia a alugar Performance. 
 * Alunos entre 23.5 e 35.5 tendem a alugar mais Longboard e Mini Malibu e menos Performance e Retro Fish.
 * Alunos entre 11.5 e 23.5 tendem a alugar mais Gun e menos Mini Malibu e Shortboard.
 * Alunos com menos de 11.5 alugam mais Shortboard e Performance e menos Gun e Evolution.

Dado a natureza dos dados, essas informações podem ser consideradas descartaveis, mas em uma situação real, a importancia de ter esse tipo de informação é muito alta, visto que elas podem dar base para a tomada de decisão. <br>

