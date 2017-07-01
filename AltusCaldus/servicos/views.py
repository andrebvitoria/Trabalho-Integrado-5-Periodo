from django.shortcuts import render
from servicos.models import Aula
from servicos.views_class import *


# Create your views here.
def index(request):
    return render(request, 'servicos/index.html', {})


def aula(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if request.POST['data_inicial'] == ' ' or request.POST['data_final'] == ' ':
            aulas = Aula.objects.order_by('id')
        else:
            data = [Date.to_date(request.POST['data_inicial']), Date.to_date(request.POST['data_final'])]
            aulas = Aula.objects.filter(data__range=data).order_by('id')

        aulas_agrupadas = dict()
        for aula in aulas:
            if aula.cliente.nome in aulas_agrupadas:
                aulas_agrupadas[aula.cliente.nome] += aula.calcula_total()
            else:
                aulas_agrupadas[aula.cliente.nome] = aula.calcula_total()

        lista_aulas = list()
        a = request.POST
        if int(request.POST['numero_de_alunos']) <= 0 or int(request.POST['numero_de_alunos']) > len(aulas_agrupadas):
            i = 1
            for nome in sorted(aulas_agrupadas.keys()):
                lista_aulas.append(AdapterAula(nome, aulas_agrupadas[nome], i))
                i += 1
        else:
            aulas_por_valor = dict()
            for nome in sorted(aulas_agrupadas.keys()):
                if aulas_agrupadas[nome] in aulas_por_valor:
                    aulas_por_valor[aulas_agrupadas[nome]].append(nome)
                else:
                    aulas_por_valor[aulas_agrupadas[nome]] = [nome]

            lista_nomes = list()
            for valor in sorted(aulas_por_valor.keys()):
                lista_nomes = aulas_por_valor[valor] + lista_nomes

            i = 1
            for nome in lista_nomes[:int(request.POST['numero_de_alunos'])]:
                lista_aulas.append(AdapterAula(nome, aulas_agrupadas[nome], i))
                i += 1

        return render(request, 'servicos/aula/aula.html', {'form': form, 'aulas': lista_aulas})
    form = AulaForm()
    return render(request, 'servicos/aula/aula.html', {'form': form, 'aulas': list()})


def construcao(request):
    return render(request, 'servicos/construcao.html', {})


def guarderia(request):
    return construcao(request)


def aluguel(request):
    return construcao(request)