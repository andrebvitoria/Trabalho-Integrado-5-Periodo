from behave import *
from django.contrib.auth.models import User
from servicos.models import *


@Given ('realizei uma guarderia no valor de {v1} e outra no valor de {v2}')
def and_guarderia(context, v1: float, v2: float):
    context.aluno = Aluno.objects.create(genero='M', cpf='12344', nome='juliana kanezaki', celular='3234545',
                                         emergencia='65767',
                                         email='juliana@gmail.com', telefone='3243546', data_nascimento='1998-12-09')
    context.item = Item.objects.create(nome='prancha', descricao='azul')
    context.g = Guarderia.objects.create(cliente=context.aluno, vendedor=context.vendedor, data='2017-05-25', vencimento='2017-05-25', desconto=0)
    context.det1 = ItemGuarderia.objects.create(item=context.item, valor=50, guarderia=context.g)
    context.det2 = ItemGuarderia.objects.create(item=context.item, valor=30, guarderia=context.g)


@When ('dei um desconto de {desconto}')
def when_desconto(context, desconto: float):
    context.g.desconto = 5

@Then ('o valor total eh de {vTotal}')
def then_vTotal(context, vTotal: str):
    assert (vTotal == context.g.valor_total())
