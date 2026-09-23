# DOCUMENTO MESTRE DO PROJETO

# LOJA VIRTUAL DE RELÓGIOS

**Versão:** 1.0  
**Tipo:** Projeto de estudo e portfólio  
**Status:** Planejamento / início do desenvolvimento  
**Linguagem principal:** Python  
**Banco de dados:** PostgreSQL  
**SQL:** Sim  
**Análise de dados:** Pandas  
**Interface:** Streamlit

---

# 1. IDENTIDADE DO PROJETO

O projeto consiste na criação de uma **loja virtual fictícia de relógios**, desenvolvida como projeto de estudo, prática e portfólio.

A empresa, seus funcionários, clientes, documentos, endereços, telefones, pedidos e demais informações cadastrais serão fictícios.

O catálogo poderá utilizar **marcas reais de relógios** como referência, porém a loja será uma empresa fictícia e não representará uma loja oficial dessas marcas.

O objetivo principal não é criar apenas uma página de venda de produtos.

O objetivo é desenvolver uma pequena simulação de um **sistema comercial completo**, utilizando:

- Python
    
- PostgreSQL
    
- SQL
    
- Pandas
    
- Streamlit
    

O sistema deverá possuir banco de dados relacional, cadastro de clientes, catálogo de produtos, estoque, carrinho, pedidos, descontos, fidelidade, reservas e análise de dados.

---

# 2. OBJETIVO EDUCACIONAL

O projeto deverá servir como uma aplicação prática para estudar e demonstrar conhecimentos de:

## Python

- Variáveis
    
- Condicionais
    
- Laços
    
- Funções
    
- Listas
    
- Dicionários
    
- Tuplas
    
- Classes
    
- Módulos
    
- Importação de arquivos
    
- Tratamento de erros
    
- Manipulação de dados
    
- Regras de negócio
    
- Comunicação com banco de dados
    

## SQL

- SELECT
    
- INSERT
    
- UPDATE
    
- DELETE
    
- WHERE
    
- ORDER BY
    
- GROUP BY
    
- HAVING
    
- JOIN
    
- Subconsultas
    
- Agregações
    
- Chaves primárias
    
- Chaves estrangeiras
    
- Constraints
    
- Relacionamentos
    
- Integridade dos dados
    

## PostgreSQL

- Criação de banco
    
- Criação de tabelas
    
- Relacionamentos
    
- Inserção de dados
    
- Consultas
    
- Atualizações
    
- Integridade
    
- Controle dos dados
    

## Pandas

- DataFrame
    
- Leitura de dados
    
- Tratamento
    
- Filtros
    
- Agrupamentos
    
- Estatísticas
    
- Análise de vendas
    
- Relatórios
    

## Streamlit

- Interface
    
- Formulários
    
- Botões
    
- Tabelas
    
- Filtros
    
- Sessão
    
- Carrinho
    
- Dashboard
    
- Visualização de dados
    

---

# 3. VISÃO GERAL DO SISTEMA

O sistema deverá simular o funcionamento de uma loja de relógios.

Fluxo principal:

```text
CLIENTE
   ↓
CATÁLOGO
   ↓
ESCOLHE PRODUTO
   ↓
ADICIONA AO CARRINHO
   ↓
ALTERA QUANTIDADE
   ↓
SISTEMA CALCULA SUBTOTAL
   ↓
SISTEMA APLICA DESCONTO
   ↓
CLIENTE ESCOLHE:
   ├── COM CADASTRO
   └── SEM CADASTRO
   ↓
FINALIZA PEDIDO
   ↓
ESTOQUE É ATUALIZADO
   ↓
PEDIDO É REGISTRADO
   ↓
SE CLIENTE CADASTRADO:
       ↓
   PONTOS DE FIDELIDADE
```

Caso o produto esteja indisponível:

```text
PRODUTO SEM ESTOQUE
       ↓
   ┌───┴────────────┐
   ↓                ↓
RESERVA       SOLICITAÇÃO
              DE PRODUTO
```

---

# 4. TECNOLOGIAS

## Obrigatórias

```text
Python
PostgreSQL
SQL
Pandas
Streamlit
```

## Bibliotecas que poderão ser utilizadas

```text
psycopg
SQLAlchemy
Pandas
Streamlit
Plotly
```

A escolha definitiva das bibliotecas deverá ser feita durante a implementação.

Não adicionar tecnologias desnecessárias no início.

---

# 5. ARQUITETURA

Arquitetura desejada:

