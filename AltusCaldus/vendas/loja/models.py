from django.db import models
import django.utils.timezone 
from django.utils.formats import number_format


# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField('modificado em', auto_now_add=False, auto_now=True)

    # Colocar autor
    class Meta:
        abstract = True


class Produto(TimeStampedModel):
    nome = models.CharField(max_length=250)
    qtd = models.IntegerField(verbose_name='Quantidade')
    categoria = models.CharField(max_length=250)
    preco = models.DecimalField(verbose_name ='Preco', max_digits=6, decimal_places=2, default=0)



    def __str__(self):
        return self.nome


class Venda(TimeStampedModel):
    cliente = models.CharField(max_length=255)
    vendedor = models.ForeignKey('auth.User', verbose_name='Vendedor')
    data = models.DateTimeField('vendido em', auto_now_add=True, auto_now=False, blank=True)


    def __str__(self):
        return self.cliente



class DetalheProduto(TimeStampedModel):
    produto = models.ForeignKey(Produto, verbose_name='Produto')
    venda = models.ForeignKey(Venda, verbose_name='Venda')
    preco = models.DecimalField(verbose_name ='Preco', max_digits=6, decimal_places=2, default=0)
    quantidade = models.IntegerField()
    categoria = models.CharField(verbose_name='Categoria', max_length=250)


    def get_categoria(self):
        return self.produto.categoria

    def get_preco(self):
        return self.produto.preco

    categoria = property(get_categoria)
    preco = property(get_preco)



