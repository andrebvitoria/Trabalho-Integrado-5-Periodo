Feature: Efetuar Venda

    Scenario Outline: venda sem desconto

        Given Estou na <url>
        When informo os produtos e o <cliente>, <vendedor>, <desconto>, <valor_pago> 
        Then <total> eh o total
    
    Examples: Aqui
	   | url                    | cliente                                        | vendedor         | desconto | valor_pago | total          | 
	   | /admin/loja/venda/add/ | joaozinho | test             | 0        | 10.0      | R$ 6,00 | 