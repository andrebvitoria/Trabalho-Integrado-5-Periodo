import random

from faker import Factory, Faker

#gerar nomes em pt-br
fake = Factory.create('pt_PT')
f = Faker()

arq = open('cliente.csv', 'w')

txt = []
txt.append('nome'+';'+'idade\n')

for i in range(100000):
	idade = random.randint(12,70)
	txt.append(fake.name()+' '+f.name()+';'+str(idade)+'\n')

arq.writelines(txt)

arq.close()
