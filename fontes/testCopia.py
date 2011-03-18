import unittest
import datetime
import time
import copia

class Copia_Test(unittest.TestCase):

    def setUp(self):
        self.copia =  copia.Copia(1, 'As trancas do careca', '2:30', 2009, 'drama',      'Jim Carey', 'Brad Pitt', 'Angelina Jolie', '18/03/2011', 'OTIMA', 5135.2)

    def tearDown(self):
        self.copia = None

    def testCopiaAno(self):
        """COPIA: Erro ao configurar o ano"""
        self.assertEqual(self.copia.ano, 2008)

    def testCopiaConcineInteger(self):
        """COPIA: Concine deve ser um inteiro"""
        self.assertEqual(int(self.copia.concine), self.copia.concine)

    def testCopiaDataValida(self):
        """COPIA: Data deve ser valida e ser <= hoje"""
        hoje = datetime.datetime.today()
        data = datetime.datetime(*time.strptime(self.copia.dataAquisicao, "%d/%m/%Y")[0:5])
        assert data <= hoje, "Data deve ser valida e ser <= hoje"

    def testCopiaEstado(self):
        """COPIA: Verifica se o estado da fita eh bom ou ruim"""
        assert self.copia.estado.lower() == "bom" or self.copia.estado.lower() == "ruim", 'Estado da copia deve ser bom ou ruim'

    def testCopiaStrings(self):
        """COPIA: setElenco deve emitir erro quando faltar informacao"""
        self.assertRaises(copia.errCopiaMissingValues, self.copia.setElenco, '','','')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(Copia_Test))
        return suite

if __name__ == '__main__':
    unittest.main()