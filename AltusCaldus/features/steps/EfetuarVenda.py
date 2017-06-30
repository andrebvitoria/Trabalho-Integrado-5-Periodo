from behave import *
from django.contrib.auth.models import User
from loja.models import *


@Given('Estou na {url}')
def given_url(context, url: str):
    pass

@when('informo os produtos e o {cliente}, {vendedor}, {desconto}, {valor_pago}')
def step_impl(context, cliente:str, vendedor: str, desconto: float, valor_pago: float):

	br = context.browser
	context.categoria = Categoria.objects.create(descricao='acessorio')

	context.cliente = Cliente.objects.create(nome=cliente)
	context.vendedor =  User.objects.create_superuser(username='test', email='foo@bar', password='admin123123')
	context.venda = Venda.objects.create(cliente=context.cliente, vendedor=context.vendedor, desconto=desconto, valor_pago=valor_pago)
	context.produto = Produto.objects.create(imagem=None, nome='strep', descricao='ahsuahs', qtd=3, categoria=context.categoria, preco=2.0, valor_custo=0.0)
	context.item1 = ItemVenda.objects.create(produto=context.produto, venda=context.venda, preco=2.0, quantidade=3)



@then('{total} eh o total')
def step_impl(context, total:str):
    
    assert (total == context.venda.Total())
    
