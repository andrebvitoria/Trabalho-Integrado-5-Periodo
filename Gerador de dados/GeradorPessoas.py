from faker import Faker
import random
import threading


class ThreadsPessoa(threading.Thread):
    def __init__(self, arquivo, quantidade):
        threading.Thread.__init__(self)
        self.arquivo = arquivo
        self.qtd = quantidade

    def run(self):
        pessoa = Pessoa()
        pessoas = list()

        for i in range(0, self.qtd):
            pessoa.gerar()
            pessoas.append(pessoa.__str__())

        file = Arquivo()
        file.salvar(self.arquivo, pessoas)

        return


class Arquivo(object):
    def salvar(self, dir, lst):
        arq = open(dir, 'wt', encoding='utf8')
        for elem in lst:
            arq.write(elem + '\n')
        arq.close()


class Pessoa(object):
    gerador = Faker()
    nome = None
    data_nascimento = None
    cpf = None
    genero = None
    email = None
    telefone = None
    celular = None
    emergencia = None

    def gerar(self):
        self.genero = ['M', 'F'][random.randint(0, 1)]
        if self.genero == 'M':
            self.nome = self.gerador.name_male()
        else:
            self.nome = self.gerador.name_female()
        self.data_nascimento = self.gerador.date()
        self.cpf = str(random.randint(10000000000, 99999999999))
        self.email = self.gerador.email()
        self.telefone = str(random.randint(10000000, 99999999))
        self.celular = str(random.randint(100000000, 999999999))
        self.emergencia = str(random.randint(10000000, 99999999))

    def __str__(self):
        return self.nome + ';' + self.genero + ';' + self.data_nascimento + ';' + self.cpf + ';' + self.email + ';' + self.telefone + ';' + self.celular + ';' + self.emergencia


def main():
    quantidade = 500000

    ThreadsPessoa('Dados/aluno.csv', quantidade).start()
    ThreadsPessoa('Dados/professor.csv', quantidade).start()
    ThreadsPessoa('Dados/vendedor.csv', quantidade).start()


if __name__ == '__main__':
    main()