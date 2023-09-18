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
            self.list_id = lists[i][3]
            list_label = [None for _ in range(len(lists))]

            if self.id_filme != None:
                list_label[i] = customtkinter.CTkButton(self.app, text=f"{list_name}", command=lambda list_id = self.list_id: self.add_movie_to_list(self.id_filme,list_id))
                list_label[i].grid(row = i, column = 0, padx = 10, pady = 10) 
            else:
                if self.bool:
                    list_label[i] = customtkinter.CTkButton(self.app, text=f"{list_name}", command=lambda list_id = self.list_id: self.show_movies_in_list(list_id, True))
                    list_label[i].grid(row = i + 2, column = 0, padx = 10, pady = 10)
                else:
                    list_label[i] = customtkinter.CTkButton(self.app, text=f"{list_name}", command=lambda list_id = self.list_id: self.show_movies_in_list(list_id, False))
                    list_label[i].grid(row = i + 2, column = 0, padx = 10, pady = 10)
                    if not db.check_like(self.list_id, self.id_user):
                        self.like_button[i] = customtkinter.CTkButton(self.app, text="Curtir", command=lambda list_id = self.list_id, row = i: self.like_event(list_id,row))
                        self.like_button[i].grid(row=i + 2, column=2, padx=10, pady=10)
                    else:
                        self.like_button[i] = customtkinter.CTkButton(self.app, text="Descurtir", command=lambda list_id = self.list_id, row = i: self.unlike_event(list_id,row))
                        self.like_button[i].grid(row=i + 2, column=2, padx=10, pady=10)

    def like_event(self, id_list,pos):
        db = database()
        db.like_list(id_list, self.id_user)
        self.like_button[pos].grid_remove()
        self.like_button[pos] = customtkinter.CTkButton(self.app, text="Descurtir", command=lambda list_id = id_list, row=pos: self.unlike_event(list_id,row))
        self.like_button[pos].grid(row=pos + 2, column=2, padx=10, pady=10)
         
    def unlike_event(self, id_list,pos):
        db = database()
        db.unlike_list(id_list, self.id_user)
        self.like_button[pos].grid_remove()
        self.like_button[pos] = customtkinter.CTkButton(self.app, text="Curtir", command=lambda list_id = id_list, row=pos: self.like_event(list_id,row))
        self.like_button[pos].grid(row=pos + 2, column=2, padx=10, pady=10)
            
    def show_movies_in_list(self, id_list, bool):
        db = database()
        movies = db.return_movies_in_list(id_list)

        self.movie_window = tk.Toplevel(self.app)
        self.movie_window.title("Filmes da Lista")
        if bool:
            list_name = tk.Label(self.movie_window, text=f"lista: {db.get_list_name(id_list)[0]}", cursor="hand2")
            list_name.bind("<Button-1>", lambda event, list_id=id_list: self.change_list_name(list_id))
            list_name.grid(row=0, column=0, padx=10, pady=10)
        else:
            list_name = tk.Label(self.movie_window, text=f"lista: {db.get_list_name(id_list)[0]}")
            list_name.grid(row=0, column=0, padx=10, pady=10)
        self.delete_movie_button = [None for _ in range(len(movies))]
        for i in range(len(movies)):
            movie_id = movies[i][0]
            movie_title = db.get_movie_name(movie_id)
            
            print(movie_title)

            movie_button = customtkinter.CTkButton(self.movie_window, text=f"{movie_title[0]}", cursor="hand2", command=lambda movie_id=movie_id: self.show_movie_details(movie_id))
            movie_button.grid(row=i+1, column=0, padx=10, pady=10)
            if bool:
                self.delete_movie_button[i] = customtkinter.CTkButton(self.movie_window, text="X", command=lambda id_movie = movie_id, list_id = id_list, row = i: self.delete_movie(id_movie, list_id, row))
                self.delete_movie_button[i].grid(row=i+1, column=1, padx=10, pady=10)
        if bool:      
            delete_list_button = customtkinter.CTkButton(self.movie_window, text="Apagar lista", command=lambda list_id = id_list: self.delete_list(list_id))
            delete_list_button.grid(row=0, column=1, padx=10, pady=10)

    def delete_list(self, id_list):
        db = database()
        db.delete_list(id_list)
        messagebox.showinfo("Sucesso", "Lista apagada com sucesso!")
        self.app.destroy()

    def delete_movie(self, id_movie, id_list, pos):
        db = database()
        db.delete_movie(id_movie, id_list)
        self.delete_movie_button[pos].grid_remove()
        self.movie_window.destroy()
        self.show_movies_in_list(id_list, True) 

    def add_movie_to_list(self,id_filme,id_lista):
        db = database()
        if db.add_movie_to_list(id_filme,id_lista):
            messagebox.showinfo("Sucesso", "Filme adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Filme já está na lista!")
        self.app.destroy()

    def show_movie_details(self, id_filme):
        db = database()
        self.movie_details = db.return_filme("filme", id_filme)
        self.movie_details_window = tk.Toplevel(self.movie_window)
        self.movie_details_window.title("Detalhes do Filme")
        
        labels_info = [
            ("Titulo", 1),
            ("Gênero", 2),
            ("Duração", 3),
            ("Classificação", 4),
            ("País de Produção", 5),
            ("Diretor", 6),
            ("Produtora", 7),
            ("Data de Lançamento", 8),
            ("Descrição", 9)
        ]

        for i, (label_text, column) in enumerate(labels_info):
            value = self.movie_details[0][column]
            if column == 6:
                value = db.return_diretor(value)[1]
            elif column == 7:
                value = db.return_estudio(value)[1]

            label = customtkinter.CTkLabel(self.movie_details_window, text=f"{label_text}: {value}")
            label.grid(row=i, column=0, padx=10, pady=10)

    def change_list_name(self, id_list):
        self.change_list_name_window = tk.Toplevel(self.movie_window)
        self.change_list_name_window.title("Mudar nome da lista")
        list_name_label = customtkinter.CTkLabel(self.change_list_name_window, text="Digite o nome da lista:")
        list_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.list_name_entry = tk.Entry(self.change_list_name_window, width=30)
        self.list_name_entry.grid(row=1, column=0, padx=10, pady=10)

        confirm_creation_list = customtkinter.CTkButton(self.change_list_name_window, text="Mudar nome", command= lambda: self.confirm_change(id_list, self.list_name_entry.get()))
        confirm_creation_list.grid(row=1, column=1, padx=10, pady=10)
        
    def confirm_change(self, id_list, new_list_name):
        db = database()
        db.change_list_name(id_list, new_list_name)
        self.change_list_name_window.destroy()
        