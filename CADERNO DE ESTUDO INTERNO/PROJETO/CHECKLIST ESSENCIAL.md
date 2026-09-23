# CHECKLIST ESSENCIAL

## Projeto Loja Virtual de Relógios

**Objetivo:** acompanhar o desenvolvimento do projeto em grandes etapas, sem perder a visão geral.

### Legenda

```text
[ ] Não iniciado
[~] Em andamento
[x] Concluído
```

---

# ETAPA 1 — PREPARAÇÃO DO PROJETO

### Objetivo

Preparar o ambiente e criar a estrutura inicial.

-  Definir nome fictício da loja  ✅
    
-  Criar pasta do projeto ✅
    
-  Criar ambiente virtual Python 
    
-  Instalar Python ✅
    
-  Instalar PostgreSQL ✅
    
-  Configurar Git ✅
    
-  Criar estrutura de pastas ✅
    
-  Criar `requirements.txt` 
    
-  Criar `README.md`
    
-  Criar Documento Mestre ✅
    
-  Criar este Checklist ✅

   **Status:** [ ]

### Teste da etapa

-  Python funcionando
    
-  PostgreSQL funcionando ✅
    
-  Ambiente virtual funcionando ✅
    
-  Git funcionando ✅
    

**Status:** [ ]

---

# ETAPA 2 — BANCO DE DADOS

### Objetivo

Criar a estrutura do PostgreSQL.

Criar as tabelas principais:

-  Empresa ✅
    
-  Clientes ✅
    
-  Cartão de fidelidade ✅
    
-  Produtos ✅
    
-  Pedidos ✅
    
-  Itens do pedido ✅
    
-  Reservas ✅
    
-  Solicitações de produtos ✅
    
   **Status:** [ ✅ ]
### Banco

-  Criar banco `loja_relogios`  ✅
    
-  Definir chaves primárias
    
-  Definir chaves estrangeiras
    
-  Definir relacionamentos
    
-  Definir constraints
    
-  Criar `schema.sql`
    

### Teste da etapa

-  Todas as tabelas criadas
    
-  Relacionamentos funcionando
    
-  `SELECT` funcionando  ✅
    
-  `INSERT` funcionando  ✅
    
-  `UPDATE` funcionando  ✅
    
-  `DELETE` funcionando  ✅
    
-  `JOIN` funcionando  ✅
    

**Status:** [ ]

---

# ETAPA 3 — DADOS DA LOJA

### Objetivo

Popular o banco com dados fictícios para que possamos trabalhar com uma loja realista.

### Empresa

-  Criar empresa fictícia  ✅


### Clientes

-  Criar clientes fictícios  ✅
    
-  Criar CPFs fictícios  ✅
    
-  Criar telefones fictícios  ✅
    
-  Criar endereços fictícios  ✅
    
   **Status:** [ ✅ ]
   
### Produtos

-  Criar catálogo ✅
    
-  Cadastrar 100+ produtos ✅
    
-  Cadastrar marcas ✅
    
-  Cadastrar categorias ✅
    
-  Definir preços ✅
    
-  Definir custos ✅
    
-  Definir estoque ✅
    
-  Definir estoque mínimo ✅
    
   **Status:** [ ✅ ]
   
### Fidelidade

-  Criar cartões para clientes ✅


### Teste da etapa

-  Consultar clientes
    
-  Consultar produtos
    
-  Consultar estoque
    
-  Consultar cartões
    
-  Confirmar relacionamentos
    

**Status:** [ ]

---

# ETAPA 4 — PYTHON + POSTGRESQL

### Objetivo

Fazer o Python conversar corretamente com o banco.

-  Criar conexão Python → PostgreSQL  ✅
    
-  Criar arquivo de conexão  ✅
    
-  Testar conexão  ✅
    
-  Criar consultas SQL pelo Python  ✅
    
-  Buscar clientes  ✅
    
-  Buscar produtos  ✅
    
-  Inserir dados  ✅
    
-  Atualizar dados  ✅
    
-  Deletar/desativar dados  ✅
    
-  Tratar erros de conexão  ✅
    
   **Status:** [ ✅ ]
### Teste da etapa

```text
Python
   ↓
PostgreSQL
   ↓
Dados
```

-  Comunicação funcionando
    

**Status:** [ ✅ ]

---

# ETAPA 5 — CATÁLOGO + CLIENTES

