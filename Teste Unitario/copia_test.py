class Copia_Test():
    def validaCopia(self):
        c = Copia(1, 'As trancas do careca', '2:30', 2008, 'drama', 'Jim Carey', 'Brad Pitt', 'Angelina Jolie', '05/02/2010', 'bom', 5135)

    def alimentaLista(self):
        self.listaCopia = []

        c = Copia(1, 'As trancas do careca', '1:30', 2008, 'Comédia', 'Steven Spilberg', 'Brad Pitt', 'Angelina Jolie', '05/12/2009', 'bom', 5167)
        self.listaCopia.append(c)
        c = Copia(2, 'As trancas do careca', '1:30', 2008, 'Comédia', 'Steven Spilberg', 'Brad Pitt', 'Angelina Jolie', '25/12/2009', 'ruim', 5167)
        self.listaCopia.append(c)
        c = Copia(3, 'As trancas do careca', '1:30', 2008, 'Comédia', 'Steven Spilberg', 'Brad Pitt', 'Angelina Jolie', '10/02/2010', 'bom', 5167)
        self.listaCopia.append(c)

        c = Copia(4, 'O pistoleiro sem dedo', '2:00', 2010, 'Ação', 'Dalton Trumbo', 'Jackie Chan', 'Antonio Banderas', '05/08/2010', 'bom', 5182)
        self.listaCopia.append(c)
        c = Copia(5, 'O pistoleiro sem dedo', '2:00', 2010, 'Ação', 'Dalton Trumbo', 'Jackie Chan', 'Antonio Banderas', '15/12/2010', 'bom', 5182)
        self.listaCopia.append(c)

        c = Copia(6, 'Poeira em alto mar', '2:15', 2007, 'Aventura', 'Samuel Ornitz', 'Steven Segal', 'Julia Roberts', '15/02/2008', 'bom', 5566)
        self.listaCopia.append(c)

        c = Copia(7, 'Robocob', '1:37', 1992, 'Policial', 'Ring Lardner Jr.', 'Alex Murphi', 'Jet Li', '05/07/2005', 'bom', 5987)
        self.listaCopia.append(c)
        c = Copia(8, 'Robocob', '1:37', 1992, 'Policial', 'Ring Lardner Jr.', 'Alex Murphi', 'Jet Li', '05/07/1995', 'ruim', 5987)
        self.listaCopia.append(c)
        c = Copia(9, 'Robocob', '1:37', 1992, 'Policial', 'Ring Lardner Jr.', 'Alex Murphi', 'Jet Li', '17/07/1995', 'ruim', 5987)
        self.listaCopia.append(c)
        c = Copia(10, 'Robocob', '1:37', 1992, 'Policial', 'Ring Lardner Jr.', 'Alex Murphi', 'Jet Li', '13/10/1998', 'ruim', 5987)
        self.listaCopia.append(c)


        c = Copia(11, 'Star Wars', '1:45', 1987, 'Ficção', 'Joan Scott', 'Lucky Skywalker', 'Darth Vader', '22/04/1990', 'bom', 5642)
        self.listaCopia.append(c)

        c = Copia(12, 'Casablanca', '2:15', 1970, 'Drama', 'Sheridan Gibney', 'Didi', 'Xuxa', '06/09/1971', 'bom', 5248)
        self.listaCopia.append(c)
        c = Copia(13, 'Casablanca', '2:15', 1970, 'Drama', 'Sheridan Gibney', 'Didi', 'Xuxa', '06/12/1971', 'bom', 5248)
        self.listaCopia.append(c)

        c = Copia(14, 'E o vento levou', '2:30', 1986, 'Romance', 'Edith Atwater', 'Lima Duarte', 'Antonio Fagundes', '19/07/1988', 'bom', 5113)
        self.listaCopia.append(c)
        c = Copia(15, 'E o vento levou', '2:30', 1986, 'Romance', 'Edith Atwater', 'Lima Duarte', 'Antonio Fagundes', '19/07/1988', 'bom', 5113)
        self.listaCopia.append(c)

        c = Copia(16, 'Titanic', '1:30', 2006, 'Romance', 'True Boardman', 'Leonardo di Caprio', 'Kate Wisr...s', '10/01/2007', 'ruim', 5679)
        self.listaCopia.append(c)
        c = Copia(17, 'Titanic', '1:30', 2006, 'Romance', 'True Boardman', 'Leonardo di Caprio', 'Kate Wisr...s', '10/01/2007', 'bom', 5679)
        self.listaCopia.append(c)
        c = Copia(18, 'Titanic', '1:30', 2006, 'Romance', 'True Boardman', 'Leonardo di Caprio', 'Kate Wisr...s', '15/04/2008', 'bom', 5679)
        self.listaCopia.append(c)
        c = Copia(19, 'Titanic', '1:30', 2006, 'Romance', 'True Boardman', 'Leonardo di Caprio', 'Kate Wisr...s', '10/02/2009', 'bom', 5679)
        self.listaCopia.append(c)

        c = Copia(20, 'Mont Python', '1:36', 2002, 'Comédia', 'Horace Grenell', 'Zacarias', 'Mussum', '02/02/2002', 'bom', 5332)
        self.listaCopia.append(c)

        c = Copia(21, 'Rambo', '2:50', 1990, 'Ação', 'Ben Myers', 'Silvester Stallone', 'Bob Marley', '27/05/1990', 'bom', 5195)
        self.listaCopia.append(c)

        c = Copia(22, 'Rocky', '1:50', 1991, 'Ação', 'Steven Spilberg', 'Tom Cruise', 'Robert de Niro', '03/03/1993', 'bom', 5564)
        self.listaCopia.append(c)

        c = Copia(23, 'A hora do pesadelo', '1:00', 1995, 'Terror', 'James Cameron', 'Al Paccino', 'Al Capone', '24/08/1996', 'bom', 5744)
        self.listaCopia.append(c)
        c = Copia(24, 'A hora do pesadelo', '1:00', 1995, 'Terror', 'James Cameron', 'Al Paccino', 'Al Capone', '24/09/1999', 'bom', 5744)
        self.listaCopia.append(c)

