import unittest
import testCopia
import testSocio
import testEmprestimo
import testCopiaRelatorios

#criando as suites
suite_copia = testCopia.Copia_Test.suite()
suite_socio = testSocio.Socio_Test.suite()
suite_emprestimo = testEmprestimo.Test_Emprestimo.suite()
suite_relatorios = testCopiaRelatorios.test_copia_relatorios.suite()

#criando a suite principal
suite_principal = unittest.TestSuite()

#Adiciona os testes da suite principal
suite_principal.addTest(suite_copia)
suite_principal.addTest(suite_socio)
suite_principal.addTest(suite_emprestimo)
suite_principal.addTest(suite_relatorios)

#configura e executa o teste (run)
unittest.TextTestRunner(verbosity=2).run(suite_principal)

