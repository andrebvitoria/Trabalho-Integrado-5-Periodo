from behave import *
from loja.models import *


@given('Eu escolho estou na {url}')
def step_impl(context, url: str):
    br = context.browser
    br.visit(context.server_url + url)


@when('eu {adiciono} uma {categoria}')
def step_impl(context, adiciono: str, categoria: str):
	
   
	context.cate = categoria
	context.c = Categoria.objects.create(descricao=categoria)



@then('eu volto para a pagina {saida}')
def step_impl(context, saida: str):
    br = context.browser
    assert ( context.cate == context.c.descricao)
    br.visit(context.server_url + saida)
