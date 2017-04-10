from django.db import models
from django.utils import timezone

class Item(models.Model):
    descricao = models.CharField(max_length=200, null=False)

class Guarderia(models.Model):
    item = models.ForeignKey(Item, blank=True, null=False)

