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

        username_label = tk.Label(self.app, text=f"Lista de {self.name}")
        username_label.grid(row=0, column=0, padx=10, pady=10)

        total_lists = db.check_total_user_lists(self.id_user_logged)
        total_lists_label = tk.Label(self.app, text=f"Total de listas: {total_lists}")
        total_lists_label.grid(row=1, column=0, padx=10, pady=10)

        self.list_lists()
    def list_lists(self):
        rowIncrement = 2
        db = database()
        lists = db.return_user_lists(self.id_user_logged)
        for list in lists:
            list_name = list[1]
            list_id = list[3]
            list_label = tk.Label(self.app, text=f"Lista ID: {list_id}, Nome: {list_name}")
            list_label.grid(row = rowIncrement, column = 0, padx = 10, pady = 10)
            rowIncrement += 1


