import unittest
from emprestimo import Emprestimo

class Teste_Emprestimo(unittest.TestCase):
    def test_exists(self):
        oEmprestimo = Emprestimo()
        assert oEmprestimo != None, 'Classe nao encontrada'

if __name__ == '__main__':
    unittest.main()
