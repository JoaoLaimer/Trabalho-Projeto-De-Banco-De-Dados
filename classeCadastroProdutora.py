import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
import customtkinter as ctk

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
        nome_produtora = self.produtora_entry.get()

        try:
            connection = psycopg2.connect(
                dbname="trabalhoPDB",
                user="postgres",
                password="271202",
                host="26.29.242.113",
                port="5432"
            )
            cursor = connection.cursor()

            consulta_sql = "INSERT INTO estudio(nome_estudio) VALUES (%s)"
            cursor.execute(consulta_sql, (nome_produtora,))

            connection.commit()
            connection.close()

            self.produtora_entry.delete(0, tk.END)
            messagebox.showinfo("Nome do App", "Produtora cadastrada com sucesso!")
        except Exception as e:
            messagebox.showinfo("Nome do App", "Erro ao cadastrar produtor: " + str(e))
