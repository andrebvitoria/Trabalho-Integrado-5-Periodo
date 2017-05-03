from django.db import models
from django.utils import timezone


class Pessoa(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False)
    email = models.EmailField()
    genero_choice = ('Masculino', 'Masculino'), ('Feminino', 'Feminino')
    genero = models.CharField(max_length=9, choices=genero_choice)
    celular = models.IntegerField()
    telefone = models.IntegerField()
    emergencia = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Aluno(Pessoa):
    def __str__(self):
        return self.nome


class Professor(Pessoa):
    def __str__(self):
        return self.nome


class Servico(models.Model):
    data = models.DateField()
    valor = models.FloatField()
    desconto = models.FloatField()
    cliente = models.ForeignKey(Aluno)
    vendedor = models.ForeignKey('auth.User')

    def prestar_servico(self, pagamento):
        troco = pagamento - self.valor + self.desconto
        return troco

    class Meta:
        abstract = True


class Item(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=200, null=False)
    data_entrada = models.DateField()

    def __str__(self):
        return self.nome


class Guarderia(Servico):
    item = models.ForeignKey(Item, blank=True, null=False)
    vencimento = models.DateField()

    def prestar_servico(self, pagamento):
        troco = pagamento - self.valor + self.desconto
        if troco > -1:
            self.vencimento = models.DateField(default=timezone.now() + timezone.timedelta(days=30))
        return troco

    def renovar(self, pagamento):
        return self.prestar_servico(self, pagamento)

    def __str__(self):
        return self.cliente.nome


class TipoPrancha(models.Model):
    descricao = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.descricao


class Prancha(models.Model):
    descricao = models.CharField(max_length=200, null=False)
    tipo_prancha = models.ForeignKey(TipoPrancha)
    altura = models.CharField(max_length=10, null=False)
    litragem = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.descricao


class Aluguel(Servico):
    prancha = models.ManyToManyField(Prancha)

    def __str__(self):
        return self.cliente.nome


class Aula(models.Model):
    professor = models.ManyToManyField(Professor)
    alunos = models.ManyToManyField(Aluno)
    horario = models.DateTimeField()

    def __str__(self):
        data_hora = self.horario.__str__().split(' ')
        data = data_hora[0].split('-')
        hora = data_hora[1][:5]
        aula = data[2] + '/' + data[1] + '/' + data[0] + ' ' + hora
        return aula


class AulaAvulsa(Servico):
    aula = models.ForeignKey(Aula)

    def __str__(self):
        return self.cliente.nome + ' (' + self.data.__str__() + ')'


class PacoteAula(Servico):
    aulas_restantes = models.IntegerField()
    aulas = models.ManyToManyField(Aula)

    def __str__(self):
        return self.cliente.nome
