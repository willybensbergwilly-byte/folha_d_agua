from models.catalogo.catalogo import Catalogo

class Arranjo(Catalogo):
    def __init__(self, nome_flor, preco):
       self.nome_flor = nome_flor
       self.preco = preco