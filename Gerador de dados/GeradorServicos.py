from faker import Faker
import random
import threading


class Arquivo(object):
    def salvar(self, dir, lst):
        arq = open(dir, 'wt', encoding='utf8')
        for elem in lst:
            arq.write(elem + '\n')
        arq.close()


class ThreadsServico(threading.Thread):
    def __init__(self, servico, quantidade):
        threading.Thread.__init__(self)
        self.servico = servico
        self.qtd = quantidade

    def run(self):
        for i in range(0, self.qtd):
            self.servico.gerar()
            self.servico.guardar()

        dados = self.servico.get_dados()
        for arquivo in dados:
            Arquivo().salvar('Dados/' + arquivo + '.csv', dados[arquivo])

        return


class Servico(object):
    gerador = Faker()

    class Meta:
        abstract = True

    def guardar(self):
        pass

    def get_dados(self):
        pass

    def gerar(self):
        self.vendedor = str(random.randint(1, 100000))
        self.cliente = str(random.randint(1, 100000))
        self.data = '2017' + self.gerador.date()[4:]
        self.desconto = '0'

    def __str__(self):
        return self.vendedor + ';' + self.cliente + ';' + self.data + ';' + self.desconto


class DetalheServico(object):
    id_detalhe = 0
    def gerar(self):
        self.id_detalhe += 1
        self.valor = str(random.randint(50, 200))

    def __str__(self):
        return self.valor + ';' + str(self.id_detalhe) + ';' + str(self.id_detalhe)


class Item(object):
    cont = 0

    def gerar(self):
        self.cont += 1
        self.nome = 'Item' + str(self.cont)
        self.descricao = 'Descrição do ' + self.nome

    def __str__(self):
        return self.nome + ';' + self.descricao


class Guarderia(Servico):
    dados = {'guarderia': list(), 'detalhe_garderia': list(), 'item': list()}
    item = Item()
    detalhe = DetalheServico()

    def gerar(self):
        self.vencimento = '2018' + self.gerador.date()[4:]
        super().gerar()
        self.item.gerar()
        self.detalhe.gerar()

    def __str__(self):
        return super().__str__() + ';' + self.vencimento

    def guardar(self):
        self.dados['guarderia'].append(self.__str__())
        self.dados['detalhe_garderia'].append(self.detalhe.__str__())
        self.dados['item'].append(self.item.__str__())

    def get_dados(self):
        return self.dados


class TipoPrancha(object):
    def gerar(self):
        tipos = ['Funboard', 'Evolution', 'Fish', 'Retro Fish', 'Mini Malibu', 'Longboard', 'Shortboard', 'Gun', 'Performance']
        self.descricao = tipos[random.randint(1, len(tipos)) - 1]

    def __str__(self):
        return self.descricao


class Prancha(object):
    id = 0
    tipo = TipoPrancha()

    def gerar(self):
        self.id += 1
        self.litragem = str(random.randint(18, 75))
        self.altura = str(random.randint(6, 10))
        self.tipo.gerar()

    def __str__(self):
        return self.litragem + ';' + self.altura + ';' + str(self.id)


class Aluguel(Servico):
    dados = {'aluguel': list(), 'prancha': list(), 'tipo_prancha': list(), 'detalhe_aluguel': list()}
    prancha = Prancha()
    detalhe = DetalheServico()

    def gerar(self):
        super().gerar()
        self.prancha.gerar()
        self.detalhe.gerar()
        return

    def guardar(self):
        self.dados['aluguel'].append(self.__str__())
        self.dados['prancha'].append(self.prancha.__str__())
        self.dados['tipo_prancha'].append(self.prancha.tipo.__str__())
        self.dados['detalhe_aluguel'].append(self.detalhe.__str__())

    def get_dados(self):
        return self.dados


class AulaMarcada(object):
    gerador = Faker()

    def gerar(self):
        self.horario = '2017' + self.gerador.date()[4:]
        self.data = self.gerador.time()

    def __str__(self):
        return self.horario + ';' + self.data


class Aula(Servico):
    dados = {'aula': list(), 'aulas_marcadas': list(), 'detalhe_aula': list()}
    detalhe = DetalheServico()
    aula_marcada = AulaMarcada()

    def gerar(self):
        super().gerar()
        self.detalhe.gerar()
        self.aula_marcada.gerar()
        self.professor = str(random.randint(1, 100000))

    def __str__(self):
        return super().__str__() + ';' + self.professor

    def guardar(self):
        self.dados['aula'].append(self.__str__())
        self.dados['aulas_marcadas'].append(self.aula_marcada.__str__())
        self.dados['detalhe_aula'].append(self.detalhe.__str__() + ';' + str(random.randint(1, 100000)))

    def get_dados(self):
        return self.dados


def main():
    quantidade = 500000

    ThreadsServico(Guarderia(), quantidade).start()
    ThreadsServico(Aluguel(), quantidade).start()
    ThreadsServico(Aula(), quantidade).start()

    return

if __name__ == '__main__':
    main()