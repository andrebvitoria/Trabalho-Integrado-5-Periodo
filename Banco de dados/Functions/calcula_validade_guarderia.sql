CREATE OR REPLACE FUNCTION validade_guarderia(id_guarderia_param integer)
RETURNS integer AS $$
 BEGIN
 RETURN current_date - vencimento from guarderia where id_servico = id_guarderia_param;
 END;
$$ LANGUAGE plpgsql;