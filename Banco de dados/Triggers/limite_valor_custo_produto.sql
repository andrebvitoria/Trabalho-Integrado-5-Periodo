/*IMPÕE QUE O VALOR DE VENDA DOS PRODUTOS DEVE SER MAIOR QUE O VALOR DE CUSTO*/

CREATE FUNCTION limite_valor_custo_cantina() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT valor_custo, valor_venda from cantina
	where valor_venda < valor_custo)
THEN
RAISE EXCEPTION ''Erro: Valor de custo maior que o valor de venda'';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorCustoCantina
AFTER INSERT OR UPDATE OF valor_custo, valor_venda ON cantina
FOR EACH ROW
EXECUTE PROCEDURE limite_valor_custo_cantina();

/*----------------------- divisão -------------------------*/

CREATE FUNCTION limite_valor_custo_camisa() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT valor_custo, valor_venda from camisa
	where valor_venda < valor_custo)
THEN
RAISE EXCEPTION ''Erro: Valor de custo maior que o valor de venda'';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorCustoCamisa
AFTER INSERT OR UPDATE OF valor_custo, valor_venda ON camisa
FOR EACH ROW
EXECUTE PROCEDURE limite_valor_custo_camisa();

/*----------------------- divisão -------------------------*/

CREATE FUNCTION limite_valor_custo_prancha() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT valor_custo, valor_venda from prancha
	where valor_venda < valor_custo)
THEN
RAISE EXCEPTION ''Erro: Valor de custo maior que o valor de venda'';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorCustoPrancha
AFTER INSERT OR UPDATE OF valor_custo, valor_venda ON prancha
FOR EACH ROW
EXECUTE PROCEDURE limite_valor_custo_prancha();