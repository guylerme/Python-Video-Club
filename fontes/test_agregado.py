import unittest
import Copia_test
import Socio_test
import Teste_Emprestimo

#criando as suites
suite_copia = Copia_test.suite()
suite_socio = Socio_test.suite()
suite_emprestimo = Teste_Emprestimo.suite()

#criando a suite principal
suite_principal = unittest.TestSuite()

#Adiciona os testes da suite principal
suite_principal.addTest(suite_copia)
suite_principal.addTest(suite_socio)
suite_principal.addTest(suite_emprestimo)

#configura e executa o teste (run)
unittest.TextTestRunner(verbosity=2).run(suite_principal)

