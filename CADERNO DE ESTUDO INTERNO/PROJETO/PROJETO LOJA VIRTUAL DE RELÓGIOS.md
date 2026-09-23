# PROJETO: LOJA VIRTUAL DE RELÓGIOS

## 1. Objetivo

Criar uma loja virtual fictícia de relógios, utilizando produtos de marcas reais apenas como referência de catálogo.

A empresa, clientes, compras, CPFs, telefones, cartões de fidelidade e demais dados serão fictícios/sintéticos.

O sistema deverá simular uma operação comercial completa:

- Cadastro da empresa
    
- Cadastro de clientes
    
- Catálogo com 100+ relógios
    
- Controle de estoque
    
- Carrinho de compras
    
- Sistema de descontos
    
- Sistema de pontos/fidelidade
    
- Compra com ou sem cadastro
    
- Pedidos
    
- Reserva de produtos sem estoque
    
- Solicitação de produtos indisponíveis
    
- Histórico de compras
    
- Banco de dados PostgreSQL
    
- Consultas SQL
    
- Análises utilizando Pandas
    
- Interface utilizando Streamlit
    

# 2. Tecnologias

## Linguagem principal

Python

## Banco de dados

PostgreSQL

## Manipulação e análise de dados

Pandas

## Interface

Streamlit

## Consultas

SQL

## Comunicação Python → PostgreSQL

psycopg / SQLAlchemy

## Controle do projeto

Git + GitHub

# 3. Arquitetura geral

O projeto será dividido em camadas:

```text
                 USUÁRIO
                    │
                    ▼
              STREAMLIT
                    │
                    ▼
              REGRAS DE NEGÓCIO
                 PYTHON
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      POSTGRESQL            PANDAS
          │                   │
          ▼                   ▼
     DADOS DA LOJA       ANÁLISES / RELATÓRIOS
```

A ideia é evitar colocar toda a lógica dentro do `app.py`.

O Streamlit será responsável principalmente pela interface.

O Python ficará responsável pelas regras do sistema.

O PostgreSQL ficará responsável pelos dados.

O Pandas será utilizado principalmente para análise e relatórios.

# 4. Estrutura de pastas

Uma estrutura inicial simples:

```text
loja_relogios/
│
├── app.py
│
├── database/
│   ├── connection.py
│   ├── schema.sql
│   └── seed.sql
│
├── models/
│   ├── cliente.py
│   ├── produto.py
│   ├── pedido.py
│   └── fidelidade.py
│
├── services/
│   ├── cliente_service.py
│   ├── produto_service.py
│   ├── carrinho_service.py
│   ├── pedido_service.py
│   ├── estoque_service.py
│   ├── desconto_service.py
│   └── fidelidade_service.py
│
├── pages/
│   ├── inicio.py
│   ├── produtos.py
│   ├── carrinho.py
│   ├── clientes.py
│   ├── pedidos.py
│   ├── fidelidade.py
│   └── admin.py
│
├── data/
│   └── produtos.csv
│
├── analysis/
│   └── vendas.py
│
├── requirements.txt
│
└── README.md
```

# 5. Banco de dados

O PostgreSQL será o coração do projeto.

Principais tabelas:

```text
empresa
    │
    ├── clientes
    │       │
    │       └── cartao_fidelidade
    │
    ├── produtos
    │       │
    │       └── estoque
    │
    ├── pedidos
    │       │
    │       └── itens_pedido
    │
    ├── reservas
    │
    └── solicitacoes_produto
```

# 6. Tabela EMPRESA

Representará a empresa fictícia.

Exemplo:

```text
empresa
--------------------------------
id
razao_social
nome_fantasia
cnpj_ficticio
telefone
email
endereco
cidade
estado
cep
data_cadastro
```

Os dados serão completamente fictícios.

# 7. Tabela CLIENTES

Cadastro completo dos clientes.

```text
clientes
--------------------------------
id
nome
cpf_ficticio
data_nascimento
telefone
email
logradouro
numero
bairro
cidade
estado
cep
data_cadastro
status
```

Importante:

Os CPFs serão apenas dados sintéticos para simulação.

Não utilizar dados pessoais reais.

# 8. CARTÃO DE FIDELIDADE

Cada cliente poderá possuir um cartão da loja.

```text
cartao_fidelidade
--------------------------------
id
cliente_id
numero_cartao
pontos
nivel
data_criacao
status
```

Exemplo de níveis:

```text
Bronze
Prata
Ouro
```

Os níveis serão determinados por quantidade de pontos.

# 9. PRODUTOS

O catálogo terá inicialmente mais de 100 produtos.

Cada produto poderá conter:

```text
produtos
--------------------------------
id
marca
modelo
referencia
categoria
descricao
preco
custo
estoque
estoque_minimo
disponivel
data_cadastro
```

Exemplo de marcas reais que podem aparecer no catálogo:

```text
Casio
Seiko
Citizen
Orient
Timex
Fossil
Tissot
G-Shock
Technos
```

