from database.conexao import conectar

def tabela_catalogo():
    conexao = conectar()
    cursor = conexao.cursor()

    criar_tabela_catalogo = """
        CREATE TABLE IF NOT EXISTS catalogo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tipo_produto VARCHAR(17) NOT NULL,
            nome_flor VARCHAR(150) NOT NULL,
            preco DECIMAL(10,2) NOT NULL,
            estoque VARCHAR(254) NOT NULL
        )
    """
    cursor.execute(criar_tabela_catalogo)
    conexao.commit()
    
    cursor.close()
    conexao.close()
