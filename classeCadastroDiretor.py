import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
from conexaoBD import database  
import customtkinter as ctk

class CadastroDiretorWindow(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Diretor")
        
        self.diretor_entry = ctk.CTkEntry(master)
        
        titulo_label = ctk.CTkLabel(master, text="Nome do Diretor")
        titulo_label.pack()
        self.diretor_entry.pack()

        insert_button = ctk.CTkButton(master, text="Adicionar Diretor", command=self.salvar_diretor)
        insert_button.pack(padx=10, pady=10)
        
    def salvar_diretor(self):
        nomediretor = self.diretor_entry.get()

        try:
            db = database()
            db.insert_newDiretor(nomediretor)
            
            self.diretor_entry.delete(0, tk.END)
            messagebox.showinfo("Nome do App", "Diretor cadastrado com sucesso!")
        except Exception as e:
            messagebox.showinfo("Nome do App", "Erro ao cadastrar diretor: " + str(e))

    