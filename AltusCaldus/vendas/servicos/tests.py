from django.test import TestCase
from .models import*
from django.contrib.auth.models import User

class GuarderiaTest(TestCase):
    def setUp(self):
        c = Aluno.objects.create(genero='M', cpf='12344', nome='juliana kanezaki', celular = '3234545', emergencia = '65767',
                                    email='juliana@gmail.com', telefone='3243546', data_nascimento='1998-12-09')
        v = User.objects.create()
        i = Item.objects.create(nome='prancha', descricao='azul')

        self.g1 = Guarderia.objects.create(cliente=c, vendedor=v, data = '2017-05-25', vencimento = '2017-05-25', desconto = 5)
        self.det1 = DetalheGuarderia.objects.create(item=i, valor=50, guarderia=self.g1)
        self.det2 = DetalheGuarderia.objects.create(item=i, valor=30, guarderia=self.g1)

        self.g2 = Guarderia.objects.create(cliente=c, vendedor=v, data='2017-05-25', vencimento='2017-05-25', desconto = 70)
        self.det3 = DetalheGuarderia.objects.create(item=i, valor=30, guarderia=self.g2)


    def testSubTotal(self):
        self.assertEquals(self.det1.get_subtotal(), 50)
        self.assertEquals(self.det2.get_subtotal(), 30)
        self.assertEquals(self.det3.get_subtotal(), 30)

    def testTotal(self):
        self.assertEquals(self.g1.valor_total(), 'R$ 75,00')
        #self.assertEquals(self.g1.valor, 75)
        self.assertEquals(self.g2.valor_total(), 'R$ 0,00')

