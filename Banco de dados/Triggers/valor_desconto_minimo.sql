CREATE FUNCTION valor_desconto_minimo_aluguel() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT desconto from aluguel
	       where desconto < 0)
THEN
RAISE EXCEPTION ''Erro: O Valor do desconto deve ser maior que zero '';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorDescontoAluguel
AFTER INSERT OR UPDATE OF desconto ON aluguel
FOR EACH ROW
EXECUTE PROCEDURE valor_desconto_minimo_aluguel();

/* ------------------------- divisão -------------------------  */ 

CREATE FUNCTION valor_desconto_minimo_guarderia() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT desconto from guarderia
	       where desconto < 0)
THEN
RAISE EXCEPTION ''Erro: O Valor do desconto deve ser maior que zero '';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorDescontoGuarderia
AFTER INSERT OR UPDATE OF desconto ON guarderia
FOR EACH ROW
EXECUTE PROCEDURE valor_desconto_minimo_guarderia();

/* ------------------------- divisão -------------------------  */ 

CREATE FUNCTION valor_desconto_minimo_aula() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT desconto from aula
	       where desconto < 0)
THEN
RAISE EXCEPTION ''Erro: O Valor do desconto deve ser maior que zero '';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorDescontoAula
AFTER INSERT OR UPDATE OF desconto ON aula
FOR EACH ROW
EXECUTE PROCEDURE valor_desconto_minimo_aula();