import tkinter as tk
from tkinter import messagebox
from conexaoBD import database
import customtkinter
from classeAdicionarFilme import AdicionarFilmePage
from tkinter import messagebox

class MinhasListasPage:
    def __init__(self, master, id_user, bool, app):
        self.master = master
        self.id_user = id_user
        self.bool = bool
        self.app = app 
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
        
        try:
            self.id_filme = self.master.get_id_filme()
        except:
            self.id_filme = None
        print(self.id_filme)
        self.list_lists()

    def list_lists(self):
        
        db = database()
        lists = db.return_user_lists(self.id_user)
        self.like_button = [None for _ in range(len(lists))]

        for i in range(len(lists)):
            list_name = lists[i][1]
            #list_id = lists[i][3]
            self.list_id = lists[i][3]
            list_label = [None for _ in range(len(lists))]

            if self.id_filme != None:
                list_label[i] = customtkinter.CTkButton(self.app, text=f"Nome: {list_name}", command=lambda list_id = self.list_id: self.add_movie_to_list(self.id_filme,list_id))
                list_label[i].grid(row = i, column = 0, padx = 10, pady = 10) 
            else:
                if self.bool:
                    list_label[i] = customtkinter.CTkButton(self.app, text=f"Nome: {list_name}", command=lambda list_id = self.list_id: self.show_movies_in_list(list_id, bool))
                    list_label[i].grid(row = i, column = 0, padx = 10, pady = 10)
                    """self.remove_button = customtkinter.CTkButton(self.app, text="Remover", command=lambda list_id = self.list_id: self.remove_movie(list_id))
                    self.remove_button.grid(row=i, column=1, padx=10, pady=10)
                    self.delete_list_button = customtkinter.CTkButton(self.app, text="Apagar lista", command=lambda list_id = self.list_id: self.delete_list(list_id))
                    self.delete_list_button.grid(row=i, column=2, padx=10, pady=10)"""
                else:
                    list_label[i] = customtkinter.CTkButton(self.app, text=f"Nome: {list_name}", command=lambda list_id = self.list_id: self.show_movies_in_list(list_id))
                    list_label[i].grid(row = i, column = 0, padx = 10, pady = 10)
                    if not db.check_like(self.list_id, self.id_user):
                        self.like_button[i] = customtkinter.CTkButton(self.app, text="Curtir", command=lambda list_id = self.list_id, row = i: self.like_event(list_id,row))
                        self.like_button[i].grid(row=i, column=2, padx=10, pady=10)
                    else:
                        self.like_button[i] = customtkinter.CTkButton(self.app, text="Descurtir", command=lambda list_id = self.list_id, row = i: self.unlike_event(list_id,row))
                        self.like_button[i].grid(row=i, column=2, padx=10, pady=10)

    def like_event(self, id_list,pos):
        db = database()
        db.like_list(id_list, self.id_user)
        self.like_button[pos].grid_remove()
        self.like_button[pos] = customtkinter.CTkButton(self.app, text="Descurtir", command=lambda list_id = id_list, row=pos: self.unlike_event(list_id,row))
        self.like_button[pos].grid(row=pos, column=2, padx=10, pady=10)
         
    def unlike_event(self, id_list,pos):
        db = database()
        db.unlike_list(id_list, self.id_user)
        self.like_button[pos].grid_remove()
        self.like_button[pos] = customtkinter.CTkButton(self.app, text="Curtir", command=lambda list_id = id_list, row=pos: self.like_event(list_id,row))
        self.like_button[pos].grid(row=pos, column=2, padx=10, pady=10)
            
    def show_movies_in_list(self, id_list, bool):
        db = database()
        movies = db.return_movies_in_list(id_list)

        movie_window = tk.Toplevel(self.app)
        movie_window.title("Filmes da Lista")

        print(movies)
        """for i in range(len(movies)):
            movie_id = movies[i][0]
            movie_title = db.get_movie_name(movie_id) 
            movie_label = tk.Label(movie_window, text=movie_title)
            movie_label.grid(row = i, column = 0, padx = 10, pady = 10)"""

        delete_list_button = customtkinter.CTkButton(movie_window, text="Apagar lista", command=lambda list_id = id_list: self.delete_list(list_id))
        delete_list_button.grid(row=1, column=2, padx=10, pady=10)

    def delete_list(self, id_list):
        db = database()
        db.delete_list(id_list)
        messagebox.showinfo("Sucesso", "Lista apagada com sucesso!")
        self.app.destroy()

    def add_movie_to_list(self,id_filme,id_lista):
        db = database()
        if db.add_movie_to_list(id_filme,id_lista):
            messagebox.showinfo("Sucesso", "Filme adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Filme já está na lista!")

        self.app.destroy()