import psycopg

def conectar():
    conexao = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="loja_relogios",
        user="postgres",
        password="Senha"
    )
    return conexao


