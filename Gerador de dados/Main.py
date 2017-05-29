from GeradorPessoas import *
from GeradorServicos import *


def main():
    quantidade = 100000
    ThreadsServico(Guarderia(), quantidade).start()
    ThreadsServico(Aluguel(), quantidade).start()
    ThreadsServico(Aula(), quantidade).start()


    return


if __name__ == '__main__':
    main()