```text
                 USUÁRIO
                    │
                    ▼
               STREAMLIT
                    │
                    ▼
             CAMADA PYTHON
                    │
              REGRAS DE NEGÓCIO
                    │
                    ▼
             POSTGRESQL
                    │
                    ▼
                  DADOS
                    │
                    ▼
                 PANDAS
                    │
                    ▼
              ANÁLISES
```

A interface não deverá concentrar toda a lógica do sistema.

O projeto deverá separar:

```text
INTERFACE
   ↓
SERVIÇOS / REGRAS
   ↓
BANCO DE DADOS
```

---

# 6. ESTRUTURA DE DIRETÓRIOS

Estrutura planejada:

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
├── analysis/
│   └── vendas.py
│
├── data/
│   └── produtos.csv
│
├── requirements.txt
│
└── README.md
```

Essa estrutura poderá ser modificada durante o desenvolvimento caso uma solução mais simples ou adequada seja encontrada.

---

# 7. BANCO DE DADOS

O PostgreSQL será o banco principal do sistema.

Banco sugerido:

```text
loja_relogios
```

Principais entidades:

```text
EMPRESA
CLIENTES
CARTAO_FIDELIDADE
PRODUTOS
ESTOQUE
PEDIDOS
ITENS_PEDIDO
RESERVAS
SOLICITACOES_PRODUTO
```

---

# 8. RELACIONAMENTOS

Relacionamento geral:

```text
EMPRESA
   │
   ├──────── CLIENTES
   │             │
   │             └──── CARTAO_FIDELIDADE
   │
   ├──────── PRODUTOS
   │             │
   │             └──── ESTOQUE
   │
   ├──────── PEDIDOS
   │             │
   │             └──── ITENS_PEDIDO
   │
   ├──────── RESERVAS
   │
   └──────── SOLICITACOES_PRODUTO
```

Relacionamentos principais:

```text
cliente 1 ─── 1 cartão_fidelidade

cliente 1 ─── N pedidos

pedido 1 ─── N itens_pedido

produto 1 ─── N itens_pedido

cliente 1 ─── N reservas

produto 1 ─── N reservas

cliente 1 ─── N solicitacoes_produto
```

---

# 9. EMPRESA

A empresa será fictícia.

Dados planejados:

```text
id
razao_social
nome_fantasia
cnpj_ficticio
telefone
email
logradouro
numero
bairro
cidade
estado
cep
data_cadastro
```

Nenhum dado empresarial real deve ser necessário para o funcionamento do projeto.

---

# 10. CLIENTES

O sistema deverá possuir cadastro completo de clientes fictícios.

Campos planejados:

```text
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

Os CPFs devem ser dados sintéticos.

Não utilizar dados pessoais reais.

O sistema deverá permitir:

```text
Cadastrar cliente
Consultar cliente
Pesquisar cliente
Alterar cliente
Desativar cliente
```

---

# 11. CARTÃO DE FIDELIDADE

Clientes cadastrados poderão possuir um cartão de fidelidade.

Campos:

```text
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
BRONZE
PRATA
OURO
```

A classificação será baseada na quantidade de pontos.

As regras poderão ser ajustadas durante o desenvolvimento.

---

# 12. SISTEMA DE PONTOS

Regra inicial proposta:

```text
A cada R$ 10,00 gastos
= 1 ponto
```

Exemplo:

```text
Compra = R$ 850,00

850 ÷ 10 = 85 pontos
```

Os pontos serão adicionados ao cartão do cliente após a confirmação da compra.

O sistema deverá manter o saldo atualizado.

---

# 13. PRODUTOS

O catálogo deverá possuir inicialmente:

**Mais de 100 produtos.**

Cada produto deverá possuir informações como:

