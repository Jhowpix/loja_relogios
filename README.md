# ⌚ Kairos Watch Co.
Sistema de gestão e loja virtual de relógios desenvolvido como projeto de estudo e portfólio.
<br>
<img width="1599" height="899" alt="Captura de tela 2026-09-23 205729" src="https://github.com/user-attachments/assets/7da4093e-e2ab-4c23-90b3-a0590291e576" />
<br>

O projeto simula o funcionamento de uma loja de relógios, permitindo trabalhar com:

* Cadastro e consulta de clientes
* Catálogo de produtos
* Estoque
* Carrinho de compras
* Pedidos
* Descontos
* Sistema de fidelidade
* Reservas de produtos
* Solicitação de produtos
* Análise de vendas
* Dashboard

## 🛠️ Tecnologias utilizadas

### Python

Utilizado como principal linguagem de programação do projeto.

Responsável pela lógica da aplicação, regras de negócio e integração entre os diferentes componentes.

### PostgreSQL

Banco de dados utilizado para armazenar as informações da loja.

Armazena dados como:

* Clientes
* Produtos
* Pedidos
* Itens dos pedidos
* Estoque
* Cartões de fidelidade
* Reservas
* Solicitações de produtos

### SQL

Utilizado para criar, consultar e manipular os dados armazenados no PostgreSQL.

### Pandas

Utilizado para análise e tratamento dos dados de vendas e outras informações da loja.

### Streamlit

Utilizado para criar a interface web da aplicação e apresentar os dados de forma visual.

### Git e GitHub

Utilizados para versionamento, organização e publicação do projeto como portfólio.

## 🏗️ Estrutura do projeto

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

## 📊 Dados

O projeto utiliza dados fictícios para simular uma loja de relógios.

Atualmente, o banco possui produtos, clientes, pedidos, reservas e outros dados utilizados para testes e análises.

## 🚀 Objetivo de aprendizado

Este projeto está sendo desenvolvido passo a passo para consolidar conhecimentos em:

O desenvolvimento também busca manter o código organizado, compreensível e próximo de uma estrutura utilizada em projetos reais.

## 📌 Status

🚧 Em desenvolvimento

Novas funcionalidades serão adicionadas conforme o desenvolvimento do projeto.
