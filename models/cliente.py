class Cliente:
    def __init__(self, id_cliente, senha_hash, nome, email, telefone):
        self.id_cliente = id_cliente
        self._senha_hash = senha_hash
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"
    