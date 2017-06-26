from django.contrib import admin
from .models import *

# Register your models here.




admin.site.register(Cor)
admin.site.register(TipoPrancha)
admin.site.register(Categoria)




@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)



@admin.register(Prancha)
class PranchaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'qtd','tipo_prancha','altura','litragem', 'preco',)
    date_hierarchy = 'criado'
    list_filter = ('nome','tipo_prancha',)
    



@admin.register(Camisa)
class CamisaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'qtd','cor','tamanho',)
    date_hierarchy = 'criado'
    list_filter = ('cor','tamanho','descricao')



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','qtd','preco','categoria',)
    date_hierarchy = 'criado'
    list_filter = ('categoria',)
    search_fields = ('nome',)  



class ItemVendaInline(admin.TabularInline):
    list_display = ('produto', 'quantidade','subtotal')
    exclude = ('preco',)
    readonly_fields = ['subtotal']
    model = ItemVenda
    extra = 0


@admin.register(Venda)    
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'vendedor',)
    readonly_fields = ['Total', 'Troco']
    exclude = ('total',)
    search_fields = ('cliente',)
    date_hierarchy = 'criado'
    list_filter = ('data',)
    inlines = [ItemVendaInline]
    

#==========={Entrada}===========#

class ItemEntradaInline(admin.TabularInline):
    list_display = ['produto','quantidade', 'SubTotal','valor atual',]
    readonly_fields = ['subtotal','_Valor_atual']
    model = ItemEntrada
    extra = 0

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'criado',)
    readonly_fields = ['_total']
    date_hierarchy = 'criado'
    list_filter = ('criado',)
    inlines = [ItemEntradaInline]
#=================================#
