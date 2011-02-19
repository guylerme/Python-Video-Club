import time, datetime

class Emprestimo():

    def __init__(self):
        self.valorFixo = 4
        self.inscricao = None
        self.codigoFita = None
        self.dataInicio = None
        self.dataFim = None
        self.multa = 1


    def pegarFita(self, v_inscricao, v_dataInicio, v_codigoFita):
        self.inscricao = v_inscricao
        self.dataInicio = v_dataInicio
        self.codigo_fita = v_codigoFita



##    def devolverFitaComData(self, v_dataFim, v_valor):
##        self.dataFim = v_dataFim
##        self.valorPago = v_valor

    def devolverFita(self):
        data =datetime.datetime.today()
        self.dataFim = str(data.day) + '/' + str(data.month) +'/' + str(data.year)

        time_format = "%d/%m/%Y"
        dataInicioFormatada = datetime.datetime.fromtimestamp(time.mktime(time.strptime(self.dataInicio, time_format)))

        x = datetime.datetime.today().date() - dataInicioFormatada.date()
        if (x.days) > 3:
            self.valorPago = self.valorFixo + self.multa*(x.days - 3)
        else:
            self.valorPago = self.valorFixo

        return str(self.valorPago)