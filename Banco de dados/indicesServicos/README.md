## Primeiro teste

SELECT nome, data, desconto from servico <br>
inner join aluno on aluno.id_pessoa = servico.id_aluno<br>
where nome like '%J';<br>

 - Busca um serviço pelo nome do aluno;

### Resultatos sem indices

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/semIndice1.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/semIndiceAnalise1.PNG)

### Resultatos com indices
Decidemos usar um indice na tabela pessoa na coluna nome. Visualmente não notamos nenhuma diferença na largura das setas, porem é possivel perceber que o tempo de planejamente e execução diminui mesmo sem usar indices.

CREATE INDEX nome_aluno ON aluno USING BTREE (nome);<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/comIndice1.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/comIndiceAnalise1.PNG)

Depois desse resultado decidimos colocar um outro indice, agora na tabela aluno e no campo id_pessoa. Os resultados pioraram em relação a anterior mas os indices não foram usados.

CREATE INDEX id_aluno ON aluno USING BTREE (id_pessoa);<br>

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/comIndiceAnalise12.PNG)

## Segundo teste

select valor, age(data_nascimento) as idade, altura, nome, data from item_aluguel<br>
inner join servico on servico.id_servico =  item_aluguel.id_servico<br>
inner join aluno on aluno.id_pessoa = servico.id_aluno<br>
inner join prancha on prancha.id_prancha = item_aluguel.id_prancha<br>
where item_aluguel.id_servico < 100000;<br>

### Resultatos sem indices

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/SemIndice2.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/SemIndiceAnalise2.PNG)

### Resultatos com indices
CREATE INDEX id_servico ON servico USING BTREE (id_servico);<br>

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/ComIndice2.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/ComIndiceAnalise2.PNG)



## Terceiro teste

select nome, valor, vencimento from item_guarderia <br>
inner join guarderia on guarderia.id_servico = item_guarderia.id_guarderia<br>
inner join item on item.id_item = item_guarderia.id_item<br>
where item.id_item < 1000;<br>

### Resultatos sem indices
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/SemIndice3.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/SemIndiceAnalise3.PNG)

### Resultatos com indices
CREATE INDEX id_item2 ON item_guarderia USING BTREE (id_item);<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/ComIndice3.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/ComIndiceAnalise3.PNG)


