from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.utils.formats import number_format

# Classe com datas de criacao e modificacao da classe 
class TimeStampedModel(models.Model):
    created = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField('modificado em', auto_now_add=False, auto_now=True)
    #Colocar autor
    class Meta:
        abstract = True

#================================{Pessoas}================================#
class Pessoa(TimeStampedModel):
    genero_list = [('M', 'Masculino'), ('F', 'Feminino')]
    nome = models.CharField('Nome', max_length=200)
    genero = models.CharField('gênero', max_length=1, choices=genero_list)
    data_nascimento = models.DateField('Nascimento')
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=18)
    celular = models.CharField('Celular', max_length=18)
    emergencia = models.CharField('Emergencia', max_length=18)


    class Meta:
        abstract = True
        ordering = ['nome']

    def __str__(self):
        return self.nome
    full_name = property(__str__)


class Aluno(Pessoa):
    pass

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    # clica na pessoa e retorna os detalhes dela
    def get_customer_url(self):
        return "/customer/%i" % self.id

class Professor(Pessoa):
    pass

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    # clica na pessoa e retorna os detalhes dela
    def get_customer_url(self):
        return "/customer/%i" % self.id

#================================{Servicos}================================#
class Servico(TimeStampedModel):
    vendedor = models.ForeignKey('auth.User', verbose_name='Vendedor')
    cliente = models.ForeignKey(Aluno, verbose_name='Cliente')
    data = models.DateField('Data')
    valor = models.DecimalField('Valor R$', max_digits=6, decimal_places=2, default=0)
    desconto = models.DecimalField('Desconto R$', max_digits=6, decimal_places=2, default=0)

    class Meta:
        abstract = True

    def valor_total(self):
        pass
        return

#================================{Guarderia}================================#
class Item(models.Model):
    nome = models.CharField('Item', max_length=100, null=False)
    descricao = models.CharField('Descrição', max_length=200, null=False)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens da Guarderia'

    def __str__(self):
        return self.nome


class Guarderia(Servico):
    valor = models.Empty()
    vencimento = models.DateField()

    class Meta:
        verbose_name = 'Guarderia'
        verbose_name_plural = 'Guarderia'


    def __str__(self):
        return self.cliente.nome

    def valor_total(self):
        qs = self.guarderia_det.filter(guarderia=self.pk).values_list('valor') or 0
        t = 0 if isinstance(qs, int) else (sum(map(lambda q: q[0], qs)))
        if t > self.desconto:
            t -= self.desconto
        else:
            t = 0
        return "R$ %s" % number_format(t, 2)

class DetalheGuarderia(models.Model):
    guarderia = models.ForeignKey(Guarderia, related_name='guarderia_det')
    item = models.ForeignKey(Item, verbose_name='itens')
    valor = models.DecimalField('Valor do item', max_digits=6, decimal_places=2, default=0)

    def get_subtotal(self):
        return self.valor

#================================{Aluguel}================================#
class TipoPrancha(TimeStampedModel):
    descricao = models.CharField('Descrição', max_length=200, null=False)

    class Meta:
        verbose_name = 'Tipo de Prancha'
        verbose_name_plural = 'Tipos de Prancha'

    def __str__(self):
        return self.descricao

class Prancha(TimeStampedModel):
    descricao = models.CharField('Descrição', max_length=200, null=False)
    altura = models.DecimalField('Altura', max_digits=6, decimal_places=2, default=0)
    litragem = models.DecimalField('Litragem', max_digits=6, decimal_places=2, default=0)
    tipo_prancha = models.ForeignKey(TipoPrancha, verbose_name='Tipo de Prancha')

    class Meta:
        verbose_name = 'Prancha'
        verbose_name_plural = 'Pranchas'

    def __str__(self):
        return self.descricao


class Aluguel(Servico):

    class Meta:
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Alugueis'

    def __str__(self):
        return self.cliente.nome

    def valor_total(self):
        qs = self.aluguel_det.filter(aluguel=self.pk).values_list('valor') or 0
        t = 0 if isinstance(qs, int) else (sum(map(lambda q: q[0], qs)))
        if t > self.desconto:
            t -= self.desconto
        else:
            t = 0
        return "R$ %s" % number_format(t, 2)

    valor = property(valor_total)

class DetalheAluguel(models.Model):
    aluguel = models.ForeignKey(Aluguel, related_name='aluguel_det')
    prancha = models.ForeignKey(Prancha,verbose_name='pranchas')
    valor = models.DecimalField('Valor do item', max_digits=6, decimal_places=2, default=0)

    def get_subtotal(self):
        return self.valor

#=================================={Aulas}================================#
class AulaMarcada(TimeStampedModel):
    horario = models.DateTimeField()

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas Marcadas'

    def __str__(self):
        data_hora = self.horario.__str__().split(' ')
        data = data_hora[0].split('-')
        hora = data_hora[1][:5]
        aula = 'Data: ' + data[2] + '/' + data[1] + '/' + data[0] + ' Hora: ' + hora
        return aula



class Aula(Servico):
    def __str__(self):
        return self.cliente.nome

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def calcula_total(self):
        qs = self.aula_det.filter(aula=self.pk).values_list('valor') or 0
        t = 0 if isinstance(qs, int) else (sum(map(lambda q: q[0], qs)))
        if t > self.desconto:
            t -= self.desconto
        else:
            t = 0
        return t

    def valor_total(self):
        return "R$ %s" % number_format(self.calcula_total(), 2)
    valor = property(calcula_total)



class DetalheAula(models.Model):

    aula = models.ForeignKey(Aula, related_name='aula_det')
    aula_marcada = models.ForeignKey(AulaMarcada, related_name='aula_marcada_det')
    professor = models.ForeignKey(Professor, related_name='professor_det')
    valor = models.DecimalField('Valor do item', max_digits=6, decimal_places=2, default=40)

    def get_subtotal(self):
        return self.valor
