CREATE OR REPLACE FUNCTION soma_item_aluguel(id_servico_param integer)
RETURNS float AS $$
 BEGIN
 RETURN sum(valor) from item_aluguel where id_servico = id_servico_param group by id_servico;
 END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION soma_item_guarderia(id_servico_param integer)
RETURNS float AS $$
 BEGIN
 RETURN sum(valor) from item_guarderia where id_servico = id_servico_param group by id_servico;
 END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION soma_item_aula(id_servico_param integer)
RETURNS float AS $$
 BEGIN
 RETURN sum(valor) from item_aula where id_servico = id_servico_param group by id_servico;
 END;
$$ LANGUAGE plpgsql;