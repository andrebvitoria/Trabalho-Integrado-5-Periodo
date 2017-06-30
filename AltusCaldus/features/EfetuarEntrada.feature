Feature: Efetuar Entrada

    Scenario Outline: efetuar entrada

        Given Estou realizando uma entrada
        When Informo o <produto>, <valor> e <quantidade>
        Then O total e <total>
    
    Examples: entrada
    | produto | valor | quantidade | total |          
    | strep   | 20.0  | 3          | R$ 60,00  |