
import random

arq = open('item-entrada.csv', 'w')

txt = []
txt.append('id_produto'+';'+'id_entrada\n')

for i in range(100000):
	#id_produto = random.randint(1,100000)
	id_entrada = random.randint(1,6)
	txt.append(str(1)+';'+str(id_entrada)+'\n')

arq.writelines(txt)
arq.close()