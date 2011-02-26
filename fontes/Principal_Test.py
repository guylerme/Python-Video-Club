import unittest
#from principal import Principal

class Principal_Test(unittest.TestCase):
    def testInicializaCopias(self):
        principal = Principal()
        assert principal.listaCopia != [], "nao tem telefone!"

if __name__ == '__main__':
    unittest.main()