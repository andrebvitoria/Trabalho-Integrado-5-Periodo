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
        contato = self.obj
        contatos = list()

        for i in range(0, self.qtd):
            contato.gerar()
            contatos.append(contato.__str__() + ';' + str(i))

        file = Arquivo()
        file.salvar(self.arquivo, contatos)

        return


class Arquivo(object):
    def salvar(self, dir, lst):
        arq = open(dir, 'wt', encoding='utf8')
        for elem in lst:
            arq.write(elem + '\n')
        arq.close()


class Contato(object):
    gerador = Faker()

    def __init__(self, start):
        self.id = start

    def gerar(self):
        self.id += 1
        self.tipo = random.randint(0, 8)
        if self.tipo == 8:
            self.contato = self.gerador.email()
        elif 4 < self.tipo < 8:
            self.contato = self.gerador.name().replace(' ', '.')
        else:
            self.contato = str(random.randint(10000000, 99999999))
        self.tipo = str(self.tipo + 1)

    def __str__(self):
        return self.contato + ';' + self.tipo + ';' + str(self.id)





def main():
    tipo_contato = ['Telefone responsavel', 'Telefone de emergencia', 'Celular', 'Telefone residencial',
                    'Telefone do Trabalho', 'Facebook', 'Twitter', 'Instagram', 'Email']
    Arquivo().salvar('Dados/tipo_contato.csv',tipo_contato)
    quantidade = 100000

    start = 1000000

    ThreadsPessoa('Dados/contato_aluno.csv', quantidade, Contato(start)).start()
    ThreadsPessoa('Dados/contato_vendedor.csv', quantidade, Contato(start * 3)).start()
    ThreadsPessoa('Dados/contato_professor.csv', quantidade, Contato(start * 2)).start()


if __name__ == '__main__':
    main()
