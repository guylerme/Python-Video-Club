import unittest
import copia

class test_copia_relatorios(unittest.TestCase):
    def testRelMalEstado():
        """Rel. de mal estado soh pode ter copia com estado ruim"""
        rel = Copia().RelMalEstado()
        for elem in rel:
            self.assertTrue(elem.estado.lower(), 'bom')


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(test_copia_relatorios))
        return suite

if __name__ == '__main__':
    unittest.main()