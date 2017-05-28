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


#=================================={Produto}================================#

class Categoria(TimeStampedModel):
    descricao = models.CharField('Descricao', max_length=200)

    def __str__(self):
        return self.descricao


class Produto(TimeStampedModel):
    nome = models.CharField('Nome', max_length=200)
    descricao = models.CharField('Descricao', max_length=200, blank = True, null=True)
    qtd = models.IntegerField(verbose_name='Quantidade', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria')
    preco = models.DecimalField(verbose_name ='Preco', max_digits=6, decimal_places=2, default=0)


    def __str__(self):
        return self.nome


class Cantina(Produto):
    pass

    def __str__(self):
        return self.nome
    

class Cor(models.Model):
    descricao = models.CharField('Descrição', max_length=200, null=False)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.descricao



class Camisa(Produto):
    tamanho =[('PP', 'PP'),('P', 'P'),('M','M'),('G','G'),('GG','GG')]
    valor_custo = models.DecimalField('Valor de Custo', max_digits=6, decimal_places=2, default=0)
    tamanho = models.CharField('Tamanho', max_length=2, choices=tamanho)
    cor = models.ForeignKey(Cor, verbose_name='Cor')

    def __str__(self):
        return self.descricao

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


#=================================={Vendas}================================#



class Cliente(TimeStampedModel):
    nome = models.CharField(max_length=255)


    def __str__(self):
        return self.nome


class Venda(TimeStampedModel):
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', null=True, blank=True)
    vendedor = models.ForeignKey('auth.User', verbose_name='Vendedor')
    data = models.DateTimeField('vendido em', auto_now_add=True, auto_now=False, blank=True)
    total = models.DecimalField('Valor R$', max_digits=6, decimal_places=2, default=0)
    desconto = models.DecimalField('Desconto R$',max_digits=6, decimal_places=2, default=0)


    def __str__(self):
        return str(self.data)


    def _total(self):
        qs = self.venda_det.filter(venda=self.pk).values_list('preco','quantidade') or 0
        t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0]*q[1], qs))
        setattr(self,'total', t )
        return "R$ %s" % number_format(t, 2)



        
class DetalheVenda(TimeStampedModel):
    produto = models.ForeignKey(Produto, verbose_name='Produto')
    venda = models.ForeignKey(Venda, verbose_name='Venda', related_name='venda_det')
    preco = models.DecimalField(verbose_name ='Preco', max_digits=6, decimal_places=2, default=25)
    quantidade = models.DecimalField(verbose_name ='Quantidade', max_digits=6, decimal_places=0, default=1)
    


    def _qtd(self, value):
        self.quantidade = value
    
    @property
    def subtotal(self):
        return self.preco*self.quantidade
    

    def subtotal_formated(self):
        return "R$ %s" % number_format(self.sub, 2)

    

    
    
    


