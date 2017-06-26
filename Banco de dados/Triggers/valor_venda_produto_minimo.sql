/*IMPÕE QUE O VALOR DOS PRODUTOS DEVE SER MAIOR QUE ZERO*/
CREATE FUNCTION valor_venda_cantina_minimo() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT valor_venda from cantina
	       where valor_venda <= 0)
THEN
RAISE EXCEPTION ''Erro: O Valor de venda deve ser maior que zero '';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorVendaCantina
AFTER INSERT OR UPDATE OF valor_venda ON cantina
FOR EACH ROW
EXECUTE PROCEDURE valor_venda_cantina_minimo();

/*----------------------- divisão -------------------------*/

CREATE FUNCTION valor_venda_prancha_minimo() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT valor_venda from prancha
	       where valor_venda <= 0)
THEN
RAISE EXCEPTION ''Erro: O Valor de venda deve ser maior que zero '';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorVendaPrancha
AFTER INSERT OR UPDATE OF valor_venda ON prancha
FOR EACH ROW
EXECUTE PROCEDURE valor_venda_prancha_minimo();
/*----------------------- divisão -------------------------*/

CREATE FUNCTION valor_venda_camisa_minimo() RETURNS TRIGGER AS '
BEGIN
IF EXISTS (SELECT valor_venda from camisa
	       where valor_venda <= 0)
THEN
RAISE EXCEPTION ''Erro: O Valor de venda deve ser maior que zero '';
END IF;
RETURN NULL;
END
'
LANGUAGE plpgsql;
CREATE TRIGGER checkValorVendaCamisa
AFTER INSERT OR UPDATE OF valor_venda ON camisa
FOR EACH ROW
EXECUTE PROCEDURE valor_venda_camisa_minimo();