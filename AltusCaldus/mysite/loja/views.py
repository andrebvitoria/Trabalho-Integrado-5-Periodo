from django.shortcuts import render
from .models import Produto


# Create your views here.
def list_produto(request):
    produtos = Produto.objects.all().order_by('nome')
    return render(request, 'loja/list_produto.html', {'produtos':produtos})
