class Emprestimo():
    self.valorFixo = 4

    def __init__(self, v_inscricao, v_dataInicio, v_codigoFita):
        self.listaEmprestimo = []

        self.inscricao = v_inscricao
        self.dataInicio = v_dataInicio
        self.codigo_fita = v_codigoFita



##    def devolverFitaComData(self, v_dataFim, v_valor):
##        self.dataFim = v_dataFim
##        self.valorPago = v_valor

    def devolverFita(self, v_codigo_fita):
        data =datetime.datetime.today()
        self.dataFim = str(data.day) + '/' + str(data.month) +'/' + str(data.year)
        self.valorPago = v_valor