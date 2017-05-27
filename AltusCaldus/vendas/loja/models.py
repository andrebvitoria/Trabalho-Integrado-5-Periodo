from django.db import models
import django.utils.timezone 
from django.core.urlresolvers import reverse_lazy
from django.utils.formats import number_format



# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField('modificado em', auto_now_add=False, auto_now=True)

    # Colocar autor
    class Meta:
        abstract = True


class Produto(TimeStampedModel):
    qtd = models.IntegerField(verbose_name='Quantidade')
    categoria = models.CharField(max_length=250)
    preco = models.DecimalField(verbose_name ='Preco', max_digits=6, decimal_places=2, default=0)


    def __str__(self):
        return self.categoria


class Cantina(Produto):
    nome = models.CharField('Nome', max_length=200)
    descricao = models.CharField('Descricao', max_length=200)


    def __str__(self):
        return self.nome
    

    def get_subtotal(self):
        return self.valor_venda



class Cor(models.Model):
    descricao = models.CharField('Descrição', max_length=200, null=False)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.descricao


class TamanhoCamisa(models.Model):
    descricao = models.CharField('Descrição', max_length=200, null=False)

    def __str__(self):
        return self.descricao


class TipoCamisa(models.Model):
    descricao = models.CharField('Descrição', max_length=200, null=False)

    def __str__(self):
        return self.descricao


class Camisa(Produto):
    valor_custo = models.DecimalField('Valor de Custo', max_digits=6, decimal_places=2, default=0)
    tipo_camisa = models.ForeignKey(TipoCamisa, verbose_name='Tipo')
    tamanho = models.ForeignKey(TamanhoCamisa, verbose_name='Tamanho')
    cor = models.ForeignKey(Cor, verbose_name='Cor')

    def __str__(self):
        return str(self.tipo_camisa)

    def get_subtotal(self):
        return self.valor_venda


class TipoPrancha(TimeStampedModel):
    descricao = models.CharField('Descrição', max_length=200, null=False)

    class Meta:
        verbose_name = 'Tipo de Prancha'
        verbose_name_plural = 'Tipos de Prancha'

    def __str__(self):
        return self.descricao



class Prancha(Produto):
    descricao = models.CharField('Descrição', max_length=200, null=True)
    altura = models.DecimalField('Altura', max_digits=6, decimal_places=2, default=0)
    litragem = models.DecimalField('Litragem', max_digits=6, decimal_places=2, default=0)
    tipo_prancha = models.ForeignKey(TipoPrancha, verbose_name='Tipo de Prancha')
    valor_custo = models.DecimalField('Valor de Custo', max_digits=6, decimal_places=2, default=0)
    

    class Meta:
        verbose_name = 'Prancha'
        verbose_name_plural = 'Pranchas'

    def __str__(self):
        return str(self.tipo_prancha)

    def get_subtotal(self):
        return self.valor_venda




class Venda(TimeStampedModel):
    cliente = models.CharField(max_length=255)
    vendedor = models.ForeignKey('auth.User', verbose_name='Vendedor')
    data = models.DateTimeField('vendido em', auto_now_add=True, auto_now=False, blank=True)
    #valor = models.DecimalField('Valor R$', max_digits=6, decimal_places=2, default=0)
    #desconto = models.DecimalField('Desconto R$', max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.cliente
    


class DetalheProduto(TimeStampedModel):
    produto = models.ForeignKey(Produto, verbose_name='Produto')
    venda = models.ForeignKey(Venda, verbose_name='Venda', related_name='venda_det')
    preco = models.DecimalField(verbose_name ='Preco', max_digits=6, decimal_places=2, default=0)
    quantidade = models.DecimalField(verbose_name ='Quantidade', max_digits=6, decimal_places=0, default=1)
    categoria = models.CharField(verbose_name='Categoria', max_length=250)
    valor = models.DecimalField(verbose_name ='Valor', max_digits=6, decimal_places=2, default=0)
    

    def get_categoria(self):
        return self.produto.categoria

    def get_preco(self):
        return self.produto.preco*self.quantidade
     
    def get_valor(self):
        return self.produto.preco

    
    valor = property(get_valor)    
    categoria = property(get_categoria)
    preco = property(get_preco)



