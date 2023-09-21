-- Insere ou atualiza o diretor
INSERT INTO diretor (nomediretor)
VALUES ('nomediretor')
ON CONFLICT (nomediretor) DO UPDATE SET nomediretor = 'nomediretor';

-- Insere ou atualiza o estúdio
INSERT INTO estudio (nome_estudio)
VALUES ('nome_estudio')
ON CONFLICT (nome_estudio) DO UPDATE SET nome_estudio = 'nome_estudio';

-- Insere o filme 
INSERT INTO filme (titulofilme, generofilme, duracao, classificacao, paisdeproducao, id_diretor, id_estudio, datalancamento)
VALUES ('titulofilme', 'generofilme', duracao, clasificacao, 'paisdeproducao', (SELECT id_diretor FROM diretor WHERE nomediretor = 'nomediretor'), (SELECT id_estudio FROM estudio WHERE nome_estudio = 'nome_estudio'), 'dia/mes/ano');


