import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
import customtkinter as ctk

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
        nome_ator = self.ator_entry.get()

        try:
            connection = psycopg2.connect(
                dbname="trabalhoPDB",
                user="postgres",
                password="271202",
                host="26.29.242.113",
                port="5432"
            )
            cursor = connection.cursor()

            consulta_sql = "INSERT INTO ator(nomeator) VALUES (%s)"
            cursor.execute(consulta_sql, (nome_ator,))

            connection.commit()
            connection.close()

            self.ator_entry.delete(0, tk.END)
            messagebox.showinfo("Nome do App", "Ator cadastrado com sucesso!")
        except Exception as e:
            messagebox.showinfo("Nome do App", "Erro ao cadastrar ator: " + str(e))
