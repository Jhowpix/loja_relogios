class Produto:

    def __init__(
        self,
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
    ):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.referencia = referencia
        self.categoria = categoria
        self.descricao = descricao
        self.preco = preco
        self.custo = custo
        self.estoque = estoque
        self.estoque_minimo = estoque_minimo
        self.disponivel = disponivel