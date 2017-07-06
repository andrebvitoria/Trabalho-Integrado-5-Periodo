## Primeiro teste

SELECT nome, data, desconto from servico <br>
inner join aluno on aluno.id_pessoa = servico.id_aluno<br>
where data_nascimento between '2018-01-01' and '2011-01-01';<br>

 - Busca um serviço pelo data de nascimento, nesse teste quis analisar como as querys se comportariam ao prorcurar um dado que não esta no banco. O Esperado é que na query sem indice o desempenho seja menor, já que ele terá que percorrer todos os registros;

### Resultatos sem indices

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/semIndiceData.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/semIndiceDataAnalise.PNG)

### Resultatos com indices
Decidemos usar um indice na tabela aluno na coluna data_nascimento. E como era de se esperar o resultado foi superior.

CREATE INDEX data_aluno ON aluno USING BTREE (data_nascimento);<br>
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/comIndiceData.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/comIndiceDataAnalise.PNG)


## Segundo teste

select valor, age(data_nascimento) as idade, altura, nome, data from item_aluguel<br>
inner join servico on servico.id_servico = item_aluguel.id_servico<br>
inner join aluno on aluno.id_pessoa = servico.id_aluno<br>
inner join prancha on prancha.id_prancha = item_aluguel.id_prancha<br>
where servico.id_servico between 2000000 and 2001555;<br>

### Resultatos sem indices

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/comIndiceServico.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/comIndiceServicoAnalise.PNG)

### Resultatos com indices
CREATE INDEX id_servico ON servico USING BTREE (id_servico);<br>

![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/semIndiceServico.PNG)
![](https://github.com/andrebvitoria/Trabalho-Integrado-5-Periodo/blob/master/Banco%20de%20dados/indicesServicos/imagens/SemmIndiceServico.PNG)



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


