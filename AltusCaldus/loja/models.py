from django.db import models
import django.utils.timezone 
from django.core.urlresolvers import reverse_lazy
from django.utils.formats import number_format
from django.shortcuts import render_to_response
# from vendas.servicos.models import Pessoa,Aluno


# Create your models here.

class TimeStampedModel(models.Model):
    criado = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)
    modificado = models.DateTimeField('modificado em', auto_now_add=False, auto_now=True)

    # Colocar autor
    class Meta:
        abstract = True


#=================================={Produto}================================#

class Categoria(TimeStampedModel):
    descricao = models.CharField('Descricao', max_length=200)

    def __str__(self):
        return self.descricao


class Produto(TimeStampedModel):
    imagem = models.ImageField(upload_to = 'static/imagem/', null=True)
    nome = models.CharField('Nome', max_length=200)
    descricao = models.CharField('Descricao', max_length=200, blank = True, null=True)
    qtd = models.IntegerField(verbose_name='Quantidade', blank=True, null=True, default=0)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria')
    preco = models.DecimalField(verbose_name ='Preco', max_digits=6, decimal_places=2, default=0.0)
    valor_custo = models.DecimalField('Valor de Custo', max_digits=6, decimal_places=2, default=0.0, null=True)


    def __str__(self):
        return self.nome +' '+self.descricao

    def setValor(self, new_valor):
        self.preco = new_valor
        self.save()
        return True

    def subtraiEstoque(self, qtd):
        new_qtd = self.qtd - int(qtd)

        if new_qtd < 0:
            return False

        self.qtd = new_qtd
        self.save()
        return True

    def aumentaEstoque(self, qtd):
        new_qtd = self.qtd + int(qtd)

        self.qtd = new_qtd
        self.save()
        return True


class Cor(models.Model):
    descricao = models.CharField('Descricao', max_length=200, null=False)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.descricao



class Camisa(Produto):
    tamanho =[('PP', 'PP'),('P', 'P'),('M','M'),('G','G'),('GG','GG')]
    tamanho = models.CharField('Tamanho', max_length=2, choices=tamanho)
    cor = models.ForeignKey(Cor, verbose_name='Cor')

    def __str__(self):
        return self.nome +' - '+str(self.cor)+' -'+self.tamanho

    def get_subtotal(self):
        return self.valor_venda


class TipoPrancha(TimeStampedModel):
    descricao = models.CharField('Descricao', max_length=200, null=False)

    class Meta:
        verbose_name = 'Tipo de Prancha'
        verbose_name_plural = 'Tipos de Prancha'

    def __str__(self):
        return self.descricao



class Prancha(Produto):
    altura = models.DecimalField('Altura', max_digits=6, decimal_places=2, default=0)
    litragem = models.DecimalField('Litragem', max_digits=6, decimal_places=2, default=0)
    tipo_prancha = models.ForeignKey(TipoPrancha, verbose_name='Tipo de Prancha')
    

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
    desconto = models.DecimalField('Desconto R$',max_digits=6, decimal_places=2, default=0)
    valor_pago = models.DecimalField('Pagamento R$',max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.data)


    
    def Total(self):
        qs = self.venda_det.filter(venda=self.pk).values_list('preco','quantidade') or 0
        t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0]*q[1], qs))
        return "R$ " + number_format(t, 2)

    
    
    def Troco(self):  
        qs = self.venda_det.filter(venda=self.pk).values_list('preco','quantidade') or 0
        t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0]*q[1], qs))
        v_final = t-self.desconto
        if self.valor_pago < v_final:
            return "VALOR ABAIXO DO TOTAL"
        else:
            return self.valor_pago-(v_final)

    
        
class ItemVenda(TimeStampedModel):
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

    def save(self, **kwargs):    
        try:
            item_venda = ItemVenda.objects.get(pk=self.pk)
            val = self.quantidade - item_venda.quantidade
            if self.produto.subtraiEstoque(val):
                super().save()
        except:
            if self.produto.subtraiEstoque(self.quantidade):
                super().save()

        self.preco = self.produto.preco
        super().save()
    


#=================================={Entradas}================================#

class Entrada(TimeStampedModel):
    total = models.Empty()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'


    def __str__(self):
        return ("ENTRADA: " + str(self.id))

    def _total(self):
        qs = self.Entrada_det.filter(entrada=self.pk).values_list('valor','quantidade') or 0
        t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0]*q[1], qs))
        setattr(self,'total', t )
        return "R$ %s" % number_format(t, 2)


class ItemEntrada(TimeStampedModel):
    entrada = models.ForeignKey(Entrada, verbose_name='Entrada',related_name='Entrada_det')
    produto = models.ForeignKey(Produto, verbose_name='Produto')
    valor = models.DecimalField('Valor do item', max_digits=6, decimal_places=2, default=0)
    quantidade = models.DecimalField(verbose_name ='Quantidade', max_digits=6, decimal_places=0, default=1)

    def _qtd(self, value):
        self.quantidade = value

    @property
    def _Valor_atual(self):
        return self.produto.preco
    
    @property
    def subtotal(self):
            return self.valor*self.quantidade
    

    def subtotal_formated(self):
        return "R$ %s" % number_format(self.sub, 2)
        
        
    def save(self, **kwargs):
        try:
            item_entrada = ItemEntrada.objects.get(pk=self.pk)
            val = self.quantidade - item_entrada.quantidade
            
            self.produto.preco = self.valor
            super().save()

            if self.produto.aumentaEstoque(val):
                super().save()

            
        except:
            
            self.produto.preco = self.valor
            super().save()
            
            if self.produto.aumentaEstoque(self.quantidade):
                super().save()
