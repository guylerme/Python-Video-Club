import unittest
import datetime
import time
from copia import Copia

class Copia_Test(unittest.TestCase):
    copia =  Copia(1, 'As trancas do careca', '2:30', 2009, 'drama',
     'Jim Carey', 'Brad Pitt', 'Angelina Jolie', '18/03/2011', 'bom', 5135.2)

    def testCopiaAno(self):
        """Erro ao configurar o ano"""
        self.assertEqual(self.copia.ano, 2008)

    def testCopiaConcineInteger(self):
        """Concine deve ser um inteiro"""
        self.assertEqual(int(self.copia.concine), self.copia.concine)

    def testCopiaDataValida(self):
        """Data deve ser válida e ser <= hoje"""
        hoje = datetime.datetime.today()
        data = datetime.datetime(*time.strptime(self.copia.dataAquisicao, "%d/%m/%Y")[0:5])
        assert data <= hoje, "Data deve ser válida e ser <= hoje"

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(Copia_Test))
        return suite

if __name__ == '__main__':
    unittest.main()