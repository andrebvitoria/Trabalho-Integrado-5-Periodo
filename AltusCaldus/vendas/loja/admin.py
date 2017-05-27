from django.contrib import admin
from .models import *

# Register your models here.

#==========={Entrada}===========#
'''
class EntradaDetailInline(admin.TabularInline):
    list_display = ('produto', 'SubTotal',)
    readonly_fields = ['get_subtotal']
    model = DetalheEntrada
    extra = 0

#readonly_fields = ['valor_total']
date_hierarchy = 'created'
@admin.register(Entrada)
class GuarderiaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data',)
    readonly_fields = ['valor_total']
    date_hierarchy = 'created'
    list_filter = ('data',)
    inlines = [EntradaDetailInline]
 '''
#=================================#


# class VendaDetailInline(admin.TabularInline):
#     list_display = ('produto','total', 'grupo',)
#     readonly_fields = ['get_total']
#     model = DetalheVenda
#     extra = 0


# @admin.register(Venda)
# class VendaAdmin(admin.ModelAdmin):
# 	list_display = ('__str__', 'data',)
# 	list_filter = ('data',)
# 	inlines = [VendaDetailInline]



admin.site.register(Cantina)

admin.site.register(Camisa)
admin.site.register(TamanhoCamisa)
admin.site.register(TipoCamisa)
admin.site.register(Cor)

admin.site.register(Prancha)
admin.site.register(TipoPrancha)

class DetalheProdutoInLine(admin.TabularInline):
    list_display = ['nome', 'quantidade', 'total']
    readonly_fields = ['get_valor','get_preco']
    model = DetalheProduto
    extra = 0

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('qtd','preco','categoria',)
    date_hierarchy = 'created'
    list_filter = ('categoria',)
    search_fields = ('nome',)  


@admin.register(Venda)    
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente','vendedor', 'data',)
    date_hierarchy = 'created'
    search_fields = ('cliente',)
    list_filter = ('data',)
    #list_per_page = 1
    inlines = [DetalheProdutoInLine]  
