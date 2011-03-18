import unittest
import Copia_Test
import Socio_Test
import Teste_Emprestimo
import teste_copia_relatorios

#criando as suites
suite_copia = Copia_Test.Copia_Test.suite()
suite_socio = Socio_Test.Socio_Test.suite()
suite_emprestimo = Teste_Emprestimo.Test_Emprestimo.suite()
suite_relatorios = teste_copia_relatorios.test_copia_relatorios.suite()

#criando a suite principal
suite_principal = unittest.TestSuite()

#Adiciona os testes da suite principal
suite_principal.addTest(suite_copia)
suite_principal.addTest(suite_socio)
suite_principal.addTest(suite_emprestimo)
suite_principal.addTest(suite_relatorios)

#configura e executa o teste (run)
unittest.TextTestRunner(verbosity=2).run(suite_principal)

