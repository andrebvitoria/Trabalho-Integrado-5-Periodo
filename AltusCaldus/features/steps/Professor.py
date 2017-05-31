'''from behave import *
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


@when('Informo o {nome}, {genero}, {data_nascimento}, {cpf}, {email}, {telefone}, {celular}, {emergencia}')
def step_impl(context, nome, genero: str, data_nascimento: str, cpf: str, email: str, telefone: str, celular: str,
              emergencia: str):
    br = context.browser

    form = {'nome': nome, 'genero': genero, 'data_nascimento': data_nascimento, 'cpf': cpf, 'email': email,
            'telefone': telefone, 'celular': celular, 'emergencia': emergencia}
    br.fill_form(form)
    br.find_by_css('.submit-row input').first.click()


@then('Eu sou direcionado para {url_saida}')
def step_impl(context, url_saida:str):
    url_atual = context.browser.url
    assert (url_atual == (context.base_url + url_saida))
    # context.browser.quit()


@when('Informo ou o {nome}, ou o {genero}, ou o {data_nascimento}, ou o {cpf}, ou o {email}, ou o {telefone}, ou o {celular}, ou o {emergencia} errado')
def step_impl(context, nome:str, genero: str, data_nascimento: str, cpf: str, email: str, telefone: str, celular: str,
              emergencia: str):
    br = context.browser

    form = {'nome': nome, 'genero': genero, 'data_nascimento': data_nascimento, 'cpf': cpf, 'email': email,
            'telefone': telefone, 'celular': celular, 'emergencia': emergencia}
    br.fill_form(form)
    br.find_by_css('.submit-row input').first.click()

'''

