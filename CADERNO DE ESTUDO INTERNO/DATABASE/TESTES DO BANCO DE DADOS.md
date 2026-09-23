# DOCUMENTAÇÃO DOS TESTES DO BANCO DE DADOS

## Projeto: Loja Virtual de Relógios

**Banco:** `loja_relogios`  
**PostgreSQL:** 18.6  
**Data dos testes:** 20/09/2026  
**Total de testes realizados:** 50  
**Status:** APROVADO

---

Esta documentação registra os testes realizados no banco de dados do projeto `loja_relogios`.

O objetivo foi verificar:

- existência dos dados;
    
- funcionamento das operações SQL;
    
- relacionamentos entre tabelas;
    
- integridade dos dados;
    
- regras financeiras;
    
- estoque;
    
- fidelidade;
    
- pedidos;
    
- reservas;
    
- solicitações;
    
- datas históricas;
    
- constraints do PostgreSQL.
    

---

# 2. ESTRUTURA VALIDADA

O banco possui as seguintes tabelas:

```text
empresa
clientes
produtos
cartao_fidelidade
pedidos
itens_pedido
reservas
solicitacoes_produto
```

---

# 3. QUANTIDADE FINAL DE DADOS

Após os testes:

```text
Empresa                  1
Clientes                10
Produtos               112
Cartões de fidelidade   10
Pedidos                105
Itens de pedidos       105
Reservas                45
Solicitações             3
```

Os testes não alteraram indevidamente essas quantidades.

---

# 4. TESTES REALIZADOS

## TESTE 1 — SELECT

### Objetivo

Verificar se todas as tabelas principais possuíam dados.

### Resultado

```text
Empresas:       1
Clientes:      10
Produtos:     112
Cartões:       10
Pedidos:      105
Itens:        105
Reservas:      45
Solicitações:   3
```

### Status

**APROVADO**

---

# TESTE 2 — INSERT

### Objetivo

Verificar a inserção de um novo cliente.

Foi inserido temporariamente:

```text
CLIENTE TESTE
CPF: 999.999.999-99
```

### Resultado

O registro foi inserido corretamente.

### Status

**APROVADO**

---

# TESTE 3 — UPDATE

### Objetivo

Verificar alteração de dados de cliente.

Foram alterados:

```text
Email
Telefone
```

### Resultado

Os dados foram atualizados corretamente.

### Status

**APROVADO**

---

# TESTE 4 — DELETE

### Objetivo

Verificar exclusão de um registro de teste.

O cliente temporário foi removido.

### Resultado

O cliente não estava mais presente no banco.

### Status

**APROVADO**

---

# TESTE 5 — CLIENTE → CARTÃO

### Objetivo

Verificar o relacionamento entre:

```text
clientes
     ↓
cartao_fidelidade
```

### Resultado

Os 10 clientes possuem relacionamento correto com seus cartões.

### Status

**APROVADO**

---

# TESTE 6 — CLIENTE → PEDIDOS

### Objetivo

Verificar o relacionamento entre clientes e pedidos.

### Resultado

Os pedidos estão relacionados aos clientes corretamente.

### Status

**APROVADO**

---

# TESTE 7 — PEDIDO → ITEM → PRODUTO

### Objetivo

Verificar o relacionamento:

```text
pedido
   ↓
itens_pedido
   ↓
produto
```

### Resultado

Os itens estão vinculados corretamente aos pedidos e produtos.

### Status

**APROVADO**

---

# TESTE 8 — CLIENTE → RESERVA → PRODUTO

### Objetivo

Verificar o relacionamento das reservas.

### Resultado

As reservas possuem cliente e produto válidos.

### Status

**APROVADO**

---

# TESTE 9 — CLIENTE → SOLICITAÇÃO

### Objetivo

Verificar o relacionamento das solicitações de produtos.

### Resultado

As solicitações estão relacionadas corretamente aos clientes.

### Status

**APROVADO**

---

# TESTE 10 — CÁLCULO DO PEDIDO

### Regra

```text
total = subtotal - desconto
```

### Resultado

Nenhum pedido apresentou inconsistência.

### Status

**APROVADO**

---

# TESTE 11 — SUBTOTAL DOS ITENS

### Regra

```text
subtotal = quantidade × preco_unitario
```

### Resultado

Nenhum item apresentou inconsistência.

