from django.contrib import admin
from .models import Produto
from .models import Categoria
from .models import Entrada
from .models import Venda
from .models import ItensVenda
from .models import ItensEntrada



admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Entrada)
admin.site.register(Venda)
admin.site.register(ItensEntrada)
admin.site.register(ItensVenda)


# Register your models here.
