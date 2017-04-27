from django.db import models
from django.utils import timezone


class Pessoa(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False)
    email = models.EmailField()
    GENERO = ('Masculino', 'Masculino'), ('Feminino', 'Feminino')
    genero = models.CharField(max_length=9, choices=GENERO)
    celular = models.IntegerField()
    telefone = models.IntegerField()
    emergencia = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Aluno(Pessoa):
    def __str__(self):
        return self.nome


class Professor(Pessoa):
    def __str__(self):
        return self.nome


class Servico(models.Model):
    data = models.DateField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Aluno)
    vendedor = models.ForeignKey('auth.User')

    class Meta:
        abstract = True


class Item(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=200, null=False)
    data_entrada = models.DateField()

    def __str__(self):
        return self.nome


class Guarderia(Servico):
    item = models.ForeignKey(Item, blank=True, null=False)

    def __str__(self):
        return self.cliente.nome


class TipoPrancha(models.Model):
    descricao = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.descricao


class Prancha(models.Model):
    descricao = models.CharField(max_length=200, null=False)
    tipo_prancha = models.ForeignKey(TipoPrancha)
    altura = models.CharField(max_length=10, null=False)
    litragem = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.descricao


class Aluguel(Servico):
    prancha = models.ManyToManyField(Prancha)

    def __str__(self):
        return self.cliente.nome


class Aula(Servico):
    professor = models.ForeignKey(Professor)
    inicio = models.TimeField()

    def __str__(self):
        return self.cliente.nome + ' (' + self.data.__str__() + ')'




class PacoteAula(Servico):
    aulas = models.ManyToManyField(Aula)

    def __str__(self):
        return "Pacote: " + self.cliente.nome + " (" + self.data.__str__() + ")"