### Status

**APROVADO**

---

# TESTE 12 — ESTOQUE NEGATIVO

### Objetivo

Verificar produtos com estoque menor que zero.

### Resultado

Nenhum produto apresentou estoque negativo.

### Status

**APROVADO**

---

# TESTE 13 — ESTOQUE ABAIXO DO MÍNIMO

### Objetivo

Identificar produtos abaixo do estoque mínimo.

Foram encontrados produtos com:

```text
estoque = 0
estoque_minimo = 1
```

Esses registros foram considerados situações válidas de estoque crítico.

### Status

**APROVADO**

---

# TESTE 14 — ESTOQUE ZERO × DISPONIBILIDADE

### Problema encontrado

Existiam produtos com:

```text
estoque = 0
disponivel = TRUE
```

### Correção

Os produtos esgotados foram atualizados para:

```text
disponivel = FALSE
```

### Resultado

A inconsistência foi corrigida.

### Status

**APROVADO**

---

# TESTE 15 — CPF DUPLICADO

### Objetivo

Verificar CPFs repetidos.

### Resultado

Nenhum CPF duplicado encontrado.

### Status

**APROVADO**

---

# TESTE 16 — PRODUTOS DUPLICADOS

### Objetivo

Verificar produtos com a mesma combinação:

```text
marca + modelo
```

### Resultado

Nenhuma duplicidade encontrada.

### Status

**APROVADO**

---

# TESTE 17 — FORMAS DE PAGAMENTO

Foram encontrados pedidos concluídos utilizando:

```text
Pix
Boleto
Cartão de Crédito
```

Distribuição:

```text
Pix                 38 pedidos
Boleto              35 pedidos
Cartão de Crédito   27 pedidos
```

### Status

**APROVADO**

---

# TESTE 18 — STATUS DOS PEDIDOS

Resultado:

```text
Cancelado       1
Concluido     100
Enviado         1
Pendente        2
Processando     1
```

### Total

```text
105 pedidos
```

### Status

**APROVADO**

---

# TESTE 19 — STATUS DAS RESERVAS

Resultado:

```text
Aguardando      22
Cancelada        6
Convertida      17
```

### Total

```text
45 reservas
```

### Status

**APROVADO**

---

# TESTE 20 — STATUS DAS SOLICITAÇÕES

Resultado:

```text
Solicitado      3
```

### Total

```text
3 solicitações
```

### Status

**APROVADO**

---

# TESTE 21 — PEDIDOS → CLIENTES

### Objetivo

Verificar pedidos apontando para clientes inexistentes.

### Resultado

```text
0 registros inválidos
```

### Status

**APROVADO**

---

# TESTE 22 — ITENS → PEDIDOS → PRODUTOS

### Objetivo

Verificar possíveis registros órfãos.

### Resultado

```text
0 registros inválidos
```

### Status

**APROVADO**

---

# TESTE 23 — RESERVAS → CLIENTES → PRODUTOS

### Objetivo

Verificar possíveis registros órfãos nas reservas.

### Resultado

```text
0 registros inválidos
```

### Status

**APROVADO**

---

# TESTE 24 — SOLICITAÇÕES → CLIENTES

### Objetivo

Verificar clientes inválidos nas solicitações.

### Resultado

```text
0 registros inválidos
```

### Status

**APROVADO**

---

# TESTE 25 — CARTÕES DUPLICADOS

### Objetivo

Verificar números de cartão repetidos.

### Resultado

```text
0 duplicidades
```

### Status

**APROVADO**

---

# TESTE 26 — UM CARTÃO POR CLIENTE

### Objetivo

Verificar se algum cliente possui mais de um cartão.

### Resultado

```text
0 duplicidades
```

### Status

**APROVADO**

---

# TESTE 27 — PONTOS NEGATIVOS

### Objetivo

Verificar pontos menores que zero.

### Resultado

```text
0 cartões com pontos negativos
```

### Status

**APROVADO**

---

# TESTE 28 — PONTOS × NÍVEL

### Regras

```text
Bronze: < 1000 pontos

Prata: 1000 até 2999 pontos

Ouro: >= 3000 pontos
```

### Resultado

Todos os níveis estão compatíveis com a quantidade de pontos.

### Status

**APROVADO**

---

# TESTE 29 — PREÇO E CUSTO NEGATIVOS