### Objetivo

Criar a primeira parte funcional da aplicação.

## Clientes

-  Cadastro ✅
    
-  Consulta ✅
    
-  Pesquisa ✅
    
-  Edição ✅
    
-  Ativação/desativação ✅
    

## Produtos

-  Exibir catálogo ✅
    
-  Pesquisar produto ✅
    
-  Filtrar por marca ✅
    
-  Filtrar por categoria
    
-  Filtrar por preço
    
-  Mostrar disponibilidade
    
-  Mostrar estoque
    

### Teste da etapa

-  Cadastrar cliente ✅
    
-  Encontrar cliente
    
-  Editar cliente
    
-  Encontrar produto
    
-  Filtrar produtos
    
-  Visualizar estoque
    

**Status:** [ ]

---

# ETAPA 6 — CARRINHO + DESCONTO

### Objetivo

Criar o processo de seleção e cálculo da compra.

## Carrinho

-  Adicionar produto
    
-  Remover produto
    
-  Alterar quantidade
    
-  Validar estoque
    
-  Calcular subtotal
    

## Desconto

-  Criar regras de desconto
    
-  Calcular percentual
    
-  Calcular valor do desconto
    
-  Calcular total
    

Regra inicial:

```text
Até R$ 499,99       → 0%
R$ 500 a R$ 999,99  → 5%
R$ 1.000 a R$ 1.999 → 10%
Acima de R$ 2.000   → 15%
```

### Teste da etapa

-  Adicionar produto  ✅
    
-  Alterar quantidade  ✅
    
-  Remover produto  ✅
    
-  Calcular subtotal  ✅
    
-  Aplicar desconto  ✅
    
-  Calcular total corretamente  ✅
    

**Status:** [ ✅  ]

---

# ETAPA 7 — COMPRA + PEDIDOS + ESTOQUE

### Objetivo

Transformar o carrinho em uma venda real dentro do sistema.

## Compra

-  Compra com cadastro
    
-  Compra sem cadastro
    
-  Simular pagamento
    
-  Finalizar compra
    

## Pedido

-  Criar pedido
    
-  Criar itens do pedido
    
-  Registrar valores
    
-  Registrar forma de pagamento
    
-  Registrar status
    

## Estoque

-  Baixar estoque automaticamente
    
-  Impedir estoque negativo
    
-  Identificar produto esgotado
    
-  Bloquear compra sem estoque
    

### Teste da etapa

```text
Produto
   ↓
Carrinho
   ↓
Desconto
   ↓
Finalização
   ↓
Pedido
   ↓
Estoque atualizado
```

-  Fluxo funcionando
    

**Status:** [ ]

---

# ETAPA 8 — FIDELIDADE + RESERVAS

### Objetivo

Adicionar as regras especiais da loja.

## Fidelidade

-  Calcular pontos
    
-  Adicionar pontos após compra
    
-  Consultar saldo
    
-  Atualizar nível
    
-  Exibir cartão
    

Regra inicial:

```text
R$ 10 = 1 ponto
```

## Reservas

-  Detectar produto sem estoque
    
-  Permitir reserva
    
-  Registrar cliente
    
-  Registrar produto
    
-  Registrar quantidade
    
-  Criar fila
    
-  Atualizar status da reserva
    

### Teste

-  Compra gera pontos  ✅
    
-  Pontos aparecem no cartão ✅
    
-  Produto sem estoque permite reserva  ✅
    
-  Reserva fica registrada  ✅
    

**Status:** [ ✅ ]

---

# ETAPA 9 — SOLICITAÇÕES + ADMINISTRAÇÃO

### Objetivo

Criar as funções administrativas da loja.

## Solicitação de produto

-  Permitir solicitar produto inexistente
    
-  Registrar marca
    
-  Registrar modelo
    
-  Registrar descrição
    
-  Registrar cliente
    
-  Criar status
    

## Administração

-  Visualizar clientes
    
-  Visualizar produtos
    
-  Visualizar estoque
    
-  Visualizar pedidos
    
-  Visualizar reservas
    
-  Visualizar solicitações
    
-  Alterar status
    

### Teste

-  Solicitação registrada
    
-  Administrador consegue visualizar
    
-  Administrador consegue alterar status
    

**Status:** [ ]

---

# ETAPA 10 — PANDAS + STREAMLIT + DASHBOARD

### Objetivo

