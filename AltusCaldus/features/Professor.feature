Feature: Cadastrar Professor


    Scenario Outline: Cadastro com dados validos

        Given Estou na <url>
        When Informo o <nome>, <genero>, <data_nascimento>, <cpf>, <email>, <telefone>, <celular>, <emergencia>
        Then Eu sou direcionado para <url_saida>

    Examples:
   | url | nome | genero | data_nascimento | cpf | email | telefone | celular | emergencia | url_saida |
   | /admin/servicos/professor/add/ | Nome do Professor 1 | M | 12/02/1997 | 12345678910 | prof@teste.com | 32323232 | 932323232 | 192 | /admin/servicos/professor/ |



    Scenario Outline: Cadastro com dados invalidos

      Given Estou na <url>
      When Informo ou o <nome>, ou o <genero>, ou o <data_nascimento>, ou o <cpf>, ou o <email>, ou o <telefone>, ou o <celular>, ou o <emergencia> errado
      Then Eu sou direcionado para <url_saida>

    Examples:
   | url | nome | genero | data_nascimento | cpf | email | telefone | celular | emergencia | url_saida |
   | /admin/servicos/professor/add/ | Nome do Professor 2 | M | 12/02/1997 | 12345678910 | prof | 32323232 | 932323232 | 192 | /admin/servicos/professor/add/ |
   | /admin/servicos/professor/add/ | Nome do Professor 3 | M | 12h32 | 12345678910 | prof@teste.com | 32323232 | 932323232 | 192 | /admin/servicos/professor/add/ |