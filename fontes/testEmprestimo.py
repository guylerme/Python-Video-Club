import unittest
import time, datetime
from emprestimo import Emprestimo

class Test_Emprestimo(unittest.TestCase):
    def test_valor_fixo(self):
        """EMPREST: Validar inicializacao do valor fixo"""
        empr = Emprestimo()
        assert empr.valorFixo == 4, 'Valor fixo corrompido'

    def test_valor_pago_sem_multa(self):
        """EMPREST: Valor pago nao deve ter multa quando pago em dia"""
        empr = Emprestimo()
        now = datetime.date.today()
        prazo = datetime.timedelta(days = empr.diasPrazo) #Usa a regra de negocio para saber se houve atraso na entrega
        di = now - prazo
        self.dataInicio = str(di.day) + '/' + str(di.month) +'/' + str(di.year)
        empr.pegarFita(1,self.dataInicio,1)
        empr.devolverFita(1)
        self.assertEqual(empr.valorPago,empr.valorFixo, 'Valor pago com juros')

    def test_valor_pago_com_multa(self):
        """EMPREST: Valor pago com multa"""
        empr = Emprestimo()
        now = datetime.date.today()

##Usa a regra de negocio com delta para simular atraso na entrega
        prazo = datetime.timedelta(days = empr.diasPrazo + 5)
        di = now - prazo
## Refatorado
        self.dataInicio = str(di.day) + '/' + str(di.month) +'/' + str(di.year)
        empr.pegarFita(1,self.dataInicio,1)
        empr.devolverFita(1)
        #assert empr.valorPago == empr.valorFixo, 'Valor pago com juros'
        self.assertEqual( empr.valorPago, empr.valorFixo, 'Valor pago com multa')

    #suite: usado para compor o conjunto de testes a serem executados automaticamente
    #quando formos executar todos os testes juntos
    def suite():
        suite = unittest.TestSuite()
        suite.addTest( unittest.makeSuite( Test_Emprestimo ) )
        return suite

if __name__ == '__main__':
    unittest.main()