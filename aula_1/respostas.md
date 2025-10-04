# RESPOSTAS

## 1 - Pesquisa sobre SGDB

Dentre varias SGBDs no mercado, Postgres é uma das mais cosolidadas, mas quando estamos começando a estudar sobre SQL, o MYsql acaba se destacando, por possuir uma curva de aprendizado menor. Fora outas coisas
* Conformidade com ACID:
ACID é a abreviação de Atomicidade, consistência, isolamento e durabilidade. Isso são propriedades que um banco de dados precisa para garantir seu bom funcionamento e efetividade. Um banco de dados que possui uma boa ACID garante bom funcionamento em situações de erro por exemplo, onde garante que o BD não será afetado num erro de uma querry.
O MySql possui ACID, porém só em configurações espefícificas. Já o Postgres é compativel em todas as configurações existentes e disponíveis.

* Controle de simultaneidade
O Postgress possui um recurso chamado MVCC, que possibilita a modificações e leitura do banco de forma simultanea, sem comprometar o banco com conflitos. O Mysql não possui esse recurso.

* Escopo de Uso
O Postgres, por ser um SGDB mais completo que o MySql, é recomendavel o uso de forma corporativa, onde exige uma demanda alta e simultanea e consultas mais complexas.

Já o MySql, quase que o oposto. Por mais 'facil', acaba sendo bom usar em escopos menores, tanto para aprendizado, quanto para corperativas menores. Ela é muito boa iniciantes, por possuir configurações mais simples de se fazer para sua utilização.

## 2 e 3 -Script SQL Prático e Modelagem de Sistema

Para ficar algo mais pratico, eu realizei esses dois exercícios ao mesmo tempo. Criei a modelagem do Sistema em algo proximo ao Spotify, fazendo a modelagem antes e então o Script Sql.

## 5 - Reflexão Critica


## 6 - Prática com Dataset Real
```
SELECT COUNT(*)
FROM items;

-- Quantidade de itens por condição (novo/usado)
SELECT condition, COUNT(*) AS total
FROM items
GROUP BY condition;

-- Buscar os itens listados em 2024
SELECT id, title, price
FROM items
WHERE start_time >= DATE '2024-01-01'
  AND start_time < DATE '2025-01-01';

-- Buscar itens do Brasil
SELECT id, title, price
FROM items
WHERE country = 'BR';
```
