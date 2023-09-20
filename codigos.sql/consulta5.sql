SELECT nomediretor AS nomediretor, 
COUNT (filme.id_filme) AS qtd_filmes_produzidos FROM diretor
JOIN filme ON diretor.id_diretor = filme.id_diretor
GROUP BY nomediretor
ORDER BY qtd_filmes_produzidos DESC
LIMIT 3