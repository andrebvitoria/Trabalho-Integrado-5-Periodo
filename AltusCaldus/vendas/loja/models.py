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

    
    def subtraiEstoque(self, qtd):
        new_qtd = self.qtd - qtd

        if new_qtd < 0:
            return False

        self.qtd = new_qtd
        self.save()
        return True


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
    total = models.DecimalField('Total R$', max_digits=6, decimal_places=2, default=0)
    desconto = models.DecimalField('Desconto R$',max_digits=6, decimal_places=2, default=0)
    

    def __str__(self):
        return str(self.data)

    @property    
    def _total(self):
        qs = self.venda_det.filter(venda=self.pk).values_list('preco','quantidade') or 0
        t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0]*q[1], qs))
        return "R$ %s" % number_format(t, 2)


    def calcula_troco(self, total, valor):
        if pago < _total:
            return 'Iválido'
        else:
            return pago-total

    
        
class DetalheVenda(TimeStampedModel):
    produto = models.ForeignKey(Produto, verbose_name='Produto')
    venda = models.ForeignKey(Venda, verbose_name='Venda', related_name='venda_det')
    preco = models.DecimalField(verbose_name ='Preco', max_digits=6, decimal_places=2, default=0)
    quantidade = models.DecimalField(verbose_name ='Quantidade', max_digits=6, decimal_places=0, default=1)
    


    def _qtd(self, value):
        self.quantidade = value
    
    @property
    def subtotal(self):
        return self.produto.preco*self.quantidade
    

    def subtotal_formated(self):
        return "R$ %s" % number_format(self.sub, 2)

    def save(self):    
        try:
            detalhe_entrada = DetalheEntrada.objects.get(pk=self.pk)
            val = self.quantidade - detalhe_entrada.quantidade
            if self.produto.subtraiEstoque(val):
                super().save()
        except:
            if self.produto.subtraiEstoque(self.quantidade):
                super().save()

        self.preco = self.produto.preco * self.quantidade
        super().save()
    


#=================================={Entradas}================================#

class Entrada(TimeStampedModel):
    total = models.Empty()
    data = models.DateTimeField('Comprado em', auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'


    def __str__(self):
        return self.data

    def _total(self):
        qs = self.venda_det.filter(venda=self.pk).values_list('valor','quantidade') or 0
        t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0]*q[1], qs))
        setattr(self,'total', t )
        return "R$ %s" % number_format(t, 2)


class DetalheEntrada(TimeStampedModel):
    entrada = models.ForeignKey(Entrada, related_name='Entrada_det')
    produto = models.ForeignKey(Prancha, verbose_name='Produto')
    valor = models.DecimalField('Valor do item', max_digits=6, decimal_places=2, default=0)
    quantidade = models.DecimalField(verbose_name ='Quantidade', max_digits=6, decimal_places=0, default=1)

    def _qtd(self, value):
        self.quantidade = value
    
    @property
    def subtotal(self):
        return self.valor*self.quantidade
    

    def subtotal_formated(self):
        return "R$ %s" % number_format(self.sub, 2)
        
        
    def save(self):
        try:
            detalhe_entrada = DetalheEntrada.objects.get(pk=self.pk)
            val = self.quantidade - detalhe_entrada.quantidade
            if self.produto.subtraiEstoque(val):
                super().save()
        except:
            if self.produto.subtraiEstoque(self.quantidade):
                super().save()

    
