from models.catalogo import Catalogo
from models.cliente import Cliente

cliente = Cliente(1, "senha123", "João Silva", "joao.silva@email.com")

catalogo = Catalogo("Rosas", "Rosas Vermelhas", 10.00, 5, 100)
catalogo = Catalogo("Tulipas", "Tulipas Amarelas", 15.00, 3, 50)
print(catalogo)
