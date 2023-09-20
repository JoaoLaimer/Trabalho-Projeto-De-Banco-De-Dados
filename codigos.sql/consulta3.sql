SELECT nomeuser, filme.titulofilme, review.nota FROM usuario
JOIN review ON usuario.id_user = review.id_user
JOIN filme ON review.id_filme = filme.id_filme
JOIN diretor ON filme.id_diretor = diretor.id_diretor
WHERE diretor.nomediretor = 'David Fincher' and review.nota >= 4 
ORDER BY review.nota ASC