-- ============================================================
-- KAIROS WATCH CO.
-- SEED DE PRODUTOS
-- 100 produtos para ambiente de desenvolvimento
-- ============================================================

-- ATENÇÃO:
-- Este comando apaga os produtos atuais.
-- Como estamos na fase inicial do projeto, isso facilita
-- manter um catálogo limpo e reproduzível.

TRUNCATE TABLE produtos RESTART IDENTITY CASCADE;


-- ============================================================
-- PRODUTOS
-- ============================================================

INSERT INTO produtos (
    marca,
    modelo,
    referencia,
    categoria,
    descricao,
    preco,
    custo,
    estoque,
    estoque_minimo
)
VALUES

-- ============================================================
-- CASIO
-- ============================================================

('Casio', 'G-Shock GA-2100', 'GA-2100-1A1', 'Esportivo',
 'Relogio analogico e digital resistente para uso esportivo.',
 699.90, 400.00, 10, 2),

('Casio', 'G-Shock DW-5600', 'DW-5600E-1', 'Esportivo',
 'Relogio digital resistente com visual classico G-Shock.',
 549.90, 310.00, 12, 3),

('Casio', 'G-Shock GA-B2100', 'GA-B2100-1A1', 'Esportivo',
 'Relogio analogico e digital com conectividade.',
 999.90, 580.00, 8, 2),

('Casio', 'Edifice EFR-S108D', 'EFR-S108D-1AV', 'Casual',
 'Relogio analogico esportivo com caixa fina.',
 899.90, 500.00, 9, 2),

('Casio', 'Edifice EFR-556', 'EFR-556DB-1AV', 'Esportivo',
 'Cronografo analogico para uso cotidiano.',
 799.90, 450.00, 7, 2),

('Casio', 'MTP-V002', 'MTP-V002D-1B3', 'Social',
 'Relogio analogico simples para uso social.',
 249.90, 130.00, 15, 3),

('Casio', 'MTP-1302D', 'MTP-1302D-7A1', 'Social',
 'Relogio analogico com pulseira de aco.',
 349.90, 190.00, 11, 2),

('Casio', 'Vintage A168', 'A168WA-1YES', 'Casual',
 'Relogio digital retro com pulseira metalica.',
 299.90, 160.00, 14, 3),

('Casio', 'Vintage F-91W', 'F-91W-1', 'Casual',
 'Relogio digital compacto e classico.',
 129.90, 65.00, 20, 4),

('Casio', 'Pro Trek PRG-340', 'PRG-340-3', 'Esportivo',
 'Relogio esportivo voltado para atividades ao ar livre.',
 1699.90, 980.00, 5, 1),

('Casio', 'G-Shock GA-700', 'GA-700-1A', 'Esportivo',
 'Relogio esportivo analogico e digital de grande porte.',
 899.90, 520.00, 7, 2),

('Casio', 'G-Shock GA-100', 'GA-100-1A1', 'Esportivo',
 'Modelo esportivo resistente com mostrador analogico digital.',
 799.90, 460.00, 9, 2),

('Casio', 'G-Shock GBD-200', 'GBD-200-1', 'Esportivo',
 'Relogio digital esportivo com recursos para treinamento.',
 1199.90, 700.00, 6, 2),

('Casio', 'Lineage LCW-M100', 'LCW-M100TSE', 'Social',
 'Relogio analogico e digital com acabamento metalico.',
 1399.90, 800.00, 4, 1),

('Casio', 'MTP-VD01', 'MTP-VD01D-1EV', 'Casual',
 'Relogio analogico masculino para uso diario.',
 299.90, 160.00, 12, 3),


-- ============================================================
-- SEIKO
-- ============================================================

('Seiko', '5 Sports', 'SRPD55K1', 'Automatico',
 'Relogio automatico esportivo da linha Seiko 5.',
 1899.90, 1100.00, 8, 2),

('Seiko', '5 Sports Field', 'SRPG27K1', 'Automatico',
 'Relogio automatico com estilo militar.',
 1999.90, 1150.00, 5, 1),

('Seiko', 'Presage Cocktail Time', 'SRPB43J1', 'Social',
 'Relogio automatico elegante para ocasioes sociais.',
 2999.90, 1800.00, 4, 1),

('Seiko', 'Presage Style 60s', 'SRPG27J1', 'Social',
 'Modelo automatico inspirado em design vintage.',
 2899.90, 1700.00, 3, 1),

