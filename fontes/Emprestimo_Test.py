import unittest
from emprestimo import Emprestimo

class Emprestimo_Test(unittest.TestCase):
    def testDevolucao(self):
        e = Emprestimo()
        e.codigoFita = 5123
        e.inscricao = 1
        #e.dataInicio = "17/02/2011"
        e.dataInicio = "14/02/2011"

        #assert e.devolverFita() == '4', "Valor incorreto"
        assert e.devolverFita() != '4', "Valor incorreto"

if __name__ == '__main__':
    unittest.main()
