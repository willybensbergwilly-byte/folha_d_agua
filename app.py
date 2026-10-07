from models.buque import Buque
from models.arranjo import Arranjo
from models.estoque import Estoque

from models.catalogo.catalogo import Catalogo
from models.cliente import Cliente
from repositories.encomenda_repo import tabela_encomenda
from repositories.cliente_repo import tabela_cliente
from repositories.catalogo_repo import tabela_catalogo
from repositories.admin_repo import tabela_admin

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

catalogo = Catalogo(1,"Buque", "Rosas Vermelhas", 100.00, 100)
print(catalogo)

catalogo1 = Catalogo(2,"Buque", "Crisântemos", 99.99, 200)

cliente = Cliente(2, "Nexus@7315", "Maria Oliveira", "Maria1029910", "maria.oliveira@gmail.com", 4199887821)
print(cliente)

buque = Buque("Rosas Vermelhas", 45.00)
arranjo = Arranjo("Lírios Brancos", 65.00)

estoque_buque = Estoque(buque, 20)
estoque_arranjo = Estoque(arranjo, 15)

print(buque)
print(arranjo)

print(estoque_buque)
print(estoque_arranjo)

tabela_encomenda()
tabela_cliente()
tabela_catalogo()
tabela_admin()