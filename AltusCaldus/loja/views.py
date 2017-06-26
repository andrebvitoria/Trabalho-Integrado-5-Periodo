from django.shortcuts import render
from .models import Produto


# Create your views here.
def loja_online(request):
    produtos = Produto.objects.all().order_by('nome')
    return render(request, 'loja/loja_online.html', {'produtos':produtos})
# Create your views here.
