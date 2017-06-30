from splinter.browser import Browser
from django.contrib.auth.models import User

def before_all(context):
    context.browser = Browser('chrome')
    context.server_url = 'http://localhost:8000'
    
    User.objects.create_superuser(username='admin', email='foo@bar', password='admin123123')
    br = context.browser
    br.visit(context.server_url + '/admin/')


def after_all(context):
    context.browser.quit()
    context.browser = None