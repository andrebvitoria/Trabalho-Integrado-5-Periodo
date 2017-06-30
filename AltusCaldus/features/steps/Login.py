from behave import *
from django.contrib.auth.models import User


@Given('Eu sou um usuario na tela de login do admin')
def given_url(context):
    User.objects.create_superuser(username='test', email='foo@bar', password='test')
    br = context.browser
    br.visit(context.base_url + '/admin/')

@when('Informo meu {login} e minha {senha}')
def step_impl(context, login:str, senha: str):
    br = context.browser
    br.fill('username', login)
    br.fill('password', senha)
    br.find_by_css('.submit-row input').first.click()



