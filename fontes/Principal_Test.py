import unittest
#from principal import Principal

class Principal_Test(unittest.TestCase):
    def testInicializaCopias(self):
        principal = Principal()
        assert principal.listaCopia != [], "lista vazia!"

    def testInicializaSocios(self):
        principal = Principal()
        assert principal.listaSocios != [], "lista vazia!"

if __name__ == '__main__':
    unittest.main()