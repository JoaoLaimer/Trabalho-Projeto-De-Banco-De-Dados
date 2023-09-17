import tkinter as tk
from tkinter import messagebox
from conexaoBD import database
import customtkinter
from classeAdicionarFilme import AdicionarFilmePage

class MinhasListasPage:
    def __init__(self, master, id_user, bool, app):
        self.master = master
        self.id_user = id_user
        self.bool = bool
        self.app = app  
        self.app.title("Nome do App")
        self.like_button = None
        self.unlike_button = None
        db = database()
        self.user = db.return_user(self.id_user)
        self.name = self.user[3]

        username_label = tk.Label(self.app, text=f"Lista de {self.name}")
        username_label.grid(row=0, column=0, padx=10, pady=10)

        total_lists = db.check_total_user_lists(self.id_user)
        total_lists_label = tk.Label(self.app, text=f"Total de listas: {total_lists[0]}")
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
        liked_lists = db.return_liked_lists(self.id_user)

        for likes in liked_lists:
            for item in likes:
                print(item)
            
        for list in lists:
            list_name = list[1]
            list_id = list[3]
            list_label = customtkinter.CTkButton(self.app, text=f"Nome: {list_name}", command=lambda: self.show_movies_in_list(list_id))
            list_label.grid(row = rowIncrement, column = 0, padx = 10, pady = 10)
            
            if self.bool:
                list_menu= tk.OptionMenu(self.app, self.options_var, *options_logged_profile)
                list_menu.grid(row=rowIncrement, column=1, padx=10, pady=10)
            else:
                if not db.check_like(list_id, self.id_user):
                    like_button = customtkinter.CTkButton(self.app, text="Curtir", command=lambda list_id = list_id: self.like_event(list_id))
                    like_button.grid(row=rowIncrement, column=2, padx=10, pady=10)
                else:
                    unlike_button = customtkinter.CTkButton(self.app, text="Descurtir", command=lambda list_id = list_id: self.unlike_event(list_id))
                    unlike_button.grid(row=rowIncrement, column=2, padx=10, pady=10)
            rowIncrement += 1

    def like_event(self, id_list):
        db = database()
        db.like_list(id_list, self.id_user)
        self.update_like_button(id_list, liked=True)

    def unlike_event(self, id_list):
        db = database()
        db.unlike_list(id_list, self.id_user)
        self.update_like_button(id_list, liked=False)

    def update_like_button(self, id_list, liked):
        if liked:
            button_text = "Descurtir"
            command = lambda id_list=id_list: self.unlike_event(id_list)
        else:
            button_text = "Curtir"
            command = lambda id_list=id_list: self.like_event(id_list)

        if not self.like_button:
            self.like_button = customtkinter.CTkButton(self.app, text=button_text, command=command)
        else:
            self.like_button.configure(text=button_text, command=command)

        self.like_button.configure(text=button_text, command=command)

        # Force a redraw of the button
        self.like_button.update_idletasks()
         
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