Os produtos podem ser fictícios ou baseados em modelos reais, deixando claro que a loja é uma simulação.

# 10. ESTOQUE

O estoque será controlado pelo sistema.

Exemplo:

```text
Produto: Relógio X
Estoque: 5
```

Quando o cliente comprar:

```text
5 → 4 → 3 → 2 → 1 → 0
```

Quando chegar a:

```text
0
```

O produto ficará indisponível para compra normal.

# 11. CATÁLOGO

O usuário poderá:

```text
Pesquisar produto
        ↓
Filtrar por marca
        ↓
Filtrar por categoria
        ↓
Ordenar por preço
        ↓
Visualizar produto
        ↓
Adicionar ao carrinho
```

Filtros podem incluir:

- Marca
    
- Categoria
    
- Faixa de preço
    
- Disponibilidade
    
- Modelo
    

# 12. CARRINHO

O sistema deverá permitir:

```text
Adicionar produto
Remover produto
Alterar quantidade
Visualizar subtotal
Aplicar desconto
Visualizar total
Finalizar compra
```

Exemplo:

```text
Relógio A     R$ 500,00
Relógio B     R$ 300,00
Relógio C     R$ 200,00

Subtotal      R$ 1.000,00
Desconto      R$   100,00
-------------------------
Total         R$   900,00
```

# 13. SISTEMA DE DESCONTOS

Criar regras de desconto por valor da compra.

Exemplo inicial:

```text
Até R$ 499,99
0%

R$ 500,00 até R$ 999,99
5%

R$ 1.000,00 até R$ 1.999,99
10%

Acima de R$ 2.000,00
15%
```

Posteriormente podemos adicionar outras regras.

# 14. SISTEMA DE FIDELIDADE

O cliente recebe pontos de acordo com o valor da compra.

Exemplo:

```text
A cada R$ 10,00
= 1 ponto
```

Compra:

```text
R$ 850,00
```

Pontos:

```text
85 pontos
```

O sistema deverá registrar esses pontos no cartão do cliente.

# 15. COMPRA COM CADASTRO

Fluxo:

```text
Cliente
   ↓
Informa CPF
   ↓
Sistema localiza cadastro
   ↓
Carrinho
   ↓
Desconto
   ↓
Compra
   ↓
Pagamento simulado
   ↓
Estoque atualizado
   ↓
Pontos adicionados
   ↓
Pedido registrado
```

# 16. COMPRA SEM CADASTRO

Também será possível comprar sem criar uma conta.

Fluxo:

```text
Cliente
   ↓
Comprar sem cadastro
   ↓
Carrinho
   ↓
Dados básicos para pedido
   ↓
Pagamento simulado
   ↓
Pedido
   ↓
Estoque atualizado
```

Nesse caso não haverá pontos de fidelidade, pois o cliente não possui cartão.

# 17. PEDIDOS

Tabela:

```text
pedidos
--------------------------------
id
cliente_id
data_pedido
subtotal
desconto
total
status
forma_pagamento
```

Status possíveis:

```text
Pendente
Pago
Preparando
Enviado
Entregue
Cancelado
```

E teremos:

```text
itens_pedido
--------------------------------
id
pedido_id
produto_id
quantidade
preco_unitario
subtotal
```

Isso permitirá descobrir exatamente quais produtos fizeram parte de cada pedido.

# 18. RESERVA DE PRODUTO

Quando um produto estiver sem estoque:

```text
Produto
Estoque = 0
       ↓
Cliente solicita reserva
       ↓
Sistema registra
       ↓
Cliente entra na fila
```

Tabela:

```text
reservas
--------------------------------
id
cliente_id
produto_id
quantidade
data_reserva
status
```

Status:

```text
Aguardando
Disponível
Convertida_em_pedido
Cancelada
```

# 19. PEDIDO DE PRODUTO INDISPONÍVEL

Além da reserva, o cliente poderá solicitar um produto que a loja não possui.

Exemplo:

```text
Cliente procura:

Relógio X

Produto não encontrado.

        ↓

"Solicitar produto"
```

Tabela:

```text
solicitacoes_produto
--------------------------------
id
cliente_id
nome_produto
marca
modelo
descricao
data_solicitacao
status
```

Isso cria uma funcionalidade interessante para análise futura.

# 20. ADMINISTRAÇÃO

Teremos uma área administrativa simulada.

O administrador poderá visualizar:

```text
Produtos
Estoque
Clientes
Pedidos
Reservas
Solicitações
Vendas
```

E futuramente:

```text
Faturamento
Produtos mais vendidos
Produtos encalhados
Ticket médio
Clientes que mais compram
Quantidade de pedidos
Valor médio por pedido
```

# 21. PANDAS

O Pandas entrará principalmente na parte analítica.

Exemplo:

```text
PostgreSQL
    ↓
SQL
    ↓
Pandas DataFrame
    ↓
Análise
```

Podemos analisar:

```text
Total de vendas
Ticket médio
Quantidade de produtos vendidos
Produtos mais vendidos
Marcas mais vendidas
Clientes com maior volume de compras
Vendas por período
Estoque
Produtos sem vendas
Produtos próximos do estoque mínimo
```

