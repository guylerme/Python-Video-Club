#Definir as classes de erro a serem disparados pela classe
class errCopiaMissingValues(Exception): pass

class Copia():
    erro = errCopiaMissingValues

    def __init__(self, v_codigo = 0, v_titulo='', v_duracao=0, v_ano=0,
        v_genero='', v_nomeDiretor='', v_artista1='', v_artista2='', v_dataAquisicao=None,
        v_estado='', v_concine=0):
        self.codigo = 0
        self.titulo = ''
        self.duracao = 0
        self.ano = 0
        self.genero = ''
        self.nomeDiretor = ''
        self.artistaPrincipal1 = ''
        self.artistaPrincipal2 = ''
        self.dataAquisicao = None
        self.estado = ''
        self.concine = 0

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

    def setElenco(self, p_art1, p_art2, p_diretor):
        """Setar os nomes principais do elenco e do diretor"""
##        pass
        if (not p_art1) and (not p_art2) and (not p_diretor):
            raise errCopiaMissingValues #, 'Nenhum dos atributos do elenco foi informado'

        if not p_art1:
            raise self.erro #, 'Nome do artista 1 nao informado'

        if not p_art2:
            raise errCopiaMissingValues #, 'Nome do artista 2 nao informado'

        if not p_diretor:
            raise errCopiaMissingValues #,'Nome do diretor nao informado'





