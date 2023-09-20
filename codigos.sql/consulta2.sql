-- Retorna o título do filme, o nome do usuário e a maior nota atribuída a cada filme
SELECT filme.titulofilme, usuario.nomeuser, max_review.nota AS maior_nota
FROM filme
JOIN (
    SELECT id_filme, MAX(nota) AS nota
    FROM review
    GROUP BY id_filme
) AS max_review ON filme.id_filme = max_review.id_filme
JOIN review ON max_review.id_filme = review.id_filme AND max_review.nota = review.nota
JOIN usuario ON review.id_user = usuario.id_user
ORDER BY titulofilme ASC, nomeuser ASC;
