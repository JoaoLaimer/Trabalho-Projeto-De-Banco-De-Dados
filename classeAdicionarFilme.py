import tkinter as tk
from conexaoBD import database
import customtkinter

class AdicionarFilmePage:
    def __init__(self, master, id_lista, id_filme, app):
        self.master = master
        self.id_lista = id_lista
        self.id_filme = id_filme
        self.app = app  
        self.app.title("Nome do App")

        db = database()

        self.busca_button = customtkinter.CTkButton(self.master, text="Busca", command=self.app.abrir_pagina_busca)
        self.busca_button.grid(row=3, column=0, padx=20, pady=10)