('Seiko', 'Prospex Diver', 'SRPE93K1', 'Mergulho',
 'Relogio automatico esportivo para mergulho.',
 4599.90, 2800.00, 3, 1),

('Seiko', '5 Sports GMT', 'SSK001K1', 'Automatico',
 'Relogio automatico com funcao GMT.',
 2999.90, 1800.00, 4, 1),

('Seiko', 'Quartz Classic', 'SUR309P1', 'Social',
 'Relogio analogico classico para uso diario.',
 1199.90, 680.00, 7, 2),

('Seiko', 'Neo Classic', 'SUR311P1', 'Social',
 'Relogio analogico elegante com acabamento metalico.',
 1299.90, 750.00, 6, 2),

('Seiko', 'Chronograph', 'SSB425P1', 'Cronografo',
 'Relogio cronografo esportivo.',
 1799.90, 1050.00, 5, 1),

('Seiko', 'Presage Automatic', 'SRPB41J1', 'Automatico',
 'Relogio automatico com mostrador inspirado em coqueteis.',
 3299.90, 1950.00, 3, 1),


-- ============================================================
-- ORIENT
-- ============================================================

('Orient', 'Bambino', 'RA-AC0M04Y10B', 'Social',
 'Relogio automatico classico da linha Bambino.',
 1299.90, 750.00, 6, 2),

('Orient', 'Bambino Version 2', 'FAC00009N0', 'Social',
 'Relogio automatico com visual classico.',
 1399.90, 800.00, 5, 1),

('Orient', 'Kamasu', 'RA-AA0003R19B', 'Mergulho',
 'Relogio automatico esportivo inspirado em mergulho.',
 2199.90, 1300.00, 5, 1),

('Orient', 'Mako III', 'RA-AA0004E19B', 'Mergulho',
 'Relogio automatico esportivo para uso aquatico.',
 1999.90, 1150.00, 6, 2),

('Orient', 'Sun and Moon', 'RA-AS0102S10B', 'Social',
 'Relogio automatico com indicador de dia e noite.',
 2499.90, 1450.00, 3, 1),

('Orient', 'Classic', 'RA-AC0E01S10B', 'Social',
 'Relogio automatico de estilo tradicional.',
 1199.90, 680.00, 7, 2),

('Orient', 'Maestro', 'RA-AC0E03B10B', 'Social',
 'Relogio automatico elegante para ocasioes formais.',
 1599.90, 900.00, 5, 1),

('Orient', 'Bambino Small Seconds', 'RA-AP0003S10B', 'Social',
 'Relogio automatico com pequeno mostrador de segundos.',
 1799.90, 1050.00, 4, 1),

('Orient', 'Diver', 'RA-AA0810N19B', 'Mergulho',
 'Relogio automatico esportivo.',
 2299.90, 1350.00, 4, 1),

('Orient', 'Three Star', 'RA-AB0F08L19B', 'Automatico',
 'Relogio automatico tradicional.',
 1099.90, 620.00, 8, 2),


-- ============================================================
-- CITIZEN
-- ============================================================

('Citizen', 'Eco-Drive', 'BM8478-01L', 'Casual',
 'Relogio com tecnologia Eco-Drive e mostrador analogico.',
 999.90, 600.00, 7, 2),

('Citizen', 'Tsuyosa', 'NJ0150-81E', 'Automatico',
 'Relogio automatico com design esportivo integrado.',
 2199.90, 1300.00, 5, 1),

('Citizen', 'Promaster Diver', 'BN0150-28E', 'Mergulho',
 'Relogio Eco-Drive para atividades aquaticas.',
 1799.90, 1050.00, 6, 2),

('Citizen', 'Promaster Land', 'BN4044-15E', 'Esportivo',
 'Relogio esportivo para atividades ao ar livre.',
 2499.90, 1450.00, 4, 1),

('Citizen', 'Eco-Drive Chronograph', 'CA0649-06X', 'Cronografo',
 'Cronografo Eco-Drive com visual esportivo.',
 1599.90, 920.00, 5, 1),

('Citizen', 'Classic', 'BI5000-01A', 'Social',
 'Relogio analogico classico de uso diario.',
 699.90, 400.00, 10, 2),

('Citizen', 'Quartz Classic', 'BF5002-05A', 'Social',
 'Relogio analogico tradicional.',
 599.90, 330.00, 9, 2),

