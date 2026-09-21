from services.produto_service import listar_produtos


produtos = listar_produtos()

print("Quantidade de produtos:", len(produtos))

print("\nPrimeiros 5 produtos:")

for produto in produtos[:5]:
    print(produto)