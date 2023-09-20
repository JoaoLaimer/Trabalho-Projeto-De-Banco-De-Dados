-- Retorna o nome do usuário, o título do filme, o nome do diretor e o país de produção do filme, dos filmes produzidos pelo mesmo pais do usuário 'ana'.
SELECT usuario.nomeuser, filme.titulofilme, diretor.nomediretor,filme.paisdeproducao FROM filme
JOIN diretor ON filme.id_diretor = diretor.id_diretor
JOIN usuario ON filme.paisdeproducao = usuario.paisuser
WHERE usuario.nomeuser = 'ana';