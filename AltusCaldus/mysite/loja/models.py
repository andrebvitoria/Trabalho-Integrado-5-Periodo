from django.db import models
from django.utils import timezone


# Create your models here.

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    desconto = models.IntegerField(default = 0)
    lucro = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.descricao)


class Produto(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor_venda = models.FloatField()
    valor_custo = models.FloatField()
    percent_desc = models.IntegerField(default = 0)
    promocao = models.FloatField(default = 0.00)
    qtd_estoque = models.IntegerField()
    grupo = models.ManyToManyField('Categoria')
    def __str__(self):
        return str(self.nome)

class Entrada(models.Model):
    itens_entrada = models.ManyToManyField('ItensEntrada')
    data = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return str(self.total)

class Venda(models.Model):
    itens_venda = models.ManyToManyField('ItensVenda')
    data = models.DateField()
    total = models.FloatField()
    desconto = models.IntegerField()

class ItensEntrada(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    valor = models.FloatField()
    quantidade = models.FloatField()

    def __str__(self):
        return str(self.produto)


class ItensVenda(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    valor = models.FloatField()
    desconto = models.FloatField()
    quantidade = models.FloatField()
    cancelado = models.BooleanField()

    def __str__(self):
        return str(self.produto)
