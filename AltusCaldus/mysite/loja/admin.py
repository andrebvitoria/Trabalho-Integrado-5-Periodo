from django.contrib import admin
from .models import Produto
from .models import Categoria
from .models import Entrada
from .models import Venda
from .models import Historico_Venda
from .models import Historico_Entrada



admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Entrada)
admin.site.register(Venda)
admin.site.register(Historico_Venda)
admin.site.register(Historico_Entrada)


# Register your models here.
