from database.conexao import conectar

def tabela_catalogo():
    conexao = conectar()
    cursor = conexao.cursor()

    criar_tabela_catalogo = """
        CREATE TABLE IF NOT EXISTS catalogo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tipo_produto FOREIGN KEY VARCHAR(17) NOT NULL,
            nome_flor VARCHAR(150) NOT NULL,
            preco VARCHAR(17) DECIMAL(10,2) NOT NULL,
            estoque NOT NULL VARCHAR(255)
        )
    """
    cursor.execute(criar_tabela_catalogo)
    conexao.commit()
    
    cursor.close()
    conexao.close()
