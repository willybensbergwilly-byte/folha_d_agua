from models.catalogo.catalogo import Catalogo
from models.cliente import Cliente
from models.encomenda import Encomenda

cliente = Cliente(1, "senha123", "João Silva", "joao.silva@gmail.com", 4123456789)
cliente = Cliente(2, "senha456", "Maria Oliveira", "maria.oliveira@gmail.com", 4199887826)
print(cliente)

catalogo = Catalogo("Rosas", "Rosas Vermelhas", 10.00, 5, 100)
catalogo = Catalogo("Tulipas", "Tulipas Amarelas", 15.00, 3, 50)
catalogo = Catalogo("Girassóis","Girassóis Amarelos", 12.00, 7, 30)
print(catalogo)

encomenda = Encomenda("2026-06-01", "2023-06-05", "João Silva", "Rosas Vermelhas", 2, "Pendente")
print(encomenda)
