
import streamlit as st


def formatar_preco(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


st.title("🛒 Meu carrinho")

if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

carrinho = st.session_state.carrinho

if not carrinho:
    st.info("Seu carrinho está vazio.")

else:
    quantidades = {}

    for produto in carrinho:
        if produto.id not in quantidades:
            quantidades[produto.id] = {"produto": produto, "quantidade": 0}

        quantidades[produto.id]["quantidade"] += 1

    total = 0

    for produto_id, item in list(quantidades.items()):
        produto = item["produto"]
        quantidade = item["quantidade"]

        st.divider()

        coluna_produto, coluna_quantidade, coluna_remover = st.columns([3, 2, 1])

        with coluna_produto:
            st.write(f"**{produto.marca} {produto.modelo}**")
            st.write(f"Preço unitário: {formatar_preco(produto.preco)}")

        with coluna_quantidade:
            st.write("Quantidade")

            coluna_menos, coluna_numero, coluna_mais = st.columns([1, 1, 1])

            with coluna_menos:
                if st.button("−", key=f"menos_{produto_id}"):
                    for indice, item_carrinho in enumerate(carrinho):
                        if item_carrinho.id == produto_id:
                            carrinho.pop(indice)
                            break
                    st.rerun()

            with coluna_numero:
                st.markdown(
                    f"<h3 style='text-align: center; margin: 0;'>{quantidade}</h3>",
                    unsafe_allow_html=True
                )

            with coluna_mais:
                if st.button("+", key=f"mais_{produto_id}"):
                    if quantidade < produto.estoque:
                        carrinho.append(produto)
                    else:
                        st.warning("Quantidade maior que o estoque disponível.")
                    st.rerun()

        with coluna_remover:
            if st.button("🗑️", key=f"remover_{produto_id}"):
                st.session_state.carrinho = [
                    item_carrinho
                    for item_carrinho in carrinho
                    if item_carrinho.id != produto_id
                ]
                st.rerun()

        subtotal = produto.preco * quantidade
        total += subtotal

        st.write(f"Subtotal: **{formatar_preco(subtotal)}**")

    st.divider()
    st.subheader(f"Total da compra: {formatar_preco(total)}")