### Objetivo

Verificar valores financeiros negativos nos produtos.

### Resultado

```text
0 produtos inválidos
```

### Status

**APROVADO**

---

# TESTE 30 — CUSTO MAIOR QUE PREÇO

### Objetivo

Verificar produtos em que:

```text
custo > preco
```

### Resultado

```text
0 produtos
```

### Status

**APROVADO**

---

# TESTE 31 — PEDIDOS CONCLUÍDOS COM PAGAMENTO

### Objetivo

Verificar se pedidos concluídos possuem forma de pagamento.

### Resultado

```text
0 pedidos sem forma de pagamento
```

### Status

**APROVADO**

---

# TESTE 32 — CAMPOS ESSENCIAIS DOS PRODUTOS

Foram verificados:

```text
marca
modelo
preço
custo
estoque
estoque mínimo
```

### Resultado

Nenhum produto apresentou campo essencial vazio.

### Status

**APROVADO**

---

# TESTE 33 — CAMPOS ESSENCIAIS DOS PEDIDOS

Foram verificados:

```text
subtotal
desconto
total
status
```

### Resultado

Nenhum pedido apresentou campo essencial vazio.

### Status

**APROVADO**

---

# TESTE 34 — DISTRIBUIÇÃO DOS PEDIDOS POR ANO

Resultado:

```text
2024    60 pedidos
2025    40 pedidos
2026     5 pedidos
```

### Total

```text
105 pedidos
```

### Objetivo

Garantir dados históricos para análise temporal.

### Status

**APROVADO**

---

# TESTE 35 — DATAS INVÁLIDAS

### Objetivo

Verificar:

- datas nulas;
    
- datas futuras.
    

### Resultado

```text
0 registros inválidos
```

### Status

**APROVADO**

---

# TESTE 36 — QUANTIDADE DOS ITENS

### Regra

```text
quantidade > 0
```

### Resultado

Nenhum item apresentou quantidade zero ou negativa.

### Status

**APROVADO**

---

# TESTE 37 — ESTOQUE × DISPONIBILIDADE

### Objetivo

Verificar produtos com estoque positivo marcados incorretamente como indisponíveis.

### Resultado

Nenhuma inconsistência encontrada.

### Status

**APROVADO**

---

# TESTE 38 — CLIENTES SEM CARTÃO

### Objetivo

Verificar clientes sem cartão de fidelidade.

### Resultado

```text
0 clientes sem cartão
```

### Status

**APROVADO**

---

# TESTE 39 — ESTOQUE MÍNIMO NEGATIVO

### Objetivo

Verificar valores inválidos em `estoque_minimo`.

### Resultado

```text
0 produtos inválidos
```

### Status

**APROVADO**

---

# TESTE 40 — DADOS BÁSICOS DOS CLIENTES

Foram verificados:

```text
nome
CPF
status
```

### Resultado

Nenhum cliente apresentou esses campos obrigatórios vazios.

### Status

**APROVADO**

---

# TESTE 41 — PEDIDOS SEM ITENS

### Objetivo

Verificar pedidos que não possuem nenhum item.

### Resultado

```text
0 pedidos sem itens
```

### Status

**APROVADO**

---

# TESTE 42 — PRODUTOS SEM DESCRIÇÃO

### Resultado

```text
produtos_sem_descricao = 0
```

Todos os 112 produtos possuem descrição.

### Status

**APROVADO**

---

# TESTE 43 — PRODUTOS SEM CATEGORIA

### Resultado

```text
produtos_sem_categoria = 0
```

Todos os produtos possuem categoria.

### Status

**APROVADO**

---

# TESTE 44 — MARCAS

### Resultado

```text
13 marcas cadastradas
0 produtos sem marca
```

### Status

**APROVADO**

---

# TESTE 45 — VALORES FINANCEIROS DOS PEDIDOS

Foram verificadas as seguintes regras:

```text
subtotal >= 0
desconto >= 0
total >= 0
desconto <= subtotal
total = subtotal - desconto
```

### Resultado

```text
0 inconsistências
```

### Status

**APROVADO**

---

# TESTE 46 — ESTOQUE TOTAL

Resultado:

```text
Produtos:             112
Estoque total:        495 unidades
Produtos esgotados:     7
Produtos disponíveis: 105
```

### Status

