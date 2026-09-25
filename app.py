import streamlit as st
from services.produto_service import listar_produtos

# ====================
# LOJA KAIROS WATCH CO.
# ====================

st.set_page_config(
    page_title="Kairos Watch Co.",
    page_icon=" ⌚︎ ",
    layout="wide",

)

st.title(" ⌚︎ Kairos Watch Co.")
st.markdown("### Encontre o relógio ideal para você.")
st.write("")
st.write("")

produtos_originais = listar_produtos()
produtos = produtos_originais.copy()

st.write(f"#### São {len(produtos)} modelos de relógios disponíveis para você.")

# ====================
# LABEL PESQUISA
# ====================
pesquisa = st.text_input(
    "🔎 Pesquisa do produto:"
    "",
    placeholder = "Digite o marca ou modelo..."
.strip().lower())

if pesquisa:
   termo = pesquisa.strip().lower()

   produtos = [
       produto
       for produto in produtos
       if termo in produto.marca.lower()
       or termo in produto.modelo.lower()
   ]

marcas = sorted(set(produto.marca for produto in produtos_originais))

# ====================
# LABEL MARCA
# ====================
marca_selecionada = st.selectbox(
    "🏷️ Marca",
    ["Todas"] + marcas
)

if marca_selecionada != "Todas":
    produtos = [
        produto for produto in produtos
        if produto.marca == marca_selecionada
    ]

categorias = sorted(set(produto.categoria for produto in produtos_originais))

# ====================
# LABEL CATEGORIA
# ====================
categoria_selecionada = st.selectbox(
    "🏷️ Categoria",
    ["Todas"] + categorias
)

if categoria_selecionada != "Todas":
    produtos = [
        produto for produto in produtos
        if produto.categoria == categoria_selecionada
    ]


# ====================
# LABEL FAIXA DE PREÇO
# ====================
preco_minimo = min (produto.preco for produto in produtos)
preco_maximo = max (produto.preco for produto in produtos)

faixa_preco = st.selectbox(
    "💰 Faixa de preço",
    [
        "Todos",
        "Até R$ 500",
        "R$ 500 - R$ 1.000",
        "R$ 1.000 - R$ 2.000",
        "R$ 2.000 - R$ 5.000",
        "Acima de R$ 5.000"
    ]
)

if faixa_preco == "Até R$ 500":
    produtos = [
        produto for produto in produtos
        if produto.preco <= 500
    ]

elif faixa_preco == "R$ 500 - R$ 1.000":
    produtos = [
        produto for produto in produtos
        if 500 < produto.preco <= 1000
    ]

elif faixa_preco == "R$ 1.000 - R$ 2.000":
    produtos = [
        produto for produto in produtos
        if 1000 < produto.preco <= 2000
    ]

elif faixa_preco == "R$ 2.000 - R$ 5.000":
    produtos = [
        produto for produto in produtos
        if 2000 < produto.preco <= 5000
    ]

elif faixa_preco == "Acima de R$ 5.000":
    produtos = [
        produto for produto in produtos
        if produto.preco > 5000
    ]

def formatar_preco(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ====================
# RELÓGIOS MOSTRUÁRIO
# ====================
colunas = st.columns(4)
for indice, produto in enumerate(produtos):

    with colunas[indice % 4]:

        st.markdown(
            f'''
            ### {produto.marca}
            **{produto.modelo}**\n 
            **{formatar_preco(produto.preco)}**\n 
            📦 Estoque: **{produto.estoque}**
            '''
        )

        if produto.estoque > 0:
            st.button(
            "🛒 Comprar",
            key=f"comprar_{produto.id}",
            use_container_width=True,
        )
        else:
            st.write("❌ Produto esgotado")

        st.divider()