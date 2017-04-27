from django.db import models
from django.utils import timezone



class Item(models.Model):
    item = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=200, null=False)
    data_entrada = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.item

class Guarderia(models.Model):
    cliente = models.CharField(max_length=100, null=False)
    item = models.ForeignKey(Item, blank=True, null=False)

    def __str__(self):
        return self.cliente


class Tipo_Prancha(models.Model):
    descricao = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.descricao


class Prancha(models.Model):
    descricao = models.CharField(max_length=200, null=False)
    tipo_prancha = models.ForeignKey(Tipo_Prancha)
    altura = models.CharField(max_length=10, null=False)
    litragem = models.CharField(max_length=10, null=False)


    def __str__(self):
        return self.descricao

class Aluguel(models.Model):
    cliente = models.CharField(max_length=100, null=False)
    prancha = models.ManyToManyField(Prancha)
    data_aluguel = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.cliente
