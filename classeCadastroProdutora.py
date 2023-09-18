import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
import customtkinter as ctk
from conexaoBD import database  

class CadastroProdutoraWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Produtora")
        
        self.produtora_entry = ctk.CTkEntry(master)
        
        titulo_label = ctk.CTkLabel(master, text="Nome da Produtora")
        titulo_label.pack()
        self.produtora_entry.pack()

        insert_button = ctk.CTkButton(master, text="Adicionar Produtora", command=self.salvar_produtora)
        insert_button.pack(padx=10, pady=10)

    def salvar_produtora(self):
        nome_estudio = self.produtora_entry.get()

        try:
            db = database()
            db.insert_newProdutora(nome_estudio)

            self.produtora_entry.delete(0, tk.END)
            messagebox.showinfo("MovideHub", "Produtora cadastrada com sucesso!")
        except Exception as e:
            messagebox.showinfo("MovideHub", "Erro ao cadastrar produtor: " + str(e))
