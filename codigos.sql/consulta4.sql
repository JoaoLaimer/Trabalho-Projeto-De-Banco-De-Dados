-- Retorna o nome do diretor que produziram algum filme pelo estudio 'Warner', ordenados pelo nome do diretor em ordem decrescente.
SELECT diretor.nomediretor FROM diretor
JOIN filme ON diretor.id_diretor = filme.id_diretor
JOIN estudio ON filme.id_estudio = estudio.id_estudio
WHERE estudio.nome_estudio = 'Warner'
ORDER BY diretor.nomediretor DESC;