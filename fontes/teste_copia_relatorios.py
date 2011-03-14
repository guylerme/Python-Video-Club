import unittest
import principal

class test_copia_relatorios(unittest.TestCase):
    princ = principal.Principal()

    def testRelMalEstado(self):
        """Rel. de mal estado soh pode ter copia com estado ruim"""
        rel = self.princ.RelMalEstado()
        for elem in rel:
            self.assertEqual(elem.estado.lower(), 'ruim')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(test_copia_relatorios))
        return suite

if __name__ == '__main__':
    unittest.main()