from django.db import models
from django.utils import timezone


# Create your models here.

class Categoria(models.Model):

    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    desconto = models.IntegerField()
    lucro = models.IntegerField()

    def __str__(self):
        return str(self.descricao)


class Produto(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor_venda = models.FloatField()
    valor_custo = models.FloatField()
    valor_desc = models.FloatField()
    percent_desc = models.IntegerField()
    promocao = models.FloatField()
    qtd_estoque = models.IntegerField()
    grupo = models.ManyToManyField('Categoria')
    def __str__(self):
        return str(self.nome)

class Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return str(self.id)

class Venda(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    total = models.FloatField()
    desconto = models.IntegerField()

class Historico_Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    id_total = models.ForeignKey('Entrada', on_delete=models.CASCADE)
    produto = models.ManyToManyField('Produto')
    valor = models.FloatField()
    quantidade = models.FloatField()

    def __str__(self):
        return str(self.produto)


class Historico_Venda(models.Model):
    id = models.AutoField(primary_key=True)
    id_total = models.ForeignKey('Venda', on_delete=models.CASCADE)
    produto = models.ManyToManyField('Produto')
    valor = models.FloatField()
    desconto = models.FloatField()
    quantidade = models.FloatField()
    cancelado = models.BooleanField()

    def __str__(self):
        return str(self.produto)
