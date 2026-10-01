class Cliente:
    def __init__(self, senha_hash, nome, email, telefone):
        self._senha_hash = senha_hash
        self.nome = nome
        self._email = email
        self.telefone = telefone

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self._email}, Telefone: {self.telefone}"
    
    