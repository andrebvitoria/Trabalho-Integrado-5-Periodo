from django.contrib import admin
#from .models import Customer, Seller, Brand, Product, Sale, SaleDetail
from .models import *

#==========={Pessoas}===========#
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cpf', 'email', 'telefone', 'celular', 'emergencia', 'data_nascimento', 'created')
    search_fields = ('nome',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cpf', 'email', 'telefone', 'celular', 'emergencia', 'data_nascimento', 'created')
    search_fields = ('nome',)
#===============================#

#==========={Guarderia}===========#
admin.site.register(Item)

class GuarderiaDetailInline(admin.TabularInline):
    list_display = ['item']
    readonly_fields = ['get_subtotal']
    model = ItemGuarderia
    extra = 0


@admin.register(Guarderia)
class GuarderiaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data', 'vencimento',)
    readonly_fields = ['valor_total']
    date_hierarchy = 'created'
    list_filter = ('cliente',)
    inlines = [GuarderiaDetailInline]
#=================================#

#============{Aluguel}============#
admin.site.register(Prancha)
admin.site.register(TipoPrancha)

class AluguelDetailInline(admin.TabularInline):
    list_display = ['prancha']
    readonly_fields = ['get_subtotal']
    model = ItemAluguel
    extra = 0


@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data',)
    readonly_fields = ['valor_total']
    date_hierarchy = 'created'
    list_filter = ('cliente',)
    inlines = [AluguelDetailInline]
#=================================#


#==========={Aulas}==========#
admin.site.register(AulaMarcada)

class AulaDetailInline(admin.TabularInline):
    list_display = ['aula', 'professor']
    readonly_fields = ['get_subtotal']
    model = ItemAula
    extra = 0


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    readonly_fields = ['valor_total']
    date_hierarchy = 'created'
    list_filter = ('cliente',)
    inlines = [AulaDetailInline]
#============================#