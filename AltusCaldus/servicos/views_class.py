from django.db import models
from django import forms
from datetime import date


class MetaAula(models.Model):
    data_inicial = models.DateField()
    data_final = models.DateField()
    numero_de_alunos = models.IntegerField()

    def get_date(self):
        new_data_inicial = self.data_inicial.__str__()
        new_data_final = self.data_final.__str__()

        return [new_data_inicial, new_data_final]


class AulaForm(forms.ModelForm):
    data_inicial = forms.DateField()
    data_final = forms.DateField()
    numero_de_alunos = forms.IntegerField(min_value=0)

    class Meta:
        model = MetaAula
        fields = ('data_inicial', 'data_final', 'numero_de_alunos')


class AdapterAula(object):
    def __init__(self, *args):
        self.nome = args[0]
        self.valor = args[1]
        self.id = args[2]


# ======={Metodos Globais}======= #
class Date(object):

    @staticmethod
    def to_date(old_date):
        new_date = old_date.split('-')
        return date(int(new_date[0]), int(new_date[1]), int(new_date[2]))