import tkinter as tk
from tkinter import messagebox
from conexaoBD import database
import customtkinter

class CriarListaPage:
    def __init__(self, master, id_user_logged, app):
        self.master = master
        self.app = app  
        self.master.geometry("320x400")
        self.id_user_logged = id_user_logged
        self.app.title("Cria Lista")
        
        db = database()
        
        list_name_label = customtkinter.CTkLabel(self.app, text="Digite o nome da lista:")
        list_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.list_name_entry = tk.Entry(self.app, width=30)
        self.list_name_entry.grid(row=1, column=0, padx=10, pady=10)

        confirm_creation_list = customtkinter.CTkButton(self.app, text="Criar Lista", command=self.create_new_list)
        confirm_creation_list.grid(row=1, column=1, padx=10, pady=10)

    def create_new_list(self):
        db = database()
        list_name = self.list_name_entry.get()
        if self.validate_input(list_name):
            db.create_new_list(self.id_user_logged, list_name)
            self.app.destroy()

    def validate_input(self, list_name):
        list_name = self.list_name_entry.get()
        if list_name == "":
            messagebox.showerror("Erro", "Nome da lista não pode ser vazio! Tente novamente.")
            return False
        else:
            messagebox.showinfo("Sucesso", f"Nome da lista: {list_name}")
            return True