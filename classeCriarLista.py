import tkinter as tk
from tkinter import messagebox
from conexaoBD import database

class CriarListaPage:
    def __init__(self, master, id_user_logged, app):
        self.master = master
        self.app = app  
        self.id_user_logged = id_user_logged
        self.app.title("Cria Lista")
        
        db = database()
        
        list_name_label = tk.Label(self.app, text="Digite o nome da lista:")
        list_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.list_name_entry = tk.Entry(self.app, width=30)
        self.list_name_entry.grid(row=1, column=0, padx=10, pady=10)

        confirm_creation_list = tk.Button(self.app, text="Criar Lista", command=self.create_new_list)
        confirm_creation_list.grid(row=1, column=1, padx=10, pady=10)

    def create_new_list(self):
        db = database()
        list_name = self.list_name_entry.get()
        db.create_new_list(self.id_user_logged, list_name)

