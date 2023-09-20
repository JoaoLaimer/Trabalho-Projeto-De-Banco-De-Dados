INSERT INTO review (id_filme, id_user, nota, texto_review)
VALUES (id_filme, id_user, nota, texto_review)
ON CONFLICT (id_filme, id_user)

-- Se a revisão já existe (atualização)
DO UPDATE review
SET nota = nota, texto_review = texto_review
WHERE id_filme = id_filme AND id_user = id_user;