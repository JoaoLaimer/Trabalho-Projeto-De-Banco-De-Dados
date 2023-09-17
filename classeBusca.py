import tkinter as tk
import customtkinter
from conexaoBD import database
from classeMeuPerfil import MeuPerfilPage
from classeFilme import FilmePage
import customtkinter as ctk
from tkinter import messagebox

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


class BuscaPage:
    def __init__(self, master, app, user_id_logged):
        self.master = master
        self.app = app
        self.master.geometry("320x400")
        self.app.title("Busca")
        self.user_id_logged = user_id_logged
        self.search_value = None
        self.search_type = None

        opcoes = ["Ator", "Diretor", "Filme", "Gênero", "Ano", "Usuário"]

        self.opcoes_var = ctk.StringVar(value=opcoes[0])
        

        option_menu = ctk.CTkOptionMenu(app,
                                        values=opcoes,
                                        variable=self.opcoes_var,
                                        width=100,
                                        corner_radius=5,
                                        text_color=("black", "white"),
                                        dropdown_text_color=("black", "white"),
                                        font=("Arial", 12))
        option_menu.pack(padx=10, pady=10)

        self.busca_entry = ctk.CTkEntry(app, width=100)
        self.busca_entry.pack(padx=10, pady=10)

        busca_button = ctk.CTkButton(app, text="Buscar", command=self.set_entry_menu)
        busca_button.pack(padx=10, pady=10)

    def set_entry_menu(self):
        self.search_value = self.busca_entry.get()
        self.search_type = self.opcoes_var.get()
        db = database()
        resultado = db.return_search(self.search_type, self.search_value)
        if resultado:
            print("ok")
            if self.search_type == "Usuário":
                self.app.withdraw()
                self.master.abrir_pagina_perfil(resultado[0][0])
            else:
                self.app.withdraw()


                self.abrir_pagina_filme(resultado[0][0],self.search_type)

        else:
            messagebox.showerror("Nome do App", "Não encontrado")
        db.connection.close()

    def abrir_pagina_filme(self, id_any, id_type):
        filme_window = tk.Toplevel(self.app)

        filme_page = FilmePage(filme_window, self ,id_any, id_type)

    def get_search_value(self):
        return self.search_value
        