```text
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

Categorias possíveis:

```text
Analógico
Digital
Automático
Esportivo
Social
Mergulho
Smartwatch
Cronógrafo
```

As categorias poderão ser ampliadas.

---

# 14. MARCAS

O catálogo poderá utilizar marcas reais conhecidas como referência.

Exemplos:

```text
Casio
G-Shock
Seiko
Citizen
Orient
Timex
Fossil
Tissot
Technos
```

Os produtos poderão ser:

1. Produtos fictícios inspirados em marcas reais; ou
    
2. Produtos/modelos reais utilizados apenas como referência de catálogo.
    

A loja continuará sendo fictícia.

---

# 15. ESTOQUE

O sistema deverá controlar o estoque.

Exemplo:

```text
Produto X
Estoque = 5
```

Compra de 2 unidades:

```text
5 - 2 = 3
```

Quando:

```text
estoque = 0
```

O produto não poderá ser comprado normalmente.

O sistema deverá impedir que uma compra ultrapasse a quantidade disponível.

---

# 16. CATÁLOGO

O usuário deverá poder:

```text
Visualizar produtos
Pesquisar
Filtrar por marca
Filtrar por categoria
Filtrar por preço
Filtrar por disponibilidade
Ordenar por preço
Visualizar detalhes
Adicionar ao carrinho
```

---

# 17. CARRINHO

O carrinho deverá permitir:

```text
Adicionar produto
Remover produto
Alterar quantidade
Visualizar quantidade
Visualizar preço unitário
Calcular subtotal
Calcular desconto
Calcular total
Finalizar compra
```

Exemplo:

```text
Produto A       R$ 500,00
Produto B       R$ 300,00
Produto C       R$ 200,00

Subtotal        R$ 1.000,00
Desconto        R$   100,00
Total           R$   900,00
```

---

# 18. DESCONTOS

O sistema deverá calcular desconto de acordo com o valor da compra.

Regra inicial:

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

Essas regras são iniciais e poderão ser modificadas.

O desconto deverá ser calculado automaticamente.

---

# 19. COMPRA COM CADASTRO

Fluxo:

```text
Cliente
   ↓
CPF
   ↓
Sistema encontra cliente
   ↓
Carrinho
   ↓
Desconto
   ↓
Finalização
   ↓
Pedido
   ↓
Atualização do estoque
   ↓
Pontuação
```

---

# 20. COMPRA SEM CADASTRO

O cliente também poderá comprar sem possuir cadastro.

Fluxo:

```text
Cliente
   ↓
Comprar sem cadastro
   ↓
Carrinho
   ↓
Dados necessários para pedido
   ↓
Finalização
   ↓
Pedido
   ↓
Estoque atualizado
```

Esse cliente não receberá pontos de fidelidade enquanto não possuir cadastro/cartão.

---

# 21. PEDIDOS

Tabela:

```text
pedidos
```

Campos planejados:

```text
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

---

# 22. ITENS DO PEDIDO

Tabela:

```text
itens_pedido
```

Campos:

```text
id
pedido_id
produto_id
quantidade
preco_unitario
subtotal
```

Um pedido poderá possuir vários produtos.

Exemplo:

```text
PEDIDO 1001

Produto A
Quantidade: 2

Produto B
Quantidade: 1

Produto C
Quantidade: 3
```

---

# 23. RESERVA DE PRODUTO

Quando o produto estiver sem estoque, o cliente poderá solicitar uma reserva.

Fluxo:

```text
Produto
   ↓
Estoque = 0
   ↓
Cliente solicita reserva
   ↓
Reserva registrada
   ↓
Status = Aguardando
```

Tabela:

```text
reservas
```

Campos:

```text
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

---

# 24. SOLICITAÇÃO DE PRODUTO INDISPONÍVEL

Existirá uma diferença entre:

## Produto existente sem estoque

Pode gerar:

```text
RESERVA
```

## Produto que a loja não possui

Pode gerar:

```text
SOLICITAÇÃO DE PRODUTO
```

Tabela:

```text
solicitacoes_produto
```

Campos:

```text
id
cliente_id
nome_produto
marca
modelo
descricao
data_solicitacao
status
```

Status possíveis:

```text
Solicitado
Em análise
Disponível
Atendido
Cancelado
```

---

# 25. ADMINISTRAÇÃO

A área administrativa deverá permitir visualizar:

```text
Clientes
Produtos
Estoque
Pedidos
Reservas
Solicitações
```

Posteriormente poderá incluir:

```text
Faturamento
Ticket médio
Produtos mais vendidos
Marcas mais vendidas
Produtos sem venda
Estoque crítico
Clientes com maior número de compras
```

---

# 26. PANDAS

O Pandas será utilizado principalmente para análise.

Fluxo:

```text
PostgreSQL
     ↓
SQL
     ↓
Pandas
     ↓
DataFrame
     ↓
Análise
     ↓
