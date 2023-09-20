SELECT diretor.nomediretor FROM diretor
JOIN filme ON diretor.id_diretor = filme.id_diretor
JOIN estudio ON filme.id_estudio = estudio.id_estudio
WHERE estudio.nome_estudio = 'Warner'
ORDER BY diretor.nomediretor DESC;