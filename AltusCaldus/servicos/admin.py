from django.contrib import admin
from .models import *
from django.contrib import messages


# ==========={Pessoas}=========== #
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cpf', 'email', 'telefone', 'celular', 'emergencia', 'data_nascimento', 'created')
    search_fields = ('nome',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cpf', 'email', 'telefone', 'celular', 'emergencia', 'data_nascimento', 'created')
    search_fields = ('nome',)


# =============================== #

# ==========={Guarderia}=========== #
admin.site.register(Item)


class GuarderiaDetailInline(admin.TabularInline):
    list_display = ['item']
    readonly_fields = ['get_subtotal']
    model = ItemGuarderia
    extra = 0


@admin.register(Guarderia)
class GuarderiaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data', 'vencimento',)
    readonly_fields = ['valor_total', 'troco']
    date_hierarchy = 'created'
    list_filter = ('cliente',)
    inlines = [GuarderiaDetailInline]

    def save_model(self, request, obj, form, change):
        if obj.save():
            messages.add_message(request, messages.INFO, 'Guarderia efetuada com Sucesso!')
        else:
            messages.add_message(request, messages.ERROR, 'Erro ao efetuar a Guarderia!')
        return


# ================================= #

# ============{Aluguel}============ #
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
    readonly_fields = ['valor_total', 'troco']
    date_hierarchy = 'created'
    list_filter = ('cliente',)
    inlines = [AluguelDetailInline]

    def save_model(self, request, obj, form, change):
        if obj.save():
            messages.add_message(request, messages.INFO, 'Aluguel efetuado com Sucesso!')
        else:
            messages.add_message(request, messages.ERROR, 'Erro ao efetuar a Algueul!')
        return


# ================================= #


# ==========={Aulas}========== #
admin.site.register(AulaMarcada)


class AulaDetailInline(admin.TabularInline):
    list_display = ['aula', 'professor']
    readonly_fields = ['get_subtotal']
    model = ItemAula
    extra = 0


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    readonly_fields = ['valor_total', 'troco']
    date_hierarchy = 'created'
    list_filter = ('cliente',)
    inlines = [AulaDetailInline]

    def save_model(self, request, obj, form, change):
        if obj.save():
            messages.add_message(request, messages.INFO, 'Venda efetuada com Sucesso!')
        else:
            messages.add_message(request, messages.ERROR, 'Erro ao efetuar a venda!')
        return

# ============================ #