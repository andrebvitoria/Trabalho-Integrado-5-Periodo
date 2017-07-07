# 1. Considerações Iniciais



### 1.1 Origem dos Dados
Os dados usados nessa analise foram gerados aleatoriamente usando a biblioteca Faker da Linguagem de Programação Python. Fora inserido lotes de 100.000 itens em cada tabela, com exceção as relacionadas diretamente a tabela serviço, nestas fora inserido lotes de 500.000. Como o subsistema de Serviços possui 3 Serviços que compartilham uma tabela no banco, fora inserido nessa tabela 500.000 itens para cada serviço. Totalizando 1.500.000 de linhas na tabela servico.

### 1.2  Algoritmos Utilizados
Para a análise do banco de dados foi usado o Orange Data Mining. Foram testados alguns recursos de análise, mas dado que os dados simulados ficaram com uma distribuição homogênea o algoritmo que obteve resultados significativos foi o Sieve Diagram. <br>
O Sieve Diagram é um método gráfico de visualização de frequências em uma tabela de contingência bidirecional. Abaixo temos um exemplo do diagrama. 

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Analise%20de%20dados%20-%20Servicos/Servicos/SieveDiagram-stamped.png?raw=true)

"A área de cada retângulo é proporcional à frequência esperada, enquanto a frequência observada é mostrada pelo número de quadrados em cada retângulo. A diferença entre a frequência observada e esperada (proporcional ao padrão Pearson residual) aparece como a densidade do sombreamento, usando cor para indicar se o desvio da independência é positivo (azul) ou negativo (vermelho)." <br>
No exemplo acima é apresentado dados quanto das pessoas que estavam no Titanic. Os campos de classificação são Sexo e Sobreviveu.
"O gráfico mostra que as duas variáveis estão altamente associadas, pois existem diferenças substanciais entre frequências observadas e esperadas em todos os quatro quadrantes. Por exemplo, e como destacado no balão, a chance de sobreviver ao acidente foi muito maior para passageiros do que o esperado."

### 1.3 Analise dos Dados
Para realizar a analise fora analisado os serviços de Aluguel e Aula, pois estes apresentavam uma maior variabilidade dos dados.
Na maioria das análises realizadas os resultados obtidos seguiram o padrão acima. Como os dados gerados possuem uma distribuição homogêneas não foi possível tirar conclusões com uma base forte. <br>
Mas em casos reais podem indicar uma propensão que se estimulada pode gerar resultados positivos.
A imagem abaixo apresenta a relação entre a altura das pranchas e o gênero que mais aluga cada altura.


![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/Analise%20de%20dados%20-%20Servicos/Servicos/Prancha%20mais%20alugada.png)

Em situações onde a variação dos dados é maior a utilização de ferramentas que apontam determinado comportamento e preferencias dos clientes se faz proveitosa por mostrar informações que podem ser usadas como base para investimento de recursos. <br>

Em uma segunda análise foi feita uma filtragem inicial e uma preparação dos dados. Visto que o software usado teve problemas em reconhecer datas. Dificultando a análise.
A Imagem a seguir apresenta a relação entre faixa etária e os tipos de pranchas mais alugados.

![](https://raw.githubusercontent.com/andrebvitoria/Trabalho-Integrado-5-Periodo/master/Banco%20de%20dados/Analise%20de%20dados%20-%20Servicos/Servicos/Idade%20Aluno%20x%20Prancha%20Alugada.png)

Nesse caso foi possível observar determinados comportamentos. Por exemplo: <br>
 * Alunos com 35 anos ou mais quase não alugam pranchas Longboard, tendo uma maior tendência a alugar Performance. 
 * Alunos entre 23.5 e 35.5 tendem a alugar mais Longboard e Mini Malibu e menos Performance e Retro Fish.
 * Alunos entre 11.5 e 23.5 tendem a alugar mais Gun e menos Mini Malibu e Shortboard.
 * Alunos com menos de 11.5 alugam mais Shortboard e Performance e menos Gun e Evolution.

# 2 Considerações Finais
Dado a natureza dos dados, essas informações podem ser consideradas descartáveis, mas em uma situação real, a importância de ter esse tipo de informação é muito alta, visto que elas podem dar base para a tomada de decisão que podem influenciar todo um negócio. <br>
