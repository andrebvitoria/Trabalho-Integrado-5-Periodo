
create function aumenta_valor_produto(id integer, percent float)
return void as'
    update loja_produto set valor_venda = valor_venda*(1.0+percent/100.0)
    where nome = nome_produto
'language sql;

##############################divisão##############################

create function reduz_valor_produto(id integer, percent float)
return void as'
    update loja_produto set valor_venda = valor_venda*(1.0-percent/100.0)
    where nome = nome_produto
'language sql;

