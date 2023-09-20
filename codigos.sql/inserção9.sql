-- Insere um novo ator na tabela ator
INSERT INTO ator (nomeator) VALUES ('nomeator');

-- Insere um relacionamento entre o ator e o filme na tabela atua
INSERT INTO atua (id_ator, id_filme)
VALUES (
    (SELECT id_ator FROM ator WHERE nomeator = 'nomeautor'),
    (SELECT id_filme FROM filme WHERE titulofilme = 'titulofilme')
);