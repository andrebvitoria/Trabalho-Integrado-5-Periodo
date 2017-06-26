Feature: Efetuar Venda

    Scenario Outline: venda sem desconto

        Given Estou na <url>
        When Informo o <cliente>, <vendedor>, <desconto>, <valor_pago>, <url2>
        Then Eu sou direcionado para <url_saida>
    
    Examples: Aqui
	   | url                    | cliente                                        | vendedor         | desconto | valor_pago | url_saida          | url2 |
	   | /admin/loja/venda/add/ | /admin/loja/cliente/add/?_to_field=id&_popup=1 | test             | 0        | 10.0      | /admin/loja/venda/ | /admin/loja/venda/add/ |