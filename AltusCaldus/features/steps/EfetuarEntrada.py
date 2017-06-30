from behave import *
from django.contrib.auth.models import User
from loja.models import *


@Given('Estou realizando uma entrada')
def given_url(context):
    pass

@when('Informo o {produto}, {valor} e {quantidade}')
def _impl(context, produto: str, valor: int, quantidade: int):

	br = context.browser

	context.categoria = Categoria.objects.create(descricao='acessorio')
	context.produto = Produto.objects.create(imagem=None, nome=produto, descricao='ahsuahs', qtd=3, categoria=context.categoria, preco=2.0, valor_custo=0.0)
	context.entrada = Entrada.objects.create()
	context.item1 = ItemEntrada.objects.create(entrada = context.entrada, produto= context.produto, valor= valor, quantidade=quantidade)



@then('O total e {total}')
def _impl(context, total:str):
    
    assert (total == context.entrada._total())
    
