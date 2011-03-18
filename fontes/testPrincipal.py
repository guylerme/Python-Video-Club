import unittest
from principal import Principal

class Principal_Test(unittest.TestCase):
    def testInicializaCopias(self):
        """Garantir que a lista das copias estah carregada"""
        principal = Principal()
        assert principal.listaCopia != [], "lista vazia!"

    def testInicializaSocios(self):
        """Garantir que a lista dos socios estah carregada"""
        principal = Principal()
        assert principal.listaSocios != [], "lista vazia!"

##Requer versao 3.1 do unittest
##    @unittest.skip("Pulando este teste. Reservado para uso futuro.")
##    def test_nothing(self):
##        self.fail("shouldn't happen")

if __name__ == '__main__':
    unittest.main()