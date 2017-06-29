Feature: Cadastrar Aluno

    
    Scenario Outline: Cadastro com dados validos

        Given Estou na <url>
        When Informo o <nome>, <genero>, <data_nascimento>, <cpf>, <email>, <telefone>, <celular>, <emergencia>
        Then Eu sou direcionado para <url_saida>
    
    Examples:
   | url | nome | genero | data_nascimento | cpf | email | telefone | celular | emergencia | url_saida |
   | /admin/servicos/aluno/add/ | Juliana Yuri| F | 12/02/1997 | 12345678910 | juju@juba.com | 32323232 | 932323232 | 192 | /admin/servicos/aluno/ |



    Scenario Outline: Cadastro com dados invalidos

      Given Estou na <url>
      When Informo ou o <nome>, ou o <genero>, ou o <data_nascimento>, ou o <cpf>, ou o <email>, ou o <telefone>, ou o <celular>, ou o <emergencia> errado
      Then Eu sou direcionado para <url_saida>

    Examples:
   | url | nome | genero | data_nascimento | cpf | email | telefone | celular | emergencia | url_saida |
   | /admin/servicos/aluno/add/ | Juliana Yuri| F | 12/02/1997 | 12345678910 | juju | 32323232 | 932323232 | 192 | /admin/servicos/aluno/add/ |
   | /admin/servicos/aluno/add/ | Juliana Yuri| F | 12h32 | 12345678910 | juju@juba.com | 32323232 | 932323232 | 192 | /admin/servicos/aluno/add/ |