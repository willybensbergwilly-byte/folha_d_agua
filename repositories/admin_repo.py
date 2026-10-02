from database.conexao import conectar

def criar_tabela_admin():
    conexao = conectar()
    cursor = conexao.cursor() = """
    CREATE TABLE IF NOT EXISTS tabela_admin (
        id INT AUTO_INCREMENT,
        usuario VARCHAR(50) NOT NULL,
        senha_hash VARCHAR(18) NOT NULL
        
    )
    """
    
    cursor.execute(criar_tabela_admin)
    conexao.commit()