('Citizen', 'Automatic', 'NH8350-83E', 'Automatico',
 'Relogio automatico com acabamento metalico.',
 1399.90, 800.00, 6, 2),

('Citizen', 'Promaster Sky', 'CB5001-57E', 'Aviação',
 'Relogio Eco-Drive cronografo inspirado em aviacao.',
 3499.90, 2100.00, 3, 1),

('Citizen', 'Series 8', 'NB6010-81E', 'Automatico',
 'Relogio automatico contemporaneo.',
 3999.90, 2400.00, 3, 1),


-- ============================================================
-- TISSOT
-- ============================================================

('Tissot', 'PRX', 'T137.410.11.041.00', 'Social',
 'Relogio quartz com design integrado.',
 3499.90, 2200.00, 4, 1),

('Tissot', 'PRX Powermatic 80', 'T137.407.11.041.00', 'Automatico',
 'Relogio automatico da linha PRX.',
 4999.90, 3000.00, 3, 1),

('Tissot', 'Seastar 1000', 'T120.407.11.051.03', 'Mergulho',
 'Relogio automatico esportivo para mergulho.',
 4999.90, 3000.00, 2, 1),

('Tissot', 'Le Locle', 'T006.407.11.033.00', 'Social',
 'Relogio automatico de estilo tradicional.',
 3999.90, 2400.00, 3, 1),

('Tissot', 'Gentleman', 'T127.410.11.041.00', 'Social',
 'Relogio quartz elegante para uso diario.',
 2999.90, 1800.00, 4, 1),

('Tissot', 'Chrono XL', 'T116.617.11.047.01', 'Cronografo',
 'Cronografo esportivo de grande porte.',
 2499.90, 1450.00, 5, 1),

('Tissot', 'Carson Premium', 'T122.410.11.033.00', 'Social',
 'Relogio classico para ocasioes formais.',
 2799.90, 1650.00, 3, 1),

('Tissot', 'PR 100', 'T101.610.11.041.00', 'Casual',
 'Relogio quartz versatil.',
 2299.90, 1350.00, 5, 1),


-- ============================================================
-- TECHNOS
-- ============================================================

('Technos', 'Executive', 'GM10AA', 'Social',
 'Relogio analogico elegante para uso profissional.',
 699.90, 390.00, 8, 2),

('Technos', 'Skydiver', 'OS10AA', 'Esportivo',
 'Relogio esportivo com cronografo.',
 899.90, 500.00, 7, 2),

('Technos', 'Performance', '2115KLA', 'Casual',
 'Relogio casual com acabamento metalico.',
 599.90, 330.00, 10, 2),

('Technos', 'Classic', '2115NDA', 'Social',
 'Relogio classico para uso cotidiano.',
 499.90, 270.00, 12, 3),

('Technos', 'Connect', 'JS15AA', 'Esportivo',
 'Relogio de visual esportivo contemporaneo.',
 799.90, 450.00, 6, 2),

('Technos', 'Diver', 'T205AA', 'Mergulho',
 'Relogio esportivo inspirado em mergulho.',
 999.90, 580.00, 5, 1),

('Technos', 'Automatic', '2115RAB', 'Automatico',
 'Relogio automatico de estilo classico.',
 1299.90, 750.00, 4, 1),

('Technos', 'Carbon', 'JS25AA', 'Esportivo',
 'Relogio esportivo com visual moderno.',
 899.90, 500.00, 8, 2),


-- ============================================================
-- TIMEX
-- ============================================================

('Timex', 'Weekender', 'T2N651', 'Casual',
 'Relogio casual de visual simples.',
 499.90, 280.00, 10, 2),

('Timex', 'Expedition Scout', 'TW4B04700', 'Esportivo',
 'Relogio esportivo inspirado em aventura.',
 599.90, 340.00, 8, 2),

('Timex', 'Marlin Automatic', 'TW2V44600', 'Automatico',
 'Relogio automatico de estilo vintage.',
 2199.90, 1300.00, 4, 1),

('Timex', 'Q Timex', 'TW2U61100', 'Casual',
 'Relogio inspirado nos modelos vintage.',
 999.90, 570.00, 6, 2),

('Timex', 'Waterbury', 'TW2V49700', 'Social',
 'Relogio classico com visual tradicional.',
 899.90, 510.00, 7, 2),

('Timex', 'Ironman', 'T5K195', 'Esportivo',
 'Relogio digital voltado para atividades esportivas.',
 699.90, 390.00, 8, 2),

