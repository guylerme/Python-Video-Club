import unittest
from copia import Copia

class Copia_Test(unittest.TestCase):
    def testCopia(self):
        copia = Copia(1, 'As trancas do careca', '2:30', 2008, 'drama', 'Jim Carey', 'Brad Pitt', 'Angelina Jolie', '05/02/2010', 'bom', 5135)
        assert copia != None, "nao existe a classe Copia"



if __name__ == '__main__':
    unittest.main()