**APROVADO**

---

# TESTE 47 — PRODUTOS ESGOTADOS

Foram encontrados 7 produtos com estoque zero.

Todos estão corretamente marcados:

```text
estoque = 0
disponivel = FALSE
```

### Produtos

```text
77  Hamilton   Khaki Aviation
79  Hamilton   Khaki Navy
88  TAG Heuer  Aquaracer
89  TAG Heuer  Carrera
95  Seiko      Presage Sharp Edged
99  Hamilton   Khaki King
104 TAG Heuer  Aquaracer Professional
```

### Status

**APROVADO**

---

# TESTE 48 — PEDIDOS × ITENS

### Objetivo

Verificar se:

```text
subtotal do pedido
=
soma dos subtotais dos itens
```

e:

```text
total
=
subtotal - desconto
```

### Resultado

```text
0 inconsistências
```

### Status

**APROVADO**

---

# TESTE 49 — CONSTRAINTS DO POSTGRESQL

Foi realizado um teste controlado com:

```text
preco = -100
```

O banco recusou corretamente o registro.

Erro apresentado:

```text
a nova linha da relação "produtos"
viola a restrição de verificação
"produtos_preco_check"
```

Isso confirma que a constraint está funcionando.

O registro inválido não foi mantido no banco.

### Status

**APROVADO**

---

# TESTE 50 — VERIFICAÇÃO FINAL

Consulta final:

```text
Empresas:        1
Clientes:       10
Produtos:      112
Cartões:        10
Pedidos:       105
Itens:         105
Reservas:       45
Solicitações:    3
```

### Resultado

As quantidades finais estão corretas.

### Status

**APROVADO**

---

# 5. RESULTADO FINAL

## STATUS DO BANCO

```text
========================================
      TESTES DO BANCO DE DADOS
========================================

TESTES REALIZADOS: 50

APROVADOS: 50
REPROVADOS: 0

STATUS: APROVADO
========================================
```

---

# 6. PRINCIPAIS PROBLEMAS ENCONTRADOS E CORRIGIDOS

Durante os testes foi encontrada uma inconsistência:

## Estoque zero × disponibilidade

Alguns produtos possuíam:

```text
estoque = 0
disponivel = TRUE
```

A regra de negócio definida para o projeto exige:

```text
estoque = 0
        ↓
disponivel = FALSE
```

Os registros foram corrigidos.

---

# 7. DADOS HISTÓRICOS

O banco também possui dados históricos para permitir análises no Pandas e no Dashboard.

Distribuição:

```text
2024 → 60 pedidos
2025 → 40 pedidos
2026 → 5 pedidos
```

Isso permitirá futuramente analisar:

```text
vendas por dia
vendas por mês
vendas por ano
comparação 2024 × 2025
ticket médio
faturamento
formas de pagamento
produtos vendidos
estoque
clientes
```

---

# 8. PONTOS QUE AINDA SERÃO IMPLEMENTADOS

Apesar do banco estar aprovado nos testes, existem algumas regras de negócio que ainda poderão ser automatizadas.

## 8.1 Pontos de fidelidade automáticos

Atualmente os pontos e níveis foram cadastrados/testados.

Ainda será necessário definir e implementar a regra automática:

```text
Compra
   ↓
Valor da compra
   ↓
Cálculo de pontos
   ↓
Atualização do cartão
   ↓
Atualização do nível
```

A fórmula exata dos pontos ainda precisa ser definida.

---

## 8.2 Disponibilidade automática

Atualmente a disponibilidade foi corrigida manualmente.

Posteriormente podemos implementar:

```text
Estoque > 0
    ↓
disponivel = TRUE

Estoque = 0
    ↓
disponivel = FALSE
```

Isso poderá ser implementado através da lógica da aplicação ou de uma trigger no PostgreSQL.

---

# 9. CONCLUSÃO

O banco de dados `loja_relogios` passou pela bateria principal de testes.

Foram testados:

```text
CRUD
Relacionamentos
Foreign Keys
Constraints
Clientes
Produtos
Pedidos
Itens
Estoque
Fidelidade
Reservas
Solicitações
Pagamentos
Descontos
Valores financeiros
Datas
Dados históricos
Integridade dos registros
```

Resultado final:

```text
50 testes realizados
50 testes aprovados
0 testes reprovados
```