Dashboard
```

Análises planejadas:

```text
Faturamento total
Quantidade de pedidos
Ticket médio
Quantidade de produtos vendidos
Produtos mais vendidos
Marcas mais vendidas
Vendas por período
Clientes com maior volume de compras
Estoque atual
Produtos sem vendas
Produtos com estoque baixo
```

---

# 27. STREAMLIT

O Streamlit será utilizado para criar a interface.

Páginas planejadas:

```text
Início
Produtos
Carrinho
Clientes
Pedidos
Fidelidade
Administração
Dashboard
```

---

# 28. DASHBOARD

O dashboard deverá apresentar indicadores como:

```text
Faturamento
Pedidos
Clientes
Produtos vendidos
Ticket médio
```

Além de gráficos e tabelas:

```text
Vendas por período
Produtos mais vendidos
Marcas mais vendidas
Estoque crítico
```

---

# 29. REGRAS IMPORTANTES DO PROJETO

## Regra 1

Nenhum dado pessoal real deverá ser utilizado.

## Regra 2

A empresa será fictícia.

## Regra 3

O sistema deve ser desenvolvido gradualmente.

## Regra 4

Cada etapa deve ser testada antes da próxima.

## Regra 5

O banco PostgreSQL será a fonte principal dos dados.

## Regra 6

Python será responsável pela lógica da aplicação.

## Regra 7

Streamlit será responsável principalmente pela interface.

## Regra 8

Pandas será utilizado principalmente para análise.

## Regra 9

SQL deverá ser utilizado de forma significativa no projeto.

## Regra 10

Não adicionar tecnologias desnecessárias antes de concluir a base do projeto.

---

# 30. ORDEM OFICIAL DE DESENVOLVIMENTO

A implementação deverá seguir esta ordem.

## FASE 1 — BANCO

Criar:

```text
Banco PostgreSQL
Schema
Tabelas
Chaves
Relacionamentos
Constraints
```

---

## FASE 2 — DADOS INICIAIS

Inserir:

```text
Empresa fictícia
Clientes fictícios
100+ produtos
Estoque
```

---

## FASE 3 — CONEXÃO PYTHON + POSTGRESQL

Criar:

```text
connection.py
```

Testar:

```text
SELECT
INSERT
UPDATE
DELETE
```

---

## FASE 4 — CLIENTES

Implementar:

```text
Cadastrar
Consultar
Pesquisar
Editar
Desativar
```

---

## FASE 5 — PRODUTOS

Implementar:

```text
Catálogo
Pesquisa
Filtros
Detalhes
Estoque
```

---

## FASE 6 — CARRINHO

Implementar:

```text
Adicionar
Remover
Alterar quantidade
Subtotal
```

---

## FASE 7 — DESCONTOS

Implementar:

```text
Cálculo automático
```

---

## FASE 8 — FINALIZAÇÃO DE COMPRA

Implementar:

```text
Com cadastro
Sem cadastro
Pedido
Itens
Estoque
```

---

## FASE 9 — FIDELIDADE

Implementar:

```text
Cartão
Pontos
Níveis
Histórico
```

---

## FASE 10 — RESERVAS

Implementar:

```text
Produto sem estoque
Reserva
Fila
Status
```

---

## FASE 11 — SOLICITAÇÕES

Implementar:

```text
Produto inexistente
Solicitação
Status
```

---

## FASE 12 — ADMINISTRAÇÃO

Implementar:

```text
Clientes
Produtos
Pedidos
Estoque
Reservas
Solicitações
```

---

## FASE 13 — PANDAS

Implementar:

```text
DataFrames
Consultas analíticas
Agrupamentos
Indicadores
```

---

## FASE 14 — DASHBOARD

Implementar:

```text
Indicadores
Gráficos
Tabelas
Filtros
```

---

# 31. FLUXO DE DESENVOLVIMENTO

Sempre que uma nova funcionalidade for criada, seguir:

```text
1. Definir o objetivo
        ↓
2. Definir os dados necessários
        ↓
3. Verificar o banco
        ↓
4. Criar/alterar SQL
        ↓
5. Criar lógica Python
        ↓
6. Testar Python
        ↓
7. Criar interface Streamlit
        ↓
8. Testar integração
        ↓
9. Corrigir erros
        ↓
10. Documentar
```

---

# 32. METODOLOGIA DE APRENDIZADO

O projeto deverá ser desenvolvido de forma didática.

Não entregar grandes blocos de código sem explicação.

Preferência:

```text
EXPLICAR
   ↓
CRIAR PEQUENO BLOCO
   ↓
TESTAR
   ↓
ENTENDER
   ↓
