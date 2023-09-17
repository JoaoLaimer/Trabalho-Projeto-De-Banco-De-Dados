import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
import customtkinter as ctk
from conexaoBD import database

class CadastroAtorWindow(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Atorr")
        
        self.ator_entry = ctk.CTkEntry(master)
        
        titulo_label = ctk.CTkLabel(master, text="Nome do Ator")
        titulo_label.pack()
        self.ator_entry.pack()

        insert_button = ctk.CTkButton(master, text="Adicionar Ator", command=self.salvar_ator)
        insert_button.pack(padx=10, pady=10)

    def salvar_ator(self):
        nomeator = self.ator_entry.get()

        try:
            db = database()
            db.insert_newAtor(nomeator)

            self.ator_entry.delete(0, tk.END)
            messagebox.showinfo("Nome do App", "Ator cadastrado com sucesso!")
        except Exception as e:
            messagebox.showinfo("Nome do App", "Erro ao cadastrar ator: " + str(e))
