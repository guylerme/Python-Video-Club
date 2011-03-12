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
        assert empr.valorFixo == 5, 'Valor fixo corrompido'

##    def test_data_fim(self):
##        empr = Emprestimo()
##        empr.devolverFita(1)
##        assert self.empr.dataFim == None, 'Devolucao da fita nao registrada'

    def test_valor_pago_sem_multa(self):
        data = datetime.date.today()

## para refactoring: o -4 deve ser feito na data, nao no dia...
        self.dataInicio = str(data.day - 4) + '/' + str(data.month) +'/' + str(data.year)

        empr = Emprestimo()
        empr.pegarFita(1,self.dataInicio,1)
        empr.devolverFita(1)
        assert empr.valorPago == empr.valorFixo, 'Valor pago com juros indevidamente'

    def suite():
        suite = unittest.TestSuite()
        suite.addTest( unittest.makeSuite( Test_Emprestimo ) )
        return suite

if __name__ == '__main__':
    unittest.main()