AVANÇAR
```

Quando houver um erro:

```text
1. Identificar o erro
2. Explicar o motivo
3. Corrigir
4. Testar novamente
5. Continuar
```

O objetivo não é apenas fazer o programa funcionar.

O objetivo é entender como o programa funciona.

---

# 33. ESTADO DO PROJETO

No momento em que este documento foi criado:

```text
[ ] Banco do projeto criado
[ ] Tabelas criadas
[ ] Relacionamentos criados
[ ] Dados iniciais inseridos
[ ] 100+ produtos cadastrados
[ ] Conexão Python/PostgreSQL
[ ] Cadastro de clientes
[ ] Catálogo
[ ] Carrinho
[ ] Descontos
[ ] Pedidos
[ ] Estoque
[ ] Fidelidade
[ ] Reservas
[ ] Solicitação de produtos
[ ] Administração
[ ] Pandas
[ ] Dashboard
```

O projeto está na fase de:

```text
PLANEJAMENTO / INÍCIO DA IMPLEMENTAÇÃO
```

---

# 34. CRITÉRIO DE CONCLUSÃO

O projeto será considerado funcional quando for possível realizar este fluxo completo:

```text
ABRIR SISTEMA
      ↓
VISUALIZAR CATÁLOGO
      ↓
ESCOLHER PRODUTO
      ↓
ADICIONAR AO CARRINHO
      ↓
ADICIONAR OUTROS PRODUTOS
      ↓
ALTERAR QUANTIDADES
      ↓
VER SUBTOTAL
      ↓
CALCULAR DESCONTO
      ↓
IDENTIFICAR CLIENTE
      ↓
FINALIZAR COMPRA
      ↓
CRIAR PEDIDO
      ↓
ATUALIZAR ESTOQUE
      ↓
CALCULAR PONTOS
      ↓
ATUALIZAR CARTÃO
      ↓
REGISTRAR VENDA
      ↓
ANALISAR VENDA COM PANDAS
      ↓
EXIBIR RESULTADO NO STREAMLIT
```

Também deverá ser possível:

```text
Produto sem estoque
      ↓
Reserva
```

e:

```text
Produto inexistente
      ↓
Solicitação de produto
```

---

# 35. VISÃO FINAL

O projeto deverá representar uma pequena empresa virtual funcionando de maneira integrada:

```text
                    LOJA
                     │
       ┌─────────────┼─────────────┐
       │             │             │
    CLIENTES      PRODUTOS       PEDIDOS
       │             │             │
       │          ESTOQUE          │
       │             │             │
       └─────────────┼─────────────┘
                     │
                  CARRINHO
                     │
                  DESCONTO
                     │
                 PAGAMENTO
                     │
                   VENDA
                     │
              ┌──────┴──────┐
              │             │
          ESTOQUE       FIDELIDADE
                            │
                          PONTOS

              ┌─────────────┴─────────────┐
              │                           │
           RESERVAS                 SOLICITAÇÕES
              │                           │
              └─────────────┬─────────────┘
                            │
                       POSTGRESQL
                            │
                           SQL
                            │
                         PANDAS
                            │
                       STREAMLIT
                            │
                        DASHBOARD
```

---

# 36. INSTRUÇÃO PARA CONTINUAÇÃO FUTURA

Quando este documento for apresentado novamente em uma conversa futura, considerar que ele representa a especificação-base do projeto.

Antes de iniciar qualquer implementação:

1. Ler todo o documento.
    
2. Identificar a fase atual.
    
3. Verificar quais itens já foram concluídos.
    
4. Não recriar funcionalidades que já estejam concluídas.
    
5. Manter a arquitetura existente sempre que possível.
    
6. Fazer alterações incrementais.
    
7. Explicar cada etapa de forma simples.
    
8. Testar cada etapa antes de avançar.
    
9. Manter PostgreSQL como banco principal.
    
10. Manter Python como linguagem principal.
    
11. Utilizar SQL de forma significativa.
    
12. Utilizar Pandas para análise.
    
13. Utilizar Streamlit para interface.
    
14. Não adicionar tecnologias sem necessidade.
    
15. Preservar as regras de negócio já definidas neste documento.
    

Se o projeto já estiver parcialmente desenvolvido, primeiro deve ser feita uma análise do estado atual dos arquivos e do banco antes de propor alterações.

---

# 37. PRINCÍPIO FUNDAMENTAL

Este projeto não deve ser tratado apenas como um exercício de programação.

Ele deve ser construído como uma **simulação de um sistema comercial real**, em escala reduzida, permitindo estudar simultaneamente:

```text
PROGRAMAÇÃO
+
BANCO DE DADOS
+
SQL
+
REGRAS DE NEGÓCIO
+
ANÁLISE DE DADOS
+
INTERFACE
```

A prioridade é construir uma base sólida, compreender cada etapa e evoluir o sistema gradualmente.