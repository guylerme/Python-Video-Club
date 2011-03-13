#Definir as classes de erro a serem disparados pela classe
##class CopiaError(Exception): pass
class errCopiaMissingValues(Exception): pass

class Copia():
    def __init__(self, v_codigo, v_titulo, v_duracao, v_ano,
        v_genero, v_nomeDiretor, v_artista1, v_artista2, v_dataAquisicao,
        v_estado, v_concine):
        self.codigo = v_codigo
        self.titulo = v_titulo
        self.duracao = v_duracao
        self.ano = v_ano
        self.genero = v_genero
        self.nomeDiretor = v_nomeDiretor
        self.artistaPrincipal1 = v_artista1
        self.artistaPrincipal2 = v_artista2
        self.dataAquisicao = v_dataAquisicao
        self.estado = v_estado
        self.concine = v_concine
        #self.newattr = v_newattr

    def setElenco(self, p_art1, p_art2, p_diretor):
        """Setar os nomes principais do elenco e do diretor"""
        pass

