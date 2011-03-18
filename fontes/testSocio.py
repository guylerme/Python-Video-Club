import unittest
from socio import Socio

class Socio_Test(unittest.TestCase):
    def testSocioName(self):
        """SOCIO: Testar nome"""
        socio = Socio('Teste', 1, '27223322')
        assert socio.nome != None, "nao tem nome"

    def testSocioInscricao(self):
        """SOCIO: Testar inscricao"""
        socio = Socio('Teste',1, None)
        assert socio.inscricao != None, "nao tem inscricao!"

    def testSocioTelefone(self):
        """SOCIO: Testar telefone"""
        socio = Socio('Teste',1, '27223344')
        assert socio.telefone != None, "nao tem telefone!"

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(Socio_Test))
        return suite

if __name__ == '__main__':
    unittest.main()
