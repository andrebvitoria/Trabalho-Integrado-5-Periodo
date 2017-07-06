from faker import Faker
import random
import threading


class ThreadsPessoa(threading.Thread):
    def __init__(self, arquivo, quantidade, obj):
        threading.Thread.__init__(self)
        self.arquivo = arquivo
        self.qtd = quantidade
        self.obj = obj

    def run(self):
        pessoa = self.obj
        pessoas = list()

        for i in range(0, self.qtd):
            print("%d concluidos" % i)
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


class Aluno(object):
    gerador = Faker()
    id = 1000000
    nome = None
    data_nascimento = None
    cpf = None
    genero = None
    responsavel = None


    def gerar(self):
        self.id += 1
        self.genero = ['M', 'F'][random.randint(0, 1)]
        if self.genero == 'M':
            self.nome = self.gerador.name_male()
        else:
            self.nome = self.gerador.name_female()
        self.data_nascimento = self.gerador.date()
        self.cpf = str(random.randint(10000000000, 99999999999))
        self.responsavel = self.gerador.name_male()

    def __str__(self):
        return self.nome + ';' + self.genero + ';' + self.data_nascimento + ';' + self.cpf + ';' + self.responsavel + ';' + str(self.id)


class Professor(object):
    gerador = Faker()
    id = 2000000
    nome = None
    data_nascimento = None
    cpf = None
    genero = None
    ativo = None

    def gerar(self):
        self.id += 1
        self.genero = ['M', 'F'][random.randint(0, 1)]
        if self.genero == 'M':
            self.nome = self.gerador.name_male()
        else:
            self.nome = self.gerador.name_female()
        self.data_nascimento = self.gerador.date()
        self.cpf = str(random.randint(10000000000, 99999999999))
        self.ativo = ['True', 'False'][random.randint(0, 1)]

    def __str__(self):
        return self.nome + ';' + self.genero + ';' + self.data_nascimento + ';' + self.cpf + ';' + self.ativo + ';' + str(self.id)


class Vendedor(object):
    gerador = Faker()
    id = 3000000
    nome = None
    data_nascimento = None
    cpf = None
    genero = None
    login = None
    senha = None


    def gerar(self):
        self.id += 1
        self.genero = ['M', 'F'][random.randint(0, 1)]
        if self.genero == 'M':
            self.nome = self.gerador.name_male()
        else:
            self.nome = self.gerador.name_female()
        self.data_nascimento = self.gerador.date()
        self.cpf = str(random.randint(10000000000, 99999999999))
        self.login = self.nome.split(' ')[0] + '.' + self.nome.split(' ')[-1]
        self.senha = self.gerador.password()


    def __str__(self):
        return self.nome + ';' + self.genero + ';' + self.data_nascimento + ';' + self.cpf + ';' + self.login + ';' + self.senha + ';' + str(self.id)


def main():
    quantidade = 100000

    ThreadsPessoa('Dados/aluno.csv', quantidade, Aluno()).start()
    ThreadsPessoa('Dados/professor.csv', quantidade, Professor()).start()
    ThreadsPessoa('Dados/vendedor.csv', quantidade, Vendedor()).start()


if __name__ == '__main__':
    main()