('Timex', 'Harborside', 'TW2V25500', 'Casual',
 'Relogio casual com visual maritimo.',
 799.90, 450.00, 6, 2),

('Timex', 'Standard', 'TW2V71400', 'Casual',
 'Relogio analogico de uso diario.',
 649.90, 360.00, 9, 2),


-- ============================================================
-- BULOVA
-- ============================================================

('Bulova', 'Classic Surveyor', '96A275', 'Social',
 'Relogio automatico elegante.',
 2299.90, 1350.00, 4, 1),

('Bulova', 'Marine Star', '98A272', 'Esportivo',
 'Relogio esportivo com cronografo.',
 1999.90, 1150.00, 5, 1),

('Bulova', 'Lunar Pilot', '96B258', 'Cronografo',
 'Cronografo inspirado em modelos espaciais.',
 4999.90, 3000.00, 2, 1),

('Bulova', 'Wilton', '96A206', 'Social',
 'Relogio automatico de estilo classico.',
 2499.90, 1450.00, 3, 1),

('Bulova', 'Hack Watch', '98A255', 'Militar',
 'Relogio inspirado em modelos militares.',
 1899.90, 1100.00, 4, 1),

('Bulova', 'Sutton', '96A208', 'Social',
 'Relogio elegante para ocasioes formais.',
 2399.90, 1400.00, 3, 1),


-- ============================================================
-- HAMILTON
-- ============================================================

('Hamilton', 'Khaki Field', 'H70455553', 'Militar',
 'Relogio automatico inspirado em modelos militares.',
 4999.90, 3000.00, 3, 1),

('Hamilton', 'Khaki Aviation', 'H64615135', 'Aviação',
 'Relogio esportivo inspirado em aviacao.',
 5999.90, 3600.00, 2, 1),

('Hamilton', 'Jazzmaster', 'H32505131', 'Social',
 'Relogio automatico elegante.',
 5499.90, 3300.00, 3, 1),

('Hamilton', 'Khaki Navy', 'H82315131', 'Mergulho',
 'Relogio esportivo para atividades aquaticas.',
 5299.90, 3150.00, 2, 1),


-- ============================================================
-- LONGINES
-- ============================================================

('Longines', 'Conquest', 'L3.776.4.58.6', 'Esportivo',
 'Relogio automatico esportivo de acabamento premium.',
 8999.90, 5400.00, 2, 1),

('Longines', 'HydroConquest', 'L3.781.4.56.6', 'Mergulho',
 'Relogio automatico esportivo para mergulho.',
 9999.90, 6000.00, 2, 1),

('Longines', 'Master Collection', 'L2.893.4.78.3', 'Social',
 'Relogio automatico de estilo classico.',
 11999.90, 7200.00, 1, 1),

('Longines', 'Spirit', 'L3.810.4.53.6', 'Aviação',
 'Relogio automatico inspirado na aviacao.',
 10999.90, 6600.00, 2, 1),


-- ============================================================
-- RAYMOND WEIL
-- ============================================================

('Raymond Weil', 'Freelancer', '2760-STC-20001', 'Social',
 'Relogio automatico de estilo contemporaneo.',
 8999.90, 5400.00, 2, 1),

('Raymond Weil', 'Maestro', '2239-ST-00659', 'Social',
 'Relogio automatico elegante.',
 7999.90, 4800.00, 2, 1),

('Raymond Weil', 'Toccata', '5485-ST-50081', 'Social',
 'Relogio classico para ocasioes formais.',
 4999.90, 3000.00, 3, 1),


-- ============================================================
-- BULGARI / TAG HEUER / MODELOS PREMIUM
-- ============================================================

('TAG Heuer', 'Formula 1', 'WAZ1110.BA0875', 'Esportivo',
 'Relogio esportivo quartz com cronografo.',
 9999.90, 6000.00, 2, 1),

('TAG Heuer', 'Aquaracer', 'WBP201A.BA0632', 'Mergulho',
 'Relogio esportivo automatico para mergulho.',
 17999.90, 10800.00, 1, 1),

('TAG Heuer', 'Carrera', 'WBN2110.BA0639', 'Cronografo',
 'Relogio esportivo elegante da linha Carrera.',
 15999.90, 9600.00, 2, 1),

('Bvlgari', 'Octo', '103481', 'Social',
 'Relogio premium com design contemporaneo.',
 29999.90, 18000.00, 1, 1),

('Bvlgari', 'Diagono', '102222', 'Esportivo',
 'Relogio premium esportivo.',
 24999.90, 15000.00, 1, 1),


-- ============================================================
-- PRODUTOS ADICIONAIS
-- ============================================================

('Casio', 'G-Shock Mudmaster', 'GG-1000-1A3', 'Esportivo',
 'Relogio resistente para ambientes extremos.',
 1399.90, 800.00, 5, 1),

('Casio', 'G-Shock Frogman', 'GWF-1000', 'Mergulho',
 'Relogio digital profissional para mergulho.',
 2999.90, 1750.00, 2, 1),

('Seiko', 'Prospex Samurai', 'SRPF03K1', 'Mergulho',
 'Relogio automatico esportivo para mergulho.',
 3999.90, 2400.00, 3, 1),

('Seiko', 'Presage Sharp Edged', 'SPB203J1', 'Social',
 'Relogio automatico premium de visual contemporaneo.',
 5499.90, 3300.00, 2, 1),

('Orient', 'Star Classic', 'RE-AU0004B00B', 'Automatico',
 'Relogio automatico premium.',
 3499.90, 2100.00, 3, 1),

('Citizen', 'Series 8 Automatic', 'NB6060-58L', 'Automatico',
 'Relogio automatico premium.',
 5999.90, 3600.00, 2, 1),

('Tissot', 'Supersport Chrono', 'T125.617.11.051.03', 'Cronografo',
 'Cronografo esportivo de alta performance.',
 3299.90, 1950.00, 4, 1),

('Hamilton', 'Khaki King', 'H64455533', 'Militar',
 'Relogio automatico inspirado em modelos militares.',
 4599.90, 2750.00, 3, 1),

('Longines', 'Conquest Classic', 'L2.386.4.76.6', 'Social',
 'Relogio automatico elegante.',
 9499.90, 5700.00, 2, 1),

('Technos', 'Skymaster', 'T2055AB', 'Aviação',
 'Relogio esportivo inspirado em aviacao.',
 1099.90, 620.00, 5, 1),

('Timex', 'Expedition North', 'TW2V64400', 'Esportivo',
 'Relogio para atividades ao ar livre.',
 1299.90, 740.00, 6, 2),

('Bulova', 'Precisionist', '98B228', 'Cronografo',
 'Relogio quartz de alta precisao.',
 2799.90, 1650.00, 4, 1),

('TAG Heuer', 'Aquaracer Professional', 'WBP5110.BA0013', 'Mergulho',
 'Relogio premium esportivo para mergulho.',
 19999.90, 12000.00, 1, 1),

('Casio', 'G-Shock GA-900', 'GA-900-1A', 'Esportivo',
 'Relogio resistente com visual industrial.',
 999.90, 570.00, 8, 2),

('Seiko', '5 Sports GMT Orange', 'SSK005K1', 'Automatico',
 'Relogio automatico GMT esportivo.',
 3199.90, 1900.00, 3, 1),

('Orient', 'Kamasu Blue', 'RA-AA0002L19B', 'Mergulho',
 'Relogio automatico esportivo com mostrador azul.',
 2199.90, 1300.00, 5, 1),

('Citizen', 'Eco-Drive AW1236', 'AW1236-03A', 'Casual',
 'Relogio Eco-Drive de uso diario.',
 899.90, 510.00, 8, 2),

('Tissot', 'Everytime', 'T109.610.11.031.00', 'Social',
 'Relogio quartz minimalista.',
 1599.90, 920.00, 6, 2),

('Technos', 'Racer', 'JS10AA', 'Esportivo',
 'Relogio esportivo com cronografo.',
 799.90, 450.00, 7, 2),

('Timex', 'Waterbury Traditional', 'TW2W14800', 'Social',
 'Relogio analogico classico.',
 899.90, 510.00, 7, 2),

('Bulova', 'Classic Automatic', '96A187', 'Automatico',
 'Relogio automatico classico.',
 2499.90, 1450.00, 4, 1);


-- ============================================================
-- VERIFICACAO
-- ============================================================

SELECT COUNT(*) AS total_produtos
FROM produtos;

SELECT
    id,
    marca,
    modelo,
    preco,
    custo,
    estoque,
    estoque_minimo,
    disponivel
FROM produtos
ORDER BY id;