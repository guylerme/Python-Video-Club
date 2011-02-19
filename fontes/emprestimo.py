from ficha_emprestimo import Ficha_Emprestimo

class Emprestimo():

    def __init__(self):
        self.listaEmprestimo = []
        self.valorFixo = 4


    def pegarFita(self, v_inscricao, v_dataInicio, v_codigoFita):
        self.inscricao = v_inscricao
        self.dataInicio = v_dataInicio
        self.codigo_fita = v_codigoFita

        self.fichaEmprestimo = FichaEmprestimo()
        self.fichaEmprestimo.inscricao = self.inscricao
        self.fichaEmprestimo.codigoFita = self.codigo_fita
        self.fichaEmprestimo.dataInicio = self.dataInicio

        self.listaEmprestimo.append(fichaEmprestimo)

##    def devolverFitaComData(self, v_dataFim, v_valor):
##        self.dataFim = v_dataFim
##        self.valorPago = v_valor

    def devolverFita(self, v_codigo_fita):
        data =datetime.datetime.today()
        self.dataFim = str(data.day) + '/' + str(data.month) +'/' + str(data.year)