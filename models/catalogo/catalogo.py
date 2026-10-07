class Catalogo:
    def __init__(self, id, tipo_produto, nome_flor, preco, estoque):
        self.id = id
        self.tipo_produto = tipo_produto
        self.nome_flor = nome_flor
        self.preco = preco
        self.estoque = estoque
    
def __str__(self):
        return f"id: {self.id} | Tipo de Produto: {self.tipo_produto}, | Nome da Flor: {self.nome_flor}, | Preço: {self.preco}, |  | Estoque: {self.estoque}"

def __str__(self):
    return (
        f"Tipo de Produto: {self.tipo_produto} | "
        f"Nome: {self.nome_flor} | "
        f"Preço: R$ {self.preco:.2f}"
    )


catalogo2 = Catalogo("Flor Individual", "de Rosas Vermelhas", 45.00,  20,)
catalogo3 = Catalogo("Flor individual", "de Tulipas Coloridas", 55.00,  15)
catalogo4 = Catalogo("Arranjo","de Lírios Brancos", 65.00,  15)
catalogo5 = Catalogo("Buquê", "de Margaridas", 30.00,  25)
catalogo6 = Catalogo("Arranjo", "jo de Orquídeas", 85.00,  10)
catalogo7 = Catalogo("Vaso", "de Violetas", 28.00,  15)
catalogo8 = Catalogo("Buquê", "de Crisântemos", 38.00,  20)
catalogo9 = Catalogo("Buquê", "de Hortênsias Azuis", 60.00,  12)
catalogo10 = Catalogo("Flor Individual", "Buquê de Cravos Coloridos", 35.00,  25)