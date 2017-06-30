Feature: Login

Scenario Outline: Login com informacoes validas
	Given Eu sou um usuario na tela de login do admin
	When Informo meu <login> e minha <senha>
	Then Eu sou direcionado para <url_saida>

	Examples:
		| login | senha | url_saida |
		| test |test|/admin/|

Scenario Outline: Login com informacoes invalidas
	Given Eu sou um usuario na tela de login do admin
	When Informo meu <login> e minha <senha>
	Then Eu sou direcionado para <url_saida>


	Examples:
		| login      | senha              | url_saida                  |
		| fabiano    | minhasenhasecreta2 | /admin/login/?next=/admin/ |
		| fabs       | minhasenhasecreta  |/admin/login/?next=/admin/  |