from database.connection import conectar
from models.produto import Produto

#=============================
# ---       PRODUTOS       ---
#=============================

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(""" 
        SELECT
            id,
            marca,
            modelo,
            referencia,
            categoria,
            descricao,
            preco,
            custo,
            estoque,
            estoque_minimo,
            disponivel
        FROM produtos
        ORDER BY id;
    """)

    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return [
        Produto(*produto) for produto in produtos
    ]

#=============================
# --- BUSCA PRODUTO POR ID ---
#=============================

def buscar_produto_por_id(produto_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(""" 
    SELECT 
        id,
        marca,
        modelo,
        referencia,
        categoria,
        descricao,
        preco,
        custo,
        estoque,
        estoque_minimo,
        disponivel
        FROM produtos
        WHERE id = %s;
    """,(produto_id,))

    produto = cursor.fetchone()

    cursor.close()
    conexao.close()

    if produto is None:
        return None

    return Produto(*produto)