##>>> cT = Copia_Test()
##>>> cT.validaCopia()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##  File "<module2>", line 3, in validaCopia
##TypeError: object.__new__() takes no parameters
##>>> cT = Copia_Test()
##>>> cT.validaCopia()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##  File "<module2>", line 3, in validaCopia
##TypeError: object.__new__() takes no parameters
##>>> c = Copia(1, 'As trancas do careca', '2:30', 2008, 'drama', 'Jim Carey', 'Brad Pitt', 'Angelina Jolie', '05/02/2010', 'bom')
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##TypeError: object.__new__() takes no parameters
##>>> cT = Copia_Test()
##>>> cT.validaCopia()
##>>>

##>>> cT = Copia_Test()
##>>> cT.alimentaLista()
##Traceback (most recent call last):
##  File "<interactive input>", line 1, in <module>
##  File "D:\Documents and Settings\cy85\Meus documentos\Pessoal\Pos\Software Livre\trabalho\Teste Unitario\copia_test.py", line 20, in alimentaLista
##    c = Copia(6, 'Poeira em alto mar', '2:15', 2007, 'Aventura', 'Samuel Ornitz', 'Steven Segal', 'Julia Roberts', '15/02/2008', 'bom')
##TypeError: __init__() takes exactly 12 positional arguments (11 given)
##>>> cT = Copia_Test()
##>>> cT.alimentaLista()
##>>> cT.listaCopia
##[<__main__.Copia object at 0x01B02ED0>,
## <__main__.Copia object at 0x01B02F10>,
## <__main__.Copia object at 0x01B02EF0>,
## <__main__.Copia object at 0x01B022F0>,
## <__main__.Copia object at 0x01B02550>,
## <__main__.Copia object at 0x01B02D70>,
## <__main__.Copia object at 0x01B02CD0>,
## <__main__.Copia object at 0x01B02890>,
## <__main__.Copia object at 0x01B02B30>,
## <__main__.Copia object at 0x01B02D30>,
## <__main__.Copia object at 0x01B02410>,
## <__main__.Copia object at 0x01B02470>,
## <__main__.Copia object at 0x01B02090>,
## <__main__.Copia object at 0x01B020F0>,
## <__main__.Copia object at 0x01B021F0>,
## <__main__.Copia object at 0x01B02230>,
## <__main__.Copia object at 0x01B021D0>,
## <__main__.Copia object at 0x01B02B10>,
## <__main__.Copia object at 0x01B02430>,
## <__main__.Copia object at 0x01B023D0>,
## <__main__.Copia object at 0x01B02490>,
## <__main__.Copia object at 0x01B02F70>,
## <__main__.Copia object at 0x033C9FF0>,
## <__main__.Copia object at 0x033C9FD0>]
##>>> cT.listaCopia[22]
##<__main__.Copia object at 0x033C9FF0>
##>>> cT.listaCopia[22].titulo
##'A hora do pesadelo'
##>>>