from models.buque import Buque
from models.arranjo import Arranjo
from models.estoque import Estoque
from models.catalogo.catalogo import Catalogo
from models.cliente import Cliente

from repositories.encomenda_repo import tabela_encomenda
from repositories.cliente_repo import tabela_cliente
from repositories.catalogo_repo import tabela_catalogo
from repositories.admin_repo import tabela_admin
from repositories.catalogo_repo import cadastrar_produto, listar_produtos

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/admin/produtos/cadastrar")
def cadastrar_produto_admin():
    return render_template("admin/cadastrar_produto.html")
    return "Produto cadastrado com sucesso!"

@app.route("/admin/estoque")
def estoque_admin():
    produtos = listar_produtos()
    return render_template("admin/estoque.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)


catalogo = Catalogo("Buquê", "Rosas Vermelhas", 100.00)

print(catalogo)

catalogo1 = Catalogo("Buquê", "Crisântemos", 99.99)

print(catalogo1)

cliente = Cliente(
    "Nexus@7315",
    "Maria Oliveira",
    "Maria1029910",
    "maria.oliveira@gmail.com",
    4199887821
)

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