Isso transforma o projeto em algo maior do que simplesmente uma loja.

# 22. DASHBOARD

O Streamlit poderá apresentar:

```text
====================================
        DASHBOARD DA LOJA
====================================

Faturamento       Pedidos       Clientes
R$ 125.450         347           182


Produtos vendidos
████████████████


Vendas por período
[GRÁFICO]


Produtos mais vendidos
[ TABELA ]


Estoque crítico
[ TABELA ]
====================================
```

# 23. ORDEM DE DESENVOLVIMENTO

Não vamos construir tudo de uma vez.

A ordem será:

## FASE 1 — Banco de dados

Criar:

```text
PostgreSQL
   ↓
Banco da loja
   ↓
Tabelas
   ↓
Relacionamentos
```

Primeiro:

- empresa
    
- clientes
    
- produtos
    
- estoque
    

## FASE 2 — Inserção dos dados

Criar:

- empresa fictícia
    
- clientes fictícios
    
- 100+ produtos
    
- estoque inicial
    

## FASE 3 — Python + PostgreSQL

Criar a conexão:

```text
Python
   ↓
PostgreSQL
```

E testar:

```text
INSERT
SELECT
UPDATE
DELETE
```

## FASE 4 — Cadastro de clientes

Criar:

```text
Cadastrar
Consultar
Editar
Excluir
Pesquisar
```

Aqui começaremos a trabalhar bastante com SQL.

## FASE 5 — Catálogo

Criar:

```text
Lista de produtos
Busca
Filtros
Detalhes
Estoque
```

## FASE 6 — Carrinho

Criar:

```text
Adicionar
Remover
Alterar quantidade
Subtotal
```

## FASE 7 — Descontos

Implementar as regras de desconto.

```text
Subtotal
   ↓
Regra de desconto
   ↓
Valor do desconto
   ↓
Total
```

## FASE 8 — Fidelidade

Criar:

```text
Cartão
Pontos
Níveis
Histórico
```

## FASE 9 — Finalização

Criar:

```text
Compra com cadastro
Compra sem cadastro
Pedido
Itens do pedido
Atualização do estoque
```

## FASE 10 — Reserva

Implementar:

```text
Produto sem estoque
        ↓
Reserva
        ↓
Fila
```

## FASE 11 — Solicitação de produtos

Criar:

```text
Produto inexistente
        ↓
Solicitação
        ↓
Registro no banco
```

## FASE 12 — Dashboard

Finalmente:

```text
PostgreSQL
     ↓
SQL
     ↓
Pandas
     ↓
Streamlit
     ↓
Dashboard
```

# 24. FLUXO COMPLETO DO SISTEMA

O projeto completo funcionará aproximadamente assim:

```text
                    LOJA
                     │
          ┌──────────┴──────────┐
          │                     │
       CLIENTE               ADMIN
          │                     │
          ▼                     ▼
      CATÁLOGO              PRODUTOS
          │                  ESTOQUE
          ▼                  CLIENTES
       PRODUTO               PEDIDOS
          │                  RELATÓRIOS
          ▼
       CARRINHO
          │
          ▼
      DESCONTO
          │
          ▼
    COM OU SEM CADASTRO
          │
          ▼
       PEDIDO
          │
     ┌────┴─────┐
     ▼          ▼
  ESTOQUE    FIDELIDADE
                │
                ▼
              PONTOS

Produto sem estoque
        │
        ├──► RESERVA
        │
        └──► SOLICITAÇÃO
```

# 25. OBJETIVO FINAL DO PORTFÓLIO

Ao terminar, teremos um projeto que demonstra:

```text
Python
│
├── Lógica de programação
├── Funções
├── Classes
├── Estruturas de dados
├── Tratamento de erros
│
SQL
│
├── SELECT
├── INSERT
├── UPDATE
├── DELETE
├── JOIN
├── GROUP BY
├── ORDER BY
├── Subqueries
└── Relacionamentos
│
PostgreSQL
│
├── Tabelas
├── Chaves primárias
├── Chaves estrangeiras
├── Constraints
└── Integridade dos dados
│
Pandas
│
├── DataFrames
├── Limpeza
├── Agrupamentos
└── Análise
│
Streamlit
│
├── Interface
├── Formulários
├── Carrinho
├── Dashboard
└── Relatórios
```

## RESULTADO

No final, não teremos apenas uma "loja feita em Python".

Teremos uma pequena simulação de um **sistema comercial completo**, com banco de dados relacional, regras de negócio, controle de estoque, vendas, fidelidade e análise de dados.

A construção será incremental:

```text
BANCO
  ↓
DADOS
  ↓
PYTHON
  ↓
REGRAS
  ↓
CARRINHO
  ↓
PEDIDOS
  ↓
FIDELIDADE
  ↓
ESTOQUE
  ↓
STREAMLIT
  ↓
PANDAS
  ↓
DASHBOARD
```

Cada etapa será testada antes de passar para a próxima.