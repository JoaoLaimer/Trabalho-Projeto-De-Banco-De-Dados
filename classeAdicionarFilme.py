import tkinter as tk
from conexaoBD import database

class AdicionarFilmePage:
    def __init__(self, master, id_lista, id_filme, app):
        self.master = master
        self.id_lista = id_lista
        self.id_filme = id_filme
        self.app = app  
        self.app.title("Nome do App")

        db = database()