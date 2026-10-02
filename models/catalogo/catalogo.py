class Catalogo:
    def __init__(self, tipo_produto, nome_flor, preco, quantidade, estoque):
        self.tipo = tipo_produto
        self.quantidade = quantidade
        self.nome_flor = nome_flor
        self.preco = preco
        self.estoque = estoque
    
    def __str__(self):
        return f"Tipo de Produto: {self.tipo_produto}, | Nome da Flor: {self.nome_flor}, | Preço: {self.preco}, | Quantidade: {self.quantidade}, | Estoque: {self.estoque}"

catalogo1 = Catalogo("Rosas Vermelhas", "Buquê de Rosas Vermelhas", 45.00, 10, 20,)
catalogo2 = Catalogo("Rosas Brancas", "Buquê de Rosas Brancas", 48.00, 8, 20)
catalogo3 = Catalogo("Tulipas", "Buquê de Tulipas Coloridas", 55.00, 6, 15)
catalogo4 = Catalogo("Lírios", "Arranjo de Lírios Brancos", 65.00, 5, 15)
catalogo5 = Catalogo("Margaridas", "Buquê de Margaridas", 30.00, 12, 25)
catalogo6 = Catalogo("Orquídeas", "Arranjo de Orquídeas", 85.00, 4, 10)
catalogo7 = Catalogo("Violetas", "Vaso de Violetas", 28.00, 9, 15)
catalogo8 = Catalogo("Crisântemos", "Buquê de Crisântemos", 38.00, 10, 20)
catalogo9 = Catalogo("Hortênsias", "Buquê de Hortênsias Azuis", 60.00, 5, 12)
catalogo10 = Catalogo("Cravos", "Buquê de Cravos Coloridos", 35.00, 11, 25)