import unittest
from emprestimo import Emprestimo

class Teste_Emprestimo(unittest.TestCase):
    def test_exists(self):
        oEmprestimo = Emprestimo()
        assert oEmprestimo.valorFixo != 4, 'Valor fixo incorreto'

if __name__ == '__main__':
    unittest.main()
