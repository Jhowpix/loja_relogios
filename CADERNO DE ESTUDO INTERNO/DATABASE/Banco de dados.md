comandos para startar o banco de dados 

& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres

CREATE DATABASE loja_relogios;

\c loja_relogios

CREATE TABLE empresa (
    id SERIAL PRIMARY KEY,
    razao_social VARCHAR(150) NOT NULL,
    nome_fantasia VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(150),
    endereco VARCHAR(200),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    cep VARCHAR(10),
    data_cadastro DATE DEFAULT CURRENT_DATE
);


INSERT INTO empresa (
    razao_social,
    nome_fantasia,
    cnpj,
    telefone,
    email,
    endereco,
    cidade,
    estado,
    cep
)
VALUES (
    'Kairos Comercio Eletronico de Relogios e Acessorios Ltda.',
    'Kairos Watch Co.',
    '48.912.304/0001-58',
    '0800 795 2020',
    'suporte@kairoswatch.com.br',
    'Av. das Nacoes Unidas, 12901 - Bloco A, Conjunto 1402, Brooklin Paulista',
    'Sao Paulo',
    'SP',
    '04578-910'
);

tudo digitado precisa ser cuidadosamente analisado pois um erro tem que recriar o cadastro para preencher novamente

SELECT * FROM empresa;
\d empresa

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    data_nascimento DATE,
    telefone VARCHAR(20),
    email VARCHAR(150),
    logradouro VARCHAR(150),
    numero VARCHAR(10),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    cep VARCHAR(10),
    data_cadastro DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'ativo'
);

\dt
\d clientes

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    modelo VARCHAR(150) NOT NULL,
    referencia VARCHAR(100),
    categoria VARCHAR(100),
    descricao TEXT,
    preco NUMERIC(12,2) NOT NULL CHECK (preco >= 0),
    custo NUMERIC(12,2) NOT NULL CHECK (custo >= 0),
    estoque INTEGER NOT NULL DEFAULT 0 CHECK (estoque >= 0),
    estoque_minimo INTEGER NOT NULL DEFAULT 1 CHECK (estoque_minimo >= 0),
    disponivel BOOLEAN DEFAULT TRUE,
    data_cadastro DATE DEFAULT CURRENT_DATE
);

\dt
\d produtos


CREATE TABLE cartao_fidelidade (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL UNIQUE,
    numero_cartao VARCHAR(30) UNIQUE NOT NULL,
    pontos INTEGER NOT NULL DEFAULT 0 CHECK (pontos >= 0),
    nivel VARCHAR(20) DEFAULT 'Bronze',
    data_criacao DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'ativo',
    CONSTRAINT fk_cartao_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
);

\dt
\d cartao_fidelidade

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    subtotal NUMERIC(12,2) NOT NULL CHECK (subtotal >= 0),
    desconto NUMERIC(12,2) NOT NULL DEFAULT 0 CHECK (desconto >= 0),
    total NUMERIC(12,2) NOT NULL CHECK (total >= 0),
    status VARCHAR(30) DEFAULT 'Pendente',
    forma_pagamento VARCHAR(30),
    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
);

\dt
\d pedidos

CREATE TABLE itens_pedido (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario NUMERIC(12,2) NOT NULL CHECK (preco_unitario >= 0),
    subtotal NUMERIC(12,2) NOT NULL CHECK (subtotal >= 0),
    CONSTRAINT fk_item_pedido
        FOREIGN KEY (pedido_id)
        REFERENCES pedidos(id),
    CONSTRAINT fk_item_produto
        FOREIGN KEY (produto_id)
        REFERENCES produtos(id)
);

\dt
\d itens_pedido

CREATE TABLE reservas (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    data_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) DEFAULT 'Aguardando',
    CONSTRAINT fk_reserva_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id),
    CONSTRAINT fk_reserva_produto
        FOREIGN KEY (produto_id)
        REFERENCES produtos(id)
);

\dt
\d reservas

CREATE TABLE solicitacoes_produto (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER,
    nome_produto VARCHAR(150) NOT NULL,
    marca VARCHAR(100),
    modelo VARCHAR(150),
    descricao TEXT,
    data_solicitacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) DEFAULT 'Solicitado',
    CONSTRAINT fk_solicitacao_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
);

\dt
\d solicitacoes_produto

\dt

SELECT id, nome_fantasia, cidade, estado
FROM empresa;

SELECT
    (SELECT COUNT(*) FROM clientes) AS clientes,
    (SELECT COUNT(*) FROM produtos) AS produtos,
    (SELECT COUNT(*) FROM pedidos) AS pedidos,
    (SELECT COUNT(*) FROM itens_pedido) AS itens,
    (SELECT COUNT(*) FROM reservas) AS reservas,
    (SELECT COUNT(*) FROM solicitacoes_produto) AS solicitacoes;


