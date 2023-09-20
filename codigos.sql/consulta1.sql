-- Conta a quantidade de atores em cada filme
SELECT titulofilme ,COUNT(*) as qnt_de_atores FROM atua
JOIN filme ON atua.id_filme = filme.id_filme
GROUP BY titulofilme;


