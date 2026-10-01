class Catalogo:
    def __init__(self, tipo_produto, nome_flor, preco, quantidade, estoque):
        self.tipo_produto = tipo_produto
        self.quantidade = quantidade
        self.nome_flor = nome_flor
        self.preco = preco
        self.estoque = estoque
    
    def __str__(self):
        return f"Tipo de Produto: {self.tipo_produto}, | Nome da Flor: {self.nome_flor}, | Preço: {self.preco}, | Quantidade: {self.quantidade}, | Estoque: {self.estoque}"