import unittest
import principal

class test_copia_relatorios(unittest.TestCase):
    princ = principal.Principal()

    def testRelMalEstado(self):
        """RELATS: Rel. de mal estado soh pode ter copia com estado ruim"""
        rel = self.princ.RelMalEstado()
        for elem in rel:
            self.assertEqual(elem.estado.lower(), 'ruim')

    def testRelQuantCopias(self):
        """RELATS: Testar se os filmes listados apresentam quantidade valida de copias"""
        rel = self.princ.RelQuantCopias()
        for elem in rel:
            #assert elem.quantCopias > 0, 'Quantidade de copias deve ser > 0'
            self.assertTrue(elem.quantCopias>0)

    def testGetQuantCopiasTitulo(self):
        """RELATS: Quantidade de copias deve ser > 0 ou concine nao existe no catalgo"""
        for elem in self.princ.listaCopia:
            self.assertTrue(self.princ.getQuantCopiasTitulo(elem.concine)>0)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(test_copia_relatorios))
        return suite

if __name__ == '__main__':
    unittest.main()