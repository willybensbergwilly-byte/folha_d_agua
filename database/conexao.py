import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="~~WrbdskmNN777",
    database="folha_dagua"
    ) 
    return conexao