INSERT INTO clientes (
    nome, cpf, data_nascimento, telefone, email,
    logradouro, numero, bairro, cidade, estado, cep
)
VALUES (
    'Carlos Eduardo Martins',
    '123.456.789-01',
    '1990-05-15',
    '(11) 98888-1111',
    'carlos.martins@email.com',
    'Rua das Flores',
    '100',
    'Centro',
    'Sao Paulo',
    'SP',
    '01000-000'
);

ALTER TABLE clientes
RENAME COLUMN lagradouro TO logradouro;

\d clientes

ALTER TABLE clientes
ALTER COLUMN logradouro TYPE VARCHAR(150);

ALTER TABLE clientes
ALTER COLUMN telefone TYPE VARCHAR(20);

\d clientes

INSERT INTO produtos (
    marca, modelo, referencia, categoria, descricao,
    preco, custo, estoque, estoque_minimo
)
VALUES (
    'Casio',
    'G-Shock GA-2100',
    'GA-2100-1A1',
    'Casual',
    'Relogio esportivo digital e analogico',
    699.90,
    400.00,
    10,
    2
);

SELECT * FROM produtos;

UPDATE produtos
SET estoque = 1
WHERE id = 1;

SELECT id, marca, modelo, preco, estoque
FROM produtos;

INSERT INTO produtos (
    marca, modelo, referencia, categoria, descricao,
    preco, custo, estoque, estoque_minimo
)
VALUES
(
    'Seiko',
    '5 Sports',
    'SRPD55K1',
    'Automatico',
    'Relogio automatico esportivo',
    1899.90,
    1100.00,
    8,
    2
),
(
    'Orient',
    'Bambino',
    'RA-AC0M04Y10B',
    'Social',
    'Relogio automatico classico',
    1299.90,
    750.00,
    6,
    2
),
(
    'Citizen',
    'Eco-Drive',
    'BM8478-01L',
    'Casual',
    'Relogio com tecnologia Eco-Drive',
    999.90,
    600.00,
    7,
    2
),
(
    'Tissot',
    'PRX',
    'T137.410.11.041.00',
    'Social',
    'Relogio quartz de estilo integrado',
    3499.90,
    2200.00,
    4,
    1
),
(
    'Casio',
    'Edifice',
    'EFR-S108D',
    'Casual',
    'Relogio analogico esportivo',
    899.90,
    500.00,
    9,
    2
);


SELECT id, marca, modelo, preco, estoque
FROM produtos
ORDER BY id;

SELECT marca, modelo, estoque
FROM produtos
WHERE estoque <= estoque_minimo;

consultar produtos SQL 

& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d loja_relogios -f "D:\loja_relogios\database\seed.sql"

SELECT COUNT(*) AS total_produtos
FROM produtos;

SELECT id, marca, modelo, preco, estoque
FROM produtos
ORDER BY id
LIMIT 5;

SELECT id, marca, modelo, preco, estoque
FROM produtos
ORDER BY id DESC
LIMIT 5;

INSERT INTO clientes (
    nome, cpf, data_nascimento, telefone, email,
    logradouro, numero, bairro, cidade, estado, cep
)
VALUES
('Mariana Alves Costa', '234.567.890-12', '1992-08-21', '(11) 97777-2222', 'mariana.costa@email.com', 'Rua das Palmeiras', '210', 'Moema', 'Sao Paulo', 'SP', '04530-000'),

('Rafael Henrique Souza', '345.678.901-23', '1988-03-10', '(11) 96666-3333', 'rafael.souza@email.com', 'Rua Augusta', '350', 'Consolacao', 'Sao Paulo', 'SP', '01305-000'),

('Fernanda Lima Rocha', '456.789.012-34', '1995-11-04', '(11) 95555-4444', 'fernanda.rocha@email.com', 'Rua Vergueiro', '820', 'Liberdade', 'Sao Paulo', 'SP', '01504-000'),

('Lucas Gabriel Mendes', '567.890.123-45', '1991-06-18', '(11) 94444-5555', 'lucas.mendes@email.com', 'Rua Haddock Lobo', '510', 'Cerqueira Cesar', 'Sao Paulo', 'SP', '01414-000'),

('Juliana Martins Silva', '678.901.234-56', '1993-01-27', '(11) 93333-6666', 'juliana.silva@email.com', 'Rua Oscar Freire', '430', 'Pinheiros', 'Sao Paulo', 'SP', '05409-010'),

('Bruno Almeida Santos', '789.012.345-67', '1987-09-15', '(11) 92222-7777', 'bruno.santos@email.com', 'Rua dos Pinheiros', '620', 'Pinheiros', 'Sao Paulo', 'SP', '05422-001'),

('Camila Ferreira Lima', '890.123.456-78', '1996-04-09', '(11) 91111-8888', 'camila.lima@email.com', 'Rua Joaquim Floriano', '750', 'Itaim Bibi', 'Sao Paulo', 'SP', '04534-002'),

('Diego Rodrigues Alves', '901.234.567-89', '1989-12-02', '(11) 90000-9999', 'diego.alves@email.com', 'Rua Funchal', '300', 'Vila Olimpia', 'Sao Paulo', 'SP', '04551-060'),

('Patricia Oliveira Gomes', '012.345.678-90', '1994-07-13', '(11) 98888-0000', 'patricia.gomes@email.com', 'Rua Bela Cintra', '900', 'Consolacao', 'Sao Paulo', 'SP', '01415-000');


INSERT INTO cartao_fidelidade (cliente_id, numero_cartao)
SELECT
    id,
    'KWC-' || LPAD(id::TEXT, 6, '0')
FROM clientes
WHERE id > 1;

SELECT cliente_id, numero_cartao, pontos, nivel
FROM cartao_fidelidade
ORDER BY cliente_id;

INSERT INTO cartao_fidelidade (cliente_id, numero_cartao)
SELECT
    id,
    'KWC-' || LPAD(id::TEXT, 6, '0')
FROM clientes
WHERE id > 1;

SELECT cliente_id, numero_cartao, pontos, nivel, status
FROM cartao_fidelidade
ORDER BY cliente_id;

SELECT
    c.id,
    c.nome,
    cf.numero_cartao,
    cf.pontos,
    cf.nivel
FROM clientes c
JOIN cartao_fidelidade cf
    ON cf.cliente_id = c.id
ORDER BY c.id;

INSERT INTO pedidos (
    cliente_id, subtotal, desconto, total, status, forma_pagamento
)
VALUES
(1, 699.90, 0.00, 699.90, 'Concluido', 'Cartao de Credito'),

(2, 1899.90, 189.99, 1709.91, 'Concluido', 'Pix'),

(3, 3499.90, 524.99, 2974.91, 'Concluido', 'Cartao de Credito');

SELECT
    id,
    cliente_id,
    subtotal,
    desconto,
    total,
    status,
    forma_pagamento
FROM pedidos
ORDER BY id;

SELECT id, marca, modelo, preco
FROM produtos
WHERE id IN (1, 16, 31);

SELECT id, marca, modelo, preco
FROM produtos
WHERE id IN (1, 16, 31);

SELECT id, marca, modelo, preco
FROM produtos
WHERE id IN (1, 16, 31)
ORDER BY id;

UPDATE pedidos
SET
    subtotal = 1199.90,
    desconto = 119.99,
    total = 1079.91
WHERE id = 3;

INSERT INTO itens_pedido (
    pedido_id, produto_id, quantidade, preco_unitario, subtotal
)
VALUES
(1, 1, 1, 699.90, 699.90),
(2, 16, 1, 1899.90, 1899.90),
(3, 31, 1, 1199.90, 1199.90);

SELECT
    p.id AS pedido,
    c.nome AS cliente,
    pr.marca,
    pr.modelo,
    ip.quantidade,
    ip.preco_unitario,
    p.desconto,
    p.total
FROM pedidos p
JOIN clientes c
    ON c.id = p.cliente_id
JOIN itens_pedido ip
    ON ip.pedido_id = p.id
JOIN produtos pr
    ON pr.id = ip.produto_id
ORDER BY p.id;

INSERT INTO itens_pedido (
    pedido_id,
    produto_id,
    quantidade,
    preco_unitario,
    subtotal
)
VALUES
(1, 1, 1, 699.90, 699.90),
(2, 16, 1, 1899.90, 1899.90),
(3, 31, 1, 1199.90, 1199.90);

SELECT *
FROM itens_pedido
ORDER BY pedido_id;

SELECT
    p.id AS pedido,
    c.nome AS cliente,
    pr.marca,
    pr.modelo,
    ip.quantidade,
    ip.preco_unitario,
    p.desconto,
    p.total
FROM pedidos p
JOIN clientes c
    ON c.id = p.cliente_id
JOIN itens_pedido ip
    ON ip.pedido_id = p.id
JOIN produtos pr
    ON pr.id = ip.produto_id
ORDER BY p.id;

UPDATE produtos
SET estoque = estoque - ip.quantidade
FROM itens_pedido ip
WHERE produtos.id = ip.produto_id
  AND ip.pedido_id IN (1, 2, 3);
SELECT
    id,
    marca,
    modelo,
    estoque
FROM produtos
WHERE id IN (1, 16, 31)
ORDER BY id;


SELECT
    p.id AS pedido,
    c.nome AS cliente,
    pr.marca,
    pr.modelo,
    ip.quantidade AS vendida,
    pr.estoque AS estoque_atual
FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
JOIN itens_pedido ip ON ip.pedido_id = p.id
JOIN produtos pr ON pr.id = ip.produto_id
ORDER BY p.id;


UPDATE cartao_fidelidade cf
SET pontos = COALESCE(
    (
        SELECT FLOOR(SUM(p.total) / 10)
        FROM pedidos p
        WHERE p.cliente_id = cf.cliente_id
          AND p.status = 'Concluido'
    ), 0
);