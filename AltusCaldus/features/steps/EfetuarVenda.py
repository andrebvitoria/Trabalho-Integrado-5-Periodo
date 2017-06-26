from behave import *
from django.contrib.auth.models import User



@Given('Estou na {url}')
def given_url(context, url: str):
    User.objects.create_superuser(username='test', email='foo@bar', password='test')

    br = context.browser
    br.visit(context.base_url + '/admin/')
    br.fill('username', 'test')
    br.fill('password', 'test')
    br.find_by_css('.submit-row input').first.click()
    br.visit(context.base_url + url)


@when('Informo o {cliente}, {vendedor}, {desconto}, {valor_pago}, {url2}')
def step_impl(context, cliente:str, vendedor: str, desconto: float, valor_pago: float, url2: str):

	br = context.browser

	br.visit(context.base_url + cliente)

	br.fill('nome', 'Fulano Cliente2')

	br.find_by_css('.submit-row input').first.click()

	br.visit(context.base_url + url2)

	br.fill('vendedor', 'test')

	form = { 'desconto': desconto, 'valor_pago': valor_pago}

	br.fill_form(form)

	br.find_by_css('.submit-row input').first.click()



@then('Eu sou direcionado para {url_saida}')
def step_impl(context, url_saida:str):
    url_atual = context.browser.url
    assert (url_atual == (context.base_url + url_saida))
    
