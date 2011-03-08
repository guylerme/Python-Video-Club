import unittest
from emprestimo import Emprestimo

class Test_Emprestimo(unittest.TestCase):
    empr = Emprestimo()
    assert empr != None, "Classe inicializada incorretamente quando construtor nao tem parametro"

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( Test_Emprestimo ) )
    return suite

if __name__ == '__main__':
    unittest.main()

