import tkinter as tk
from tkinter import messagebox
from conexaoBD import database

class MinhasListasPage:
    def __init__(self, master, id_user_logged, app):
        self.master = master
        self.app = app  
        self.id_user_logged = id_user_logged
        self.app.title("Nome do App")
        
        db = database()
        self.user = db.return_user(self.id_user_logged)
        self.name = self.user[3]

        username_label = tk.Label(self.app, text=f"Lista de {self.name}").pack()

        total_lists = db.check_total_user_lists(self.id_user_logged)
        total_lists_label = tk.Label(self.app, text=f"Total de listas: {total_lists}").pack()

        

