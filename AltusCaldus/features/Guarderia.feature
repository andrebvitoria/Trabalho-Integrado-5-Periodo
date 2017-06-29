Feature: Cadastrar Aluno


    Scenario Outline: Cadastro com dados validos

        Given Estou na <url>
        And realizei uma guarderia no valor de <v1> e outra no valor de <v2>
        When dei um desconto de <desconto>
        Then o valor total eh de <vTotal>

    Examples:
   | url | v1 | v2 | desconto | vTotal |
   | /admin/servicos/guarderia/add/ | 50 | 30 | 5 | R$ 00,00 |



