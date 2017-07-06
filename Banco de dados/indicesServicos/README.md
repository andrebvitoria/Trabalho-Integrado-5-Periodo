## Primeiro teste

SELECT nome, data, desconto from servico
inner join aluno on aluno.id_pessoa = servico.id_aluno
where nome like '%J';

### Resultatos sem indices

### Resultatos com indices
CREATE INDEX nome_aluno ON aluno USING BTREE (nome);


CREATE INDEX id_aluno ON aluno USING BTREE (id_pessoa);

## Segundo teste

select valor, age(data_nascimento) as idade, altura, nome, data from item_aluguel
inner join servico on servico.id_servico =  item_aluguel.id_servico
inner join aluno on aluno.id_pessoa = servico.id_aluno
inner join prancha on prancha.id_prancha = item_aluguel.id_prancha
where item_aluguel.id_servico > 100000;

### Resultatos sem indices

### Resultatos com indices
CREATE INDEX id_aluno ON aluno USING BTREE (id_pessoa);
CREATE INDEX id_servico ON servico USING BTREE (id_servico);


## Terceiro teste

select nome, valor, vencimento from item_guarderia 
inner join guarderia on guarderia.id_servico = item_guarderia.id_guarderia
inner join item on item.id_item = item_guarderia.id_item
where item.id_item > 1000;

### Resultatos sem indices

### Resultatos com indices
CREATE INDEX id_item2 ON item_guarderia USING BTREE (id_item);


