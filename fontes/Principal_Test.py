import unittest
#from principal import Principal

class Principal_Test(unittest.TestCase):
    def testInicializaCopias(self):
        """Verifica se a lista de copias esta vazia"""
        principal = Principal()
        assert principal.listaCopia != [], "lista vazia!"

    def testInicializaSocios(self):
        principal = Principal()
        assert principal.listaSocios != [], "lista vazia!"

##Requer versao 3.1 do unittest
##    @unittest.skip("Pulando este teste. Reservado para uso futuro.")
##    def test_nothing(self):
##        self.fail("shouldn't happen")

if __name__ == '__main__':
    unittest.main()