from models.buque import Buque
from models.arranjo import Arranjo
from models.estoque import Estoque
from models.catalogo.catalogo import Catalogo
from models.cliente import Cliente

from repositories.encomenda_repo import tabela_encomenda
from repositories.cliente_repo import tabela_cliente
from repositories.catalogo_repo import tabela_catalogo
from repositories.admin_repo import tabela_admin
from repositories.catalogo_repo import cadastrar_produto, listar_produtos, atualizar_estoque

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/admin/")
def admin():
    return render_template("admin/admin.html")
      
@app.route("/admin/produtos/cadastrar", methods=["GET", "POST"])
def cadastrar_produto_admin(): 
    if  request.method == "POST":
        tipo_produto = request.form["tipo_produto"]
        nome_flor = request.form["nome_flor"]
        preco = request.form["preco"]
        estoque = request.form["estoque"]

        cadastrar_produto(
            tipo_produto,
            nome_flor,
            preco,
            estoque
        )

        return "Produto cadastrado com sucesso!"

    return render_template("admin/cadastrar_produto.html")

@app.route("/admin/estoque")
def estoque_admin():
    produtos = listar_produtos()
    return render_template("admin/estoque.html", produtos=produtos)

@app.route("/admin/estoque/atualizar/<int:id>", methods=["POST"])
def atualizar_estoque_admin(id):
    estoque = request.form.get("estoque", type=int)

    if estoque is None or estoque < 0:
        return "Informe uma quantidade válida.", 400

    atualizar_estoque(id, estoque)

    return redirect(url_for("estoque_admin"))

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