from faker import Faker
import random
import threading


class Arquivo(object):
    @staticmethod
    def salvar(dir, lst):
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
            print("%d concluidos" % i)
            self.servico.gerar()
            self.servico.guardar()

        dados = self.servico.get_dados()
        for arquivo in dados:
            if arquivo == 'aula_marcada':
                print(dados[arquivo])
                input()
            Arquivo.salvar('Dados/' + arquivo + '.csv', dados[arquivo])

        return


# ============{ SERVIÇO }============ #

class Servico(object):
    def __init__(self, id, max):
        self.max = max
        self.id = id
        self.reboot = id
        self.gerador = Faker()

    class Meta:
        abstract = True

    def guardar(self):
        pass

    def get_dados(self):
        pass

    def gerar(self):
        self.id += 1
        self.vendedor = str(random.randint(1, self.max) + 3000000)
        self.cliente = str(random.randint(1, self.max) + 1000000)
        data = self.gerador.date()[4:]
        if data == '-02-29':
            data = data[:-1] + '8'
        self.data = '2017' + data
        self.desconto = '0'

    def __str__(self):
        return self.vendedor + ';' + self.cliente + ';' + self.data + ';' + self.desconto


class ItemServico(object):
    def __init__(self, id, max):
        self.reboot = id
        self.id_detalhe = id
        self.max = max

    def gerar(self):
        if self.id_detalhe == self.reboot + self.max:
            self.id_detalhe = self.reboot
        self.id_detalhe += 1
        self.valor = str(random.randint(50, 200))

    def __str__(self):
        return self.valor + ';' + str(self.id_detalhe)


# ============{ GUARDERIA }============ #

class Item(object):
    def __init__(self, id, max):
        self.max = max
        self.reboot = id
        self.cont = id
        self.check = True

    def gerar(self):
        if self.cont < self.reboot + self.max:
            self.cont += 1
            self.nome = 'Item' + str(self.cont)
            self.descricao = 'Descrição do ' + self.nome
        else:
            self.check = False

    def __str__(self):
        if self.check:
            return self.nome + ';' + self.descricao + ';' + str(self.cont)
        return ''

class Guarderia(Servico):
    def __init__(self, id, max):
        super().__init__(id, max)
        self.dados = {'guarderia': list(), 'detalhe_garderia': list(), 'item': list()}
        self.item = Item(self.id, self.max)
        self.detalhe = ItemServico(self.id, self.max)

    def gerar(self):
        super().gerar()
        data = self.gerador.date()[4:]
        if data == '-02-29':
            data = data[:-1] + '8'
        self.vencimento = '2018' + data
        self.item.gerar()
        self.detalhe.gerar()

    def __str__(self):
        return super().__str__() + ';' + self.vencimento + ';' + str(self.id)

    def guardar(self):
        self.dados['guarderia'].append(self.__str__())
        item = self.item.__str__()
        if item != '':
            self.dados['item'].append(self.item.__str__())
            self.dados['detalhe_garderia'].append(self.detalhe.__str__() + ';' + str(self.item.cont))
        else:
            self.dados['detalhe_garderia'].append(self.detalhe.__str__() + ';' + str(random.randint(1, self.item.max) + self.item.reboot))

    def get_dados(self):
        return self.dados


# ============{ ALUGUEL }============ #

class TipoPrancha(object):
    def gerar(self):
        tipos = ['Funboard', 'Evolution', 'Fish', 'Retro Fish', 'Mini Malibu', 'Longboard', 'Shortboard', 'Gun',
                 'Performance']
        id = random.randint(1, len(tipos) - 1)
        self.descricao = tipos[id]
        return id

    def __str__(self):
        return self.descricao


class Prancha(object):
    def __init__(self, id, max):
        self.max = max
        self.id = id
        self.reboot = id
        self.check = True
        self.tipo = TipoPrancha()

    def gerar(self):
        if self.id < self.reboot + self.max:
            self.id += 1
            self.litragem = str(random.randint(18, 75))
            self.altura = str(random.randint(6, 10))
            self.id_prancha = self.tipo.gerar()
        else:
            self.check = False

    def __str__(self):
        if self.check:
            return self.litragem + ';' + self.altura + ';' + str(self.id_prancha) + ';' + str(self.id)
        else:
            return ''


class Aluguel(Servico):
    def __init__(self, id, max):
        super().__init__(id, max)
        self.dados = {'aluguel': list(), 'prancha': list(), 'tipo_prancha': list(), 'detalhe_aluguel': list()}
        self.prancha = Prancha(id, max)
        self.detalhe = ItemServico(id, max)

    def gerar(self):
        super().gerar()
        self.prancha.gerar()
        self.detalhe.gerar()
        return

    def guardar(self):
        self.dados['aluguel'].append(self.__str__() + ';' + str(self.id))
        prancha = self.prancha.__str__()
        if prancha != '':
            self.dados['prancha'].append(prancha)
            self.dados['detalhe_aluguel'].append(self.detalhe.__str__() + ';' + str(self.prancha.id))
        else:
            self.dados['detalhe_aluguel'].append(self.detalhe.__str__() + ';' +
                                                 str(random.randint(1, self.prancha.max) + self.reboot))
        if self.prancha.tipo.__str__() not in self.dados['tipo_prancha']:
            self.dados['tipo_prancha'].append(self.prancha.tipo.__str__())

    def get_dados(self):
        return self.dados


# ============={ AULA }=========== #

class AulaMarcada(object):
    def __init__(self, id, max):
        self.id = id
        self.max = max
        self.reboot = id
        self.check = True
        self.gerador = Faker()

    def gerar(self):
        if self.id < self.reboot + self.max:
            self.id += 1
            self.horario = '2017' + self.gerador.date()[4:]
            self.data = self.gerador.time()
        else:
            self.check = False

    def __str__(self):
        if self.check:
            return self.horario + ' ' + self.data + ';' + str(self.id)
        return ''


class Aula(Servico):
    def __init__(self, id, max):
        super().__init__(id, max)
        self.dados = {'aula': list(), 'aulas_marcadas': list(), 'detalhe_aula': list()}
        self.detalhe = ItemServico(id, max)
        self.aula_marcada = AulaMarcada(id, max)

    def gerar(self):
        super().gerar()
        self.detalhe.gerar()
        self.aula_marcada.gerar()
        self.professor = str(random.randint(1, self.max) + 2000000)

    def __str__(self):
        return super().__str__() + ';' + str(self.id)

    def guardar(self):
        self.dados['aula'].append(self.__str__())
        aula_marcada = self.aula_marcada.__str__()
        if aula_marcada == '':
            self.dados['detalhe_aula'].append(
                self.detalhe.__str__() + ';' + str(random.randint(1, self.max) + self.reboot) + ';' + self.professor)
        else:
            self.dados['aulas_marcadas'].append(aula_marcada)
            self.dados['detalhe_aula'].append(
                self.detalhe.__str__() + ';' + str(self.aula_marcada.id) + ';' + self.professor)

    def get_dados(self):
        return self.dados


def main():
    quantidade = 500000
    qtd_pessoas = 100000
    ThreadsServico(Guarderia(1000000, qtd_pessoas), quantidade).start()
    ThreadsServico(Aluguel(2000000, qtd_pessoas), quantidade).start()
    ThreadsServico(Aula(3000000, qtd_pessoas), quantidade).start()

    return


if __name__ == '__main__':
    main()
