# 1. Análise Exploratória

Antes de aplicar qualquer método estatístico, é importante ter conhecimento dos dados, por isso é importante a fase de análise exploratória de dados. Nela, somos capazes de entender melhor sobre as características dos dados em questão.<br>


### 1.1 Conjunto de Dados
Os dados usados foram gerados aleatoriamente usando a linguagem de programação Python. <br>
Do banco inteiro, contendo 1500.000.000 dados tabela principal, foi realizada uma junção e depois uma view, em cima dessa junção, que trazia uma amostra com todas as características de uma só vez. 


### 1.2  Distribuição dos Dados 
Uma das primeiras coisas a se fazer, é verificar a distribuição dos dados, porque algumas técnicas estatísticas possuem restrições com relação à isso, como por exemplo, correlação de Pearson, que espera que os dados sejam normalmente distribuídos.

### Desconto
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/desconto-uniforme.png)

Podemos ver por esse histograma que, quando usamos granularidade 10 (bins=10),  que os dados estão uniformente distribuídos. <br>
Agora vejamos a distribuição se pegarmos toda a amostra. 

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/desconto-normal.png)

Veja que agora os dados seguem uma distribuição normal. Por que isso aconteceu ? <br>
Dependendo da granularidade, ou seja, do qual "detalhista" você é ao observar os seus dados, às vezes algumas características podem desaparecer, como a distribuição normal. <br>
Pense na altura de alunos. Se olharmos apenas a altura dos alunos de uma série específica, como por exemplo, 5ª série, ela seguirá uma distribuição uniforme, o que faz sentido, pois eles estão quase na mesma faixa de altura. Agora imagine a altura de todos os alunos da escola que tem ensino fundamental e médio; ela provavelmente seguirá uma distribuição normal, pois temos alunos mais baixos (das séries iniciais), alunos altos (ensino médio) e os alunos com que estão nas séries do meio, que são a maioria e possuem uma faixa parecida. <br>

O mesmo acontece com as variáveis seguites.

### Idade
#### Uniforme
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/idade-uniforme.png)

#### Normal
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/idade-normal.png)


Para a variável **Quantidade** e **Valor Venda**, mesmo sem usar a granularidade os dados continuam resultando em uma distribuição uniforme.

### Quantidade

#### Uniforme
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/quantidade-uniforme.png)

#### Normal
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/quantidade-normal.png)



### Valor Venda
#### Uniforme
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/valor_venda-uniforme.png)

#### Normal
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/valor_venda-normal.png)



### Total Venda
#### Lei de Potência (usando bins)

O gráfico abaixo nos mostra que os dados seguem uma lei de potência, popularmente conhecida como, muitos com pouco e pouco com muito - qualquer semelhança com a situação econômica do país é mera coincidência.

Se os dados fossem reais, talvez isso nos diria que, o pessoal da escola de surfe, ganha mais vendendo pouca coisa ou mais barata, do que com muitos produtos ou produtos mais caros.

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/total_venda-lei-de-potencia.png)

#### Lei de Potência
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/total_venda-lei-de-potencia-sem-bins.png)


### 1.2  Possíveis Correlações

Depois da analisar a distribuição dos dados, outro passo comum é analisar possíveis correlações entre as variáveis analisadas.

#### Total Venda X Idade

Hipótese: Será que clientes mais velhos compram mais/gastam mais do que clientes mais novos ? <br>
A ferramenta que utilizamos para responder essa pergunta foi plotar os dados usando gráfico de dispersão, que ajuda muito na visualização dos dados afim de encontrar possíveis dependência lineares.

A imagem obtida foi essa:
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/total_venda-idade-zero-corr.png)


Como pode ser visto, a massa tem forma circular o que nos diz que não existe correlação linear entre idade e o preço total de uma venda.


# 2. Aplicação de Algoritmos

Dado a natureza dos dados aleatória, o algoritmo usado foi k-means, que é não supervisionado e tem a finalidade de encontrar clusters (o k é a quantidade de clusters). Seu objetivo é agrupar estes dados baseado em sua similaridades. No caso, foi escolhida de acordo com a data.

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/analise-de-dados-orange/imagens/k-means-por-data.png)

