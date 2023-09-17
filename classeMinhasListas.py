import tkinter as tk
from tkinter import messagebox
from conexaoBD import database
import customtkinter

class MinhasListasPage:
    def __init__(self, master, id_user, bool, app):
        self.master = master
        self.id_user = id_user
        self.bool = bool
        self.app = app  
        self.app.title("Nome do App")
        
        db = database()
        self.user = db.return_user(self.id_user)
        self.name = self.user[3]

        username_label = tk.Label(self.app, text=f"Lista de {self.name}")
        username_label.grid(row=0, column=0, padx=10, pady=10)

        total_lists = db.check_total_user_lists(self.id_user)
        total_lists_label = tk.Label(self.app, text=f"Total de listas: {total_lists}")
        total_lists_label.grid(row=1, column=0, padx=10, pady=10)

        self.list_lists()

    def list_lists(self):
        options_logged_profile = ["Adicionar filme", "Excluir filme", "Apagar lista"]
        self.options_var = tk.StringVar(self.app)
        self.options_var.set(options_logged_profile[0])
        
        checkbox_vars = []
        rowIncrement = 2
        db = database()
        lists = db.return_user_lists(self.id_user)
        for list in lists:
            list_name = list[1]
            list_id = list[3]
            list_label = customtkinter.CTkButton(self.app, text=f"Nome: {list_name}", command=lambda: self.show_movies_in_list(list_id))
            list_label.grid(row = rowIncrement, column = 0, padx = 10, pady = 10)

            if self.bool:
                list_menu = tk.OptionMenu(self.app, self.options_var, *options_logged_profile)
                list_menu.grid(row=rowIncrement, column=1, padx=10, pady=10)
            else:
                var = tk.IntVar()
                checkbox_vars.append(var)

                checkbox = tk.Checkbutton(self.app, text="Curtir Lista", variable=var, command=lambda: self.checkbox_event(list_id, var.get()))
                checkbox.grid(row=rowIncrement, column=1, padx=10, pady=10)
            rowIncrement += 1

    def show_movies_in_list(self, id_list):
        db = database()
        movies = db.return_movies_in_list(id_list)

        movie_window = tk.Toplevel(self.app)
        movie_window.title("Filmes da Lista")

        for movie in movies:
            movie_id = movie[0]
            movie_name = db.get_movie_name(movie_id) 
            movie_label = tk.Label(movie_window, text=movie_name)
            movie_label.grid(row = rowIncrement, column = 0, padx = 10, pady = 10)
            rowIncrement += 1

    def checkbox_event(self, id_list, value):
        db = database()
        if value == 1:
            db.like_list(id_list, self.id_user)
        else:
            db.unlike_list(id_list, self.id_user)