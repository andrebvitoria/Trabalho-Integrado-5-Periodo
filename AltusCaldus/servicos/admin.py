from django.contrib import admin
from .models import *
from django.contrib import messages
from decimal import Decimal


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
        guarderia = obj

        # Verifica se existe requisição com novo valor de pagamento, caso nao tenha usa o armazenado no banco
        valor_pago = float(request.POST['valor_pago']) if 'valor_pago' in request.POST else guarderia.valor_pago
        # Verifica se existe requisição com novo valor de desconto caso, caso nao tenha usa o armazenado no banco
        # Soma desconto com valor pago
        valor_pago += float(request.POST['desconto']) if 'desconto' in request.POST else valor_pago + guarderia.desconto
        # Verifica se existe requisição com novos valores de serviço, caso nao tenha usa o armazenado no banco
        valor_servico = get_valor_itens(request.POST,
                                        'guarderia_det-#-valor') if 'guarderia_det-0-valor' in request.POST else guarderia.calcula_total()

        if valor_pago < valor_servico:
            messages.add_message(request, messages.WARNING,
                                 'Não é Permitido guarderias com valores menores que o minimo, caso seja inserido valor '
                                 'inferior ao da guarderia o minimo sera inserido por padrão')
            request.POST['valor_pago'] = str(valor_servico)
            obj.valor_pago = Decimal(str(valor_servico - float(request.POST['desconto'])))
        else:
            messages.add_message(request, messages.INFO, 'Guarderia efetuada com Sucesso!')
        super().save_model(request, obj, form, change)


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
        aluguel = obj

        # Verifica se existe requisição com novo valor de pagamento, caso nao tenha usa o armazenado no banco
        valor_pago = float(request.POST['valor_pago']) if 'valor_pago' in request.POST else aluguel.valor_pago
        # Verifica se existe requisição com novo valor de desconto caso, caso nao tenha usa o armazenado no banco
        # Soma desconto com valor pago
        valor_pago += float(request.POST['desconto']) if 'desconto' in request.POST else valor_pago + aluguel.desconto
        # Verifica se existe requisição com novos valores de serviço, caso nao tenha usa o armazenado no banco
        valor_servico = get_valor_itens(request.POST,
                                        'aluguel_det-#-valor') if 'aluguel_det-0-valor' in request.POST else aluguel.calcula_total()

        if valor_pago < valor_servico:
            messages.add_message(request, messages.WARNING,
                                 'Não é Permitido alugueis com valores menores que o minimo, caso seja inserido valor '
                                 'inferior ao do aluguel o minimo sera inserido por padrão')
            request.POST['valor_pago'] = str(valor_servico)
            obj.valor_pago = Decimal(str(valor_servico - float(request.POST['desconto'])))
        else:
            messages.add_message(request, messages.INFO, 'Aluguel efetuada com Sucesso!')
        super().save_model(request, obj, form, change)


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
        aula = obj

        # Verifica se existe requisição com novo valor de pagamento, caso nao tenha usa o armazenado no banco
        valor_pago = float(request.POST['valor_pago']) if 'valor_pago' in request.POST else aula.valor_pago
        # Verifica se existe requisição com novo valor de desconto caso, caso nao tenha usa o armazenado no banco
        # Soma desconto com valor pago
        valor_pago += float(request.POST['desconto']) if 'desconto' in request.POST else valor_pago + aula.desconto
        # Verifica se existe requisição com novos valores de serviço, caso nao tenha usa o armazenado no banco
        valor_servico = get_valor_itens(request.POST,
                                        'aula_det-#-valor') if 'aula_det-0-valor' in request.POST else aula.calcula_total()

        if valor_pago < valor_servico:
            messages.add_message(request, messages.WARNING,
                                 'Não é Permitido vendas com valores menores que o minimo, caso seja inserido valor '
                                 'inferior ao da venda o minimo sera inserido por padrão')
            request.POST['valor_pago'] = str(valor_servico)
            obj.valor_pago = Decimal(str(valor_servico - float(request.POST['desconto'])))
        else:
            messages.add_message(request, messages.INFO, 'Venda efetuada com Sucesso!')
        super().save_model(request, obj, form, change)


# ============================ #

# =={Metodos Compartilhados}== #
def get_valor_itens(POST, key):
    valor = 0.0
    index = 0
    new_key = key.replace('#', str(index))
    while new_key in POST:
        valor += float(POST[new_key])

        index += 1
        new_key = key.replace('#', str(index))
    return valor


# ============================ #
