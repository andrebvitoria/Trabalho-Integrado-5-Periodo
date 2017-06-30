Feature: showing off behave

  Scenario Outline: run a simple test
     Given Eu escolho estou na <url>
     When eu <adiciono> uma <categoria>
     Then eu volto para a pagina <saida>


     Examples: alguns
     | url  | adiciono | categoria| saida  |
     |/admin/loja/categoria/| /admin/loja/categoria/add/ | prancha | /admin/loja/categoria/ |