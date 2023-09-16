import tkinter as tk
import psycopg2
from conexaoBD import database

class FilmePage:
    def __init__(self, master, id_any, id_type):
        self.master = master
        
        self.id_any = id_any
        self.id_type = id_type

        self.master.title("Resultado da Busca")

        


    consulta_sql = "SELECT titulofilme,generofilme,datalancamento,duracao,classificacao,paisdeproducao,nomediretor,nome_estudio FROM filme JOIN diretor on filme.id_diretor = diretor.id_diretor JOIN estudio on filme.id_estudio = estudio.id_estudio WHERE if_filme = %s"