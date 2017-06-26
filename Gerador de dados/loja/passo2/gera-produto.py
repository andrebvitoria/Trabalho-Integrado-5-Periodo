
import random

arq_produto = open('produto.csv', 'w')
arq_camisa = open('camisas.csv', 'w')
arq_prancha = open('prancha.csv', 'w')
arq_cantina = open('cantina.csv', 'w')

txt_produto = []
txt_produto.append('nome'+';'+'valor_venda'+';'+'quantidade'+';'+'id_categoria\n')
for i in range(25000):
	id_categoria = random.randint(1,20)
	quantidade = random.randint(1,50)
	valor_venda = round(random.uniform(20,5000),2)
	txt_produto.append('produto'+str(i+1)+';'+str(valor_venda)+';'+str(quantidade)+';'+str(id_categoria)+'\n')

arq_produto.writelines(txt_produto)
arq_produto.close()

txt_camisa = []
txt_camisa.append('nome'+';'+'valor_venda'+';'+'quantidade'+';'+'id_categoria'+';'+'id_tipo_camisa'+';'+'id_cor'+';'+'id_tamanho\n')
for i in range(25000):
	id_categoria = random.randint(1,20)
	id_cor = random.randint(1,5)
	id_tamanho = random.randint(1,5)
	id_tipo_camisa = random.randint(1,5)
	quantidade = random.randint(1,50)
	valor_venda = round(random.uniform(20,50),2)
	txt_camisa.append('camisa'+str(i+1)+';'+str(valor_venda)+';'+str(quantidade)+';'+str(id_categoria)+';'+str(id_tipo_camisa)+';'+str(id_cor)+';'+str(id_tamanho)+'\n')

arq_camisa.writelines(txt_camisa)
arq_camisa.close()


txt_prancha = []
txt_prancha.append('nome'+';'+'valor_venda'+';'+'quantidade'+';'+'id_categoria'+';'+'litragem'+';'+'altura'+';'+'id_tipo_prancha\n')
for i in range(25000):
	id_categoria = random.randint(1,20)
	altura = round(random.uniform(1,10),2)
	litragem = round(random.uniform(1,10),2)
	id_tipo_prancha = random.randint(1,7)
	quantidade = random.randint(1,50)
	valor_venda = round(random.uniform(20,5000),2)
	txt_prancha.append('prancha'+str(i+1)+';'+str(valor_venda)+';'+str(quantidade)+';'+str(id_categoria)+';'+str(litragem)+';'+str(altura)+';'+str(id_tipo_prancha)+'\n')

arq_prancha.writelines(txt_prancha)
arq_prancha.close()

txt_cantina = []
txt_cantina.append('nome'+';'+'valor_venda'+';'+'quantidade'+';'+'id_categoria'+';'+'descricao\n')
for i in range(25000):
	id_categoria = random.randint(1,20)
	quantidade = random.randint(1,50)
	valor_venda = round(random.uniform(2,50),2)
	txt_cantina.append('produto_cantina'+str(i+1)+';'+str(valor_venda)+';'+str(quantidade)+';'+str(id_categoria)+';'+'descricao'+str(i+1)+'\n')

arq_cantina.writelines(txt_cantina)
arq_cantina.close()