Transformar o sistema em uma aplicação visual e analítica completa.

## Streamlit

-  Criar interface principal
    
-  Criar menu
    
-  Criar página de produtos
    
-  Criar página do carrinho
    
-  Criar página de clientes
    
-  Criar página de pedidos
    
-  Criar página de fidelidade
    
-  Criar área administrativa
    

## Pandas

-  Conectar consultas ao Pandas
    
-  Criar DataFrames
    
-  Analisar vendas
    
-  Analisar produtos
    
-  Analisar clientes
    
-  Analisar estoque
    

## Dashboard

-  Faturamento
    
-  Número de pedidos
    
-  Número de clientes
    
-  Produtos vendidos
    
-  Ticket médio
    
-  Produtos mais vendidos
    
-  Marcas mais vendidas
    
-  Estoque crítico
    
-  Gráficos
    

### Teste

-  Streamlit abre
    
-  Todas as páginas funcionam
    
-  Dados aparecem corretamente
    
-  Dashboard apresenta informações do PostgreSQL
    
-  Pandas produz análises corretas
    

**Status:** [ ]

---

# TESTE FINAL DO PROJETO

Quando todas as etapas anteriores estiverem concluídas, executar o seguinte cenário:

```text
1. Abrir a loja
        ↓
2. Pesquisar produto
        ↓
3. Escolher produto
        ↓
4. Adicionar ao carrinho
        ↓
5. Adicionar segundo produto
        ↓
6. Alterar quantidade
        ↓
7. Calcular subtotal
        ↓
8. Aplicar desconto
        ↓
9. Identificar cliente
        ↓
10. Finalizar compra
        ↓
11. Criar pedido
        ↓
12. Registrar itens
        ↓
13. Atualizar estoque
        ↓
14. Calcular pontos
        ↓
15. Atualizar cartão
        ↓
16. Consultar pedido
        ↓
17. Consultar estoque
        ↓
18. Consultar pontos
        ↓
19. Abrir dashboard
        ↓
20. Conferir venda
```

### Resultado

-  Fluxo completo funcionando
    

---

# CONTROLE GERAL

|Etapa|Descrição|Status|
|---|---|---|
|1|Preparação|[ ]|
|2|Banco de dados|[ ]|
|3|Dados da loja|[ ]|
|4|Python + PostgreSQL|[ ]|
|5|Catálogo + Clientes|[ ]|
|6|Carrinho + Descontos|[ ]|
|7|Compra + Pedidos + Estoque|[ ]|
|8|Fidelidade + Reservas|[ ]|
|9|Solicitações + Administração|[ ]|
|10|Pandas + Streamlit + Dashboard|[ ]|

---

# REGISTRO ATUAL

**Etapa atual:**

```text
Etapa 1 — Preparação
```

**Tarefa atual:**

```text
Criar a estrutura inicial do projeto.
```

**Última etapa concluída:**

```text
Nenhuma.
```

**Próxima etapa:**

```text
Etapa 1 — Preparação.
```

---

# REGRA DE DESENVOLVIMENTO

O projeto deve ser desenvolvido **uma etapa por vez**.

Não devemos tentar implementar várias etapas simultaneamente.

Para cada etapa:

```text
PLANEJAR
   ↓
IMPLEMENTAR
   ↓
TESTAR
   ↓
CORRIGIR
   ↓
CONFIRMAR
   ↓
MARCAR [x]
   ↓
PRÓXIMA ETAPA
```

Quando houver um erro, o desenvolvimento permanece na etapa atual até que o problema seja compreendido e resolvido.

---

# META FINAL

Ao marcar as 10 etapas como concluídas, teremos uma aplicação integrada contendo:

```text
                 LOJA VIRTUAL
                      │
       ┌──────────────┼──────────────┐
       │              │              │
    CLIENTES       PRODUTOS       ESTOQUE
       │              │              │
       └──────────────┼──────────────┘
                      │
                   CARRINHO
                      │
                   DESCONTO
                      │
                    PEDIDO
                      │
             ┌────────┴────────┐
             │                 │
        FIDELIDADE          RESERVAS
             │
           PONTOS
             
             │
             ▼
         POSTGRESQL
             │
             ▼
            SQL
             │
             ▼
           PANDAS
             │
             ▼
         STREAMLIT
             │
             ▼
         DASHBOARD
```

**Fim do checklist.**