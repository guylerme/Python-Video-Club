class Emprestimo_Test():
    def validaEmprestimo(self):
        e = Emprestimo(1, '01/02/2011')

    def validaDevolucao(self):
        e = Emprestimo(1, '01/02/2011')
        e.devolverFita('17/02/2011', 50)




##>>> eT = EmprestimoTest
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##NameError: name 'EmprestimoTest' is not defined
##>>> eT = EmprestimoTest()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##NameError: name 'EmprestimoTest' is not defined
##>>> eT = EmprestimoTest()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##NameError: name 'EmprestimoTest' is not defined
##>>> eT = Emprestimo_Test()
##>>> eT.validaEmprestimo()
##>>> eT.validaDevolucao()
##>>> today()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##NameError: name 'today' is not defined
##>>> import datetime
##>>> today()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##NameError: name 'today' is not defined
##>>> import datetime
##>>> datetime.today()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##AttributeError: 'module' object has no attribute 'today'
##>>> datetime.date
##<class 'datetime.date'>
##>>> datetime.date()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##TypeError: Required argument 'year' (pos 1) not found
##>>> datetime.today
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##AttributeError: 'module' object has no attribute 'today'
##>>> datetime.datetime.today
##<built-in method today of type object at 0x1E1D38A0>
##>>> datetime.datetime.today()
##datetime.datetime(2011, 2, 17, 16, 34, 7, 15000)
##>>> datetime.datetime.today()[1]
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##TypeError: 'datetime.datetime' object is unsubscriptable
##>>> datetime.datetime.today()
##datetime.datetime(2011, 2, 17, 16, 35, 31, 656000)
##>>> x = datetime.datetime.today()
##>>> x[1]]
##  File "<string>", line None
##SyntaxError: invalid syntax (<interactive input>, line 1)
##>>> x[1]
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##TypeError: 'datetime.datetime' object is unsubscriptable
##>>> x
##datetime.datetime(2011, 2, 17, 16, 35, 53, 828000)
##>>> x(1)
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##TypeError: 'datetime.datetime' object is not callable
##>>> x
##datetime.datetime(2011, 2, 17, 16, 35, 53, 828000)
##>>> x.day
##17
##>>> x.day + '/'  + x.month
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##TypeError: unsupported operand type(s) for +: 'int' and 'str'
##>>> x.day  '/'   x.month
##  File "<string>", line None
##SyntaxError: invalid syntax (<interactive input>, line 1)
##>>> x.day . '/'
##  File "<string>", line None
##SyntaxError: invalid syntax (<interactive input>, line 1)
##>>> x.day || '/'
##  File "<string>", line None
##SyntaxError: invalid syntax (<interactive input>, line 1)
##>>> x.day + '/'
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##TypeError: unsupported operand type(s) for +: 'int' and 'str'
##>>> to_str(x.day) + '/'
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##NameError: name 'to_str' is not defined
##>>> str(x.day) + '/'
##'17/'
##>>> str(x.day) + '/'
##>>> str(x.day) + '/'
##'17/'
##>>> e = Emprestimo(1, '02/01/2010')
##>>> e.devolverFita(10)
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##TypeError: devolverFita() takes exactly 3 positional arguments (2 given)
##>>> e = Emprestimo(1, '02/01/2010')
##>>> e.devolverFita(10)