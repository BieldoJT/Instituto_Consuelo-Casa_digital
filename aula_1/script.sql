CREATE TABLE usuario (
  id          SERIAL PRIMARY KEY,
  email       VARCHAR(50) UNIQUE NOT NULL,
  username    VARCHAR(50) UNIQUE NOT NULL,
  senha       VARCHAR(50) NOT NULL
);

CREATE TABLE artista (
  id    SERIAL PRIMARY KEY,
  nome  VARCHAR(100) NOT NULL
);

CREATE TABLE genero (
  id    SERIAL PRIMARY KEY,
  nome  VARCHAR(50) NOT NULL
);

CREATE TABLE album (
  id          SERIAL PRIMARY KEY,
  titulo      VARCHAR(100) NOT NULL,
  id_artista  INT NOT NULL REFERENCES artista(id),
  id_genero   INT NOT NULL REFERENCES genero(id)
);

CREATE TABLE musica (
  id          SERIAL PRIMARY KEY,
  id_album    INT NOT NULL REFERENCES album(id),
  id_artista  INT NOT NULL REFERENCES artista(id),
  nome        VARCHAR(100) NOT NULL
);

CREATE TABLE playlist (
  id          SERIAL PRIMARY KEY,
  nome        VARCHAR(100) NOT NULL,
  id_usuario  INT NOT NULL REFERENCES usuario(id),
  id_musica   INT NOT NULL REFERENCES musica(id)
);


CREATE TABLE historico (
  id          SERIAL PRIMARY KEY,
  id_usuario  INT NOT NULL REFERENCES usuario(id),
  id_musica   INT NOT NULL REFERENCES musica(id),
  data        DATE NOT NULL,
  hora        TIME NOT NULL
);

-- === Inserts (IDs explícitos) ===
INSERT INTO usuario (id, email, username, senha) VALUES
(1, 'guilherme@gmail.com', 'gui123', 'senha123'),
(2, 'sara@gmail.com', 'sara456', 'senha456'),
(3, 'joao@gmail.com', 'joao789', 'senha789'),
(4, 'carlos@gmail.com', 'carlos123', 'senha123'),
(5, 'maria@gmail.com', 'maria456', 'senha456');

INSERT INTO genero (id, nome) VALUES
(1, 'Pop'),
(2, 'Rock'),
(3, 'Jazz'),
(4, 'Classica'),
(5, 'Hip-Hop');

INSERT INTO artista (id, nome) VALUES
(1, 'The Weeknd'),
(2, 'BK'''),
(3, 'AnaVitoria'),
(4, 'SlipKnot'),
(5, 'Bruno Mars')
(6, 'Adele'),
(7, 'Coldplay'),
(8, 'Chico Buarque'),
(9, 'Miles Davis'),
(10, 'Bach');

-- Corrigido: album tem (titulo, id_artista, id_genero)
INSERT INTO album (id, titulo, id_artista, id_genero) VALUES
(1, 'After Hours', 1, 1),
(2, 'Ouro', 2, 5),
(3, 'AnaVitoria', 3, 1),
(4, 'Iowa', 4, 2),
(5, '24K Magic', 5, 5)
(6, '21', 6, 1),
(7, 'Parachutes', 7, 2),
(8, 'Construção', 8, 5),
(9, 'Kind of Blue', 9, 3),
(10, 'Brandenburg Concerto', 10, 4);

INSERT INTO musica (id, id_album, id_artista, nome) VALUES
(1, 1, 1, 'Blinding Lights'),
(2, 2, 2, 'Me Deixa Em Paz'),
(3, 3, 3, 'Trevo (Tu)'),
(4, 4, 4, 'Duality'),
(5, 5, 5, '24K Magic')
(6, 6, 6, 'Rolling in the Deep'),
(7, 7, 7, 'Yellow'),
(8, 7, 7, 'Trouble'),
(9, 8, 8, 'Construção'),
(10, 9, 9, 'So What'),
(11, 10, 10, 'Concerto No. 3'),
(12, 6, 6, 'Someone Like You'),
(13, 9, 9, 'Freddie Freeloader');

INSERT INTO playlist (id, nome, id_usuario, id_musica) VALUES
(1, 'Favoritas', 1, 1),
(2, 'Rock', 2, 4),
(3, 'Pop', 3, 5),
(4, 'Jazz', 4, 3),
(5, 'Hip-Hop', 5, 2);

INSERT INTO historico (id, id_usuario, id_musica, data, hora) VALUES
(1, 1, 1, '2023-10-01', '10:00:00'),
(2, 2, 4, '2023-10-02', '11:00:00'),
(3, 3, 5, '2023-10-03', '12:00:00'),
(4, 4, 3, '2023-10-04', '13:00:00'),
(5, 5, 2, '2023-10-05', '14:00:00')
(6, 6, 12, '2023-10-06', '15:00:00'),
(7, 7, 11, '2023-10-07', '16:30:00'),
(8, 8, 10, '2023-10-08', '18:00:00'),
(9, 9, 6, '2023-10-09', '20:15:00'),
(10, 10, 7, '2023-10-10', '21:00:00'),
(11, 6, 13, '2023-10-11', '10:00:00'),
(12, 8, 9, '2023-10-12', '09:30:00');


INSERT INTO album (id, titulo, id_artista, id_genero) VALUES
(6, '21', 6, 1),
(7, 'Parachutes', 7, 2),
(8, 'Construção', 8, 5),
(9, 'Kind of Blue', 9, 3),
(10, 'Brandenburg Concerto', 10, 4);

/*Saber quantos albuns são de rock*/
SELECT COUNT(*) FROM album WHERE id_genero=2;

/*Saber quais musicas são do artista BK'*/
SELECT * FROM musica WHERE id_artista=2;

/*Saber quais playlists são do usuario de id 1*/
SELECT * FROM playlist WHERE id_usuario=1;

/*query usando oder by*/
/*Saber quantas musicas cada artista tem*/
SELECT id_artista, COUNT(*) AS total_musicas FROM musica GROUP BY id_artista ORDER BY id_artista;

/*query usando join*/
/*Saber o nome do artista de cada musica*/
SELECT musica.nome AS nome_musica, artista.nome AS nome_artista
FROM musica
JOIN artista ON musica.id_artista = artista.id;






