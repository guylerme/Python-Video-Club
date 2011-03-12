import unittest
import time, datetime
from emprestimo import Emprestimo

class Test_Emprestimo(unittest.TestCase):

##    def setUp(self):
##        empr = Emprestimo()

##    #def test_emprestimo(self):
##        #empr = Emprestimo()
##        #assert self.empr != None, "Classe inicializada incorretamente quando construtor nao tem parametro"

    def test_valor_fixo(self):
        empr = Emprestimo()
        assert empr.valorFixo == 4, 'Valor fixo corrompido'

##    def test_data_fim(self):
##        empr = Emprestimo()
##        empr.devolverFita(1)
##        assert self.empr.dataFim == None, 'Devolucao da fita nao registrada'

    def test_valor_pago_sem_multa(self):
        empr = Emprestimo()
        now = datetime.date.today()

        prazo = datetime.timedelta(days = empr.diasPrazo) #Usa a regra de negocio para saber se houve atraso na entrega
        di = now - prazo
## Refatorado
        self.dataInicio = str(di.day) + '/' + str(di.month) +'/' + str(di.year)
        empr.pegarFita(1,self.dataInicio,1)
        empr.devolverFita(1)
        assert empr.valorPago == empr.valorFixo, 'Valor pago com juros'
        ##self.assertEqual(empr.valorPago, empr.valorFixo) #Exibe os valores em vez da mensagem, que pode ser o 3Âº parm.

    def test_valor_pago_com_multa(self):
        empr = Emprestimo()
        now = datetime.date.today()

##Usa a regra de negocio com delta para simular atraso na entrega
        prazo = datetime.timedelta(days = empr.diasPrazo + 5)
        di = now - prazo
## Refatorado
        self.dataInicio = str(di.day) + '/' + str(di.month) +'/' + str(di.year)
        empr.pegarFita(1,self.dataInicio,1)
        empr.devolverFita(1)
        assert empr.valorPago == empr.valorFixo, 'Valor pago com juros'

    #suite: usado para compor o conjunto de testes a serem executados automaticamente
    #quando formos executar todos os testes juntos
    def suite():
        suite = unittest.TestSuite()
        suite.addTest( unittest.makeSuite( Test_Emprestimo ) )
        return suite

if __name__ == '__main__':
    unittest.main()

