create function reduz_valor_aluguel(id_aluno_param int, percent float)
returns void as'
    update aluguel set valor = valor*(1.0-percent/100.0)
    where id_aluno = id_aluno_param;
'language sql;

create function reduz_valor_guarderia(id_guarderia_param int, percent float)
returns void as'
    update guarderia set valor = valor*(1.0-percent/100.0)
    where id_guarderia = id_guarderia_param;
'language sql;

create function reduz_valor_aula(id_aula_param int, percent float)
returns void as'
    update aula set valor = valor*(1.0-percent/100.0)
    where id_aula = id_aula_param;
'language sql;