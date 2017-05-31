import random

def gera_entrada():
	arq_entrada = open('entrada.csv', 'w')
	d = ['2001-02-16 20:38:40', '2016-04-17 22:38:42',\
	'2011-05-16 16:38:40', '2009-07-13 13:39:42', '2009-07-17 14:39:42',\
	'2016-04-28 18:36:44']
	txt = []
	txt.append('data\n')
	for i in range(len(d)):
		txt.append(str(d[i])+'\n')

	arq_entrada.writelines(txt)
	arq_entrada.close()

def gera_cor():
	arq_cor = open('cor.csv', 'w')
	c = ['azul', 'branco', 'rosa', 'amarelo', 'verde']
	txt_cor = []
	txt_cor.append('descricao\n')
	for i in range(len(c)):
		txt_cor.append(str(c[i])+'\n')

	arq_cor.writelines(txt_cor)
	arq_cor.close()


def gera_tipo_camisa():
	arq_camisa = open('camisa.csv', 'w')
	txt_tipo_camisa = []
	txt_tipo_camisa.append('descricao\n')
	for i in range(5):
		txt_tipo_camisa.append('tipo_camisa'+str(i)+'\n')

	arq_camisa.writelines(txt_tipo_camisa)
	arq_camisa.close()


def gera_tipo_prancha():
	arq_tipo_prancha = open('tipo_prancha.csv', 'w')
	p = ['shortboard', 'evolution', 'fish', 'retro fish', 'mini malibu', 'longboard', 'funboard']
	txt_tipo_prancha = []
	txt_tipo_prancha.append('descricao\n')
	for i in range(len(p)):
		txt_tipo_prancha.append(p[i]+'\n')

	arq_tipo_prancha.writelines(txt_tipo_prancha)
	arq_tipo_prancha.close()


def gera_tamanho():
	arq_tamanho = open('tamanho.csv', 'w')
	t = ['PP', 'P', 'M', 'G', 'GG']
	txt_tamanho = []
	txt_tamanho.append('descricao\n')
	for i in range(len(t)):
		txt_tamanho.append(t[i]+'\n')

	arq_tamanho.writelines(txt_tamanho)
	arq_tamanho.close()

def gera_categoria():
	arq_categoria = open('categoria.csv', 'w')
	txt_categoria = []
	txt_categoria.append('descricao\n')
	for i in range(20):
		txt_categoria.append('categoria'+str(i+1)+'\n')

	arq_categoria.writelines(txt_categoria)
	arq_categoria.close()


gera_entrada()
gera_cor()
gera_tipo_camisa()
gera_tipo_prancha()
gera_tamanho()
gera_categoria()