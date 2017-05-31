
import random

arq = open('item-venda.csv', 'w')
d = ['2001-02-16 20:38:40', '2016-04-17 22:38:42',\
'2011-05-16 16:38:40', '2009-07-13 13:39:42']
txt = []
txt.append('quantidade'+';'+'valor_venda'+';'+'desconto'+';'+'id_produto'+';'+'id_venda\n')

for i in range(100000):
	id_venda = random.randint(1,1500000)
	#id_produto = random.randint(1,25000)
	quantidade = random.randint(1,100)
	desconto = round(random.uniform(0,20),2)
	valor_venda = round(random.uniform(20,5000),2)
	
	txt.append(str(quantidade)+';'+str(valor_venda)+';'+str(desconto)+';'+str(1)+';'+str(id_venda)+'\n')

arq.writelines(txt)
arq.close()
