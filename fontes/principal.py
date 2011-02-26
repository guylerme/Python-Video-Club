import _tkinter
import tkinter

##import Emprestimo
##import Copia
##import Socio

class Principal():
    def __init__(self):
        self.listaCopia = []
        self.listaSocios = []
        self.listaEmprestimos = []

        self.inicializaCopias()
        self.inicializaSocios()

        self.inicializaMenu()


    def inicializaCopias(self):
        c = Copia(1, 'As trancas do careca', '1:30', 2008, 'Comedia', 'Steven Spilberg', 'Brad Pitt', 'Angelina Jolie', '05/12/2009', 'bom', 5167)
        self.listaCopia.append(c)
        c = Copia(2, 'As trancas do careca', '1:30', 2008, 'Comedia', 'Steven Spilberg', 'Brad Pitt', 'Angelina Jolie', '25/12/2009', 'ruim', 5167)
        self.listaCopia.append(c)
        c = Copia(3, 'As trancas do careca', '1:30', 2008, 'ComÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©dia', 'Steven Spilberg', 'Brad Pitt', 'Angelina Jolie', '10/02/2010', 'bom', 5167)
        self.listaCopia.append(c)

        c = Copia(4, 'O pistoleiro sem dedo', '2:00', 2010, 'Acao', 'Dalton Trumbo', 'Jackie Chan', 'Antonio Banderas', '05/08/2010', 'bom', 5182)
        self.listaCopia.append(c)
        c = Copia(5, 'O pistoleiro sem dedo', '2:00', 2010, 'Acao', 'Dalton Trumbo', 'Jackie Chan', 'Antonio Banderas', '15/12/2010', 'bom', 5182)
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


        c = Copia(11, 'Star Wars', '1:45', 1987, 'Ficcao', 'Joan Scott', 'Lucky Skywalker', 'Darth Vader', '22/04/1990', 'bom', 5642)
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

        c = Copia(20, 'Mont Python', '1:36', 2002, 'Comedia', 'Horace Grenell', 'Zacarias', 'Mussum', '02/02/2002', 'bom', 5332)
        self.listaCopia.append(c)

        c = Copia(21, 'Rambo', '2:50', 1990, 'Acao', 'Ben Myers', 'Silvester Stallone', 'Bob Marley', '27/05/1990', 'bom', 5195)
        self.listaCopia.append(c)

        c = Copia(22, 'Rocky', '1:50', 1991, 'Acao', 'Steven Spilberg', 'Tom Cruise', 'Robert de Niro', '03/03/1993', 'bom', 5564)
        self.listaCopia.append(c)

        c = Copia(23, 'A hora do pesadelo', '1:00', 1995, 'Terror', 'James Cameron', 'Al Paccino', 'Al Capone', '24/08/1996', 'bom', 5744)
        self.listaCopia.append(c)
        c = Copia(24, 'A hora do pesadelo', '1:00', 1995, 'Terror', 'James Cameron', 'Al Paccino', 'Al Capone', '24/09/1999', 'bom', 5744)
        self.listaCopia.append(c)


    def inicializaSocios(self):
        self.s = Socio('Joao', 1, '27221122')
        self.listaSocios.append(self.s)

        self.s = Socio('Jose', 2, '27221133')
        self.listaSocios.append(self.s)

        self.s = Socio('Maria', 3, '27221144')
        self.listaSocios.append(self.s)

        self.s = Socio('Joana', 4, '27221155')
        self.listaSocios.append(self.s)

    def inicializaMenu(self):
        root = tkinter.Tk()
        frame = tkinter.Frame()
        frame.pack()

        self.button = tkinter.Button(frame, text="QUIT", fg="red",
                         command=frame.quit)
        self.button.pack(side=tkinter.LEFT)

        self.hi_there = tkinter.Button(frame, text="Hello",
                           command=self.say_hi)
        self.hi_there.pack(side=tkinter.LEFT)
        self.label = tkinter.Label(frame, text="Test")
        self.label.pack(side=tkinter.LEFT)

        root.mainloop()

    def say_hi(self):
        print("hi there, everyone!")