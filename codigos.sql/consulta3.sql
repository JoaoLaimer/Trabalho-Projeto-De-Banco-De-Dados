-- Retorna os reviews do usuário, o título do filme e a nota do review, dos filmes do diretor 'X'com nota maior ou igual a 4, ordenados pela nota do review em ordem crescente.
SELECT nomeuser, filme.titulofilme, review.nota FROM usuario
JOIN review ON usuario.id_user = review.id_user
JOIN filme ON review.id_filme = filme.id_filme
JOIN diretor ON filme.id_diretor = diretor.id_diretor
WHERE diretor.nomediretor = 'nomediretor' and review.nota >= 4 
ORDER BY review.nota ASC