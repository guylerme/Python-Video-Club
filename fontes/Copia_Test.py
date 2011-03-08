import unittest
from copia import Copia

class Copia_Test(unittest.TestCase):
    def testCopia(self):
        copia =  Copia(1, 'As trancas do careca', '2:30', 2008, 'drama', 'Jim Carey', 'Brad Pitt', 'Angelina Jolie', '05/02/2010', 'bom', 5135)
        assert copia != None, "nao existe a classe Copia"

    def testNewattr(self):
        assert copia.newattr != None, "Nao inicializou newattr"

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(Copia_Test))
        return suite

if __name__ == '__main__':
    unittest.main()