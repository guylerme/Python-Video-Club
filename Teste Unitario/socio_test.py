class Socio_Test():
    def validaNome(self):
        s = Socio('Teste')


    def validaDados(self):
        s = Socio('Teste', 1, '27222222')

    def alimentaLista(self):
        self.listaSocios = []
        self.s = Socio('Joao', 1, '27221122')
        self.listaSocios.append(self.s)

        self.s = Socio('Jose', 2, '27221133')
        self.listaSocios.append(self.s)

        self.s = Socio('Maria', 3, '27221144')
        self.listaSocios.append(self.s)

        self.s = Socio('Joana', 4, '27221155')
        self.listaSocios.append(self.s)










##>>> sT = Socio_Test()
##>>> sT.validaNome()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##  File "<module1>", line 3, in validaNome
##NameError: global name 'Socio' is not defined
##>>> sT = Socio_Test()
##>>> sT.validaNome()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##  File "<module1>", line 3, in validaNome
##NameError: global name 'Socio' is not defined
##>>> import Socio
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##ImportError: No module named Socio
##>>> sT = Socio_Test()
##>>> sT.validaNome()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##  File "<module1>", line 3, in validaNome
##TypeError: __init__() takes exactly 2 positional arguments (1 given)
##>>> import Socio
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##ImportError: No module named Socio
##>>> sT = Socio_Test()
##>>> sT.validaNome()
##>>>
##>>> st = Socio_Test()
##>>> st.validaDados()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##  File "<module1>", line 7, in validaDados
##TypeError: __init__() takes exactly 2 positional arguments (4 given)
##>>>
##  File "<module2>", line 3
##    def inscricao
##                ^
##SyntaxError: invalid syntax
##>>> st = Socio_Test()
##>>> st.validaDados()
##>>> sT = Socio_Test()
##>>> sT.alimentaLista
##<bound method Socio_Test.alimentaLista of <__main__.Socio_Test object at 0x01AE1CB0>>
##>>> sT.alimentaLista()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##  File "D:\Documents and Settings\cy85\Meus documentos\Pessoal\Pos\Software Livre\trabalho\Teste Unitario\socio_test.py", line 11, in alimentaLista
##    self.s = Socio('Joao', 1, '27221122')
##NameError: global name 'Socio' is not defined
##>>> import Socio
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##ImportError: No module named Socio
##>>> import fontes.Socio
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##ImportError: No module named fontes.Socio
##>>> sT = Socio_Test()
##>>> sT.alimentaLista()
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AE60B0>, <__main__.Socio object at 0x01AE6050>]
##>>> sT.listaSocios[]
##  File "<string>", line None
##SyntaxError: invalid syntax (<interactive input>, line 1)
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AE60B0>, <__main__.Socio object at 0x01AE6050>]
##>>> sT.listaSocios[1]
##<__main__.Socio object at 0x01AE6050>
##>>> sT.listaSocios.pop(0)
##<__main__.Socio object at 0x01AE60B0>
##>>> sT.listaSocios.pop(0).nome
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##IndexError: pop from empty list
##>>> sT.listaSocios
##[]
##>>> sT.alimentaLista()
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDF10>, <__main__.Socio object at 0x01AFDB30>]
##>>> sT.listaSocios[0].nome
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##AttributeError: 'Socio' object has no attribute 'nome'
##>>>
##>>> sT = Socio_Test()
##>>> sT.alimentaLista
##<bound method Socio_Test.alimentaLista of <__main__.Socio_Test object at 0x01AFD970>>
##>>> sT.alimentaLista()
##>>> sT.listaSocios
##[<__main__.Socio object at 0x01AFDC10>, <__main__.Socio object at 0x01AFDFF0>]
##>>> sT.listaSocios[0].nome
##'Joao'
##>>> sT.listaSocios[1].nome
##'Jose'