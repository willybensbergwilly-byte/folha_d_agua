from models.catalogo.catalogo import Catalogo
from models.cliente import Cliente
from repositories.encomenda_repo import tabela_encomenda
from repositories.cliente_repo import tabela_cliente
from repositories.catalogo_repo import tabela_catalogo

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

catalogo = Catalogo("Rosas", "Rosas Vermelhas", 10.00, 5, 100)
print(catalogo)

cliente = Cliente(2, "Nexus@7315", "Maria Oliveira", "maria.oliveira@gmail.com", 4199887821)
print(cliente)

tabela_encomenda()
tabela_cliente()
tabela_catalogo()