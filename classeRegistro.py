import tkinter as tk
import psycopg2
from tkinter import messagebox
from classeCadastroFilmeWindow import CadastroFilmeWindow
class RegistroPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Nome do App")

        # atributos de registro usuario
        self.nomeuser_entry = tk.Entry(master, width=30)
        self.emailuser_entry = tk.Entry(master, width=30)
        self.senhauser_entry = tk.Entry(master, width=30, show="*")
        self.telefoneuser_entry = tk.Entry(master, width=30)
        self.paisuser_entry = tk.Entry(master, width=30)

        nomeuser_label = tk.Label(master, text="Nome de Usuário")
        nomeuser_label.pack()
        self.nomeuser_entry.pack()

        emailuser_label = tk.Label(master, text="Email de Usuário")
        emailuser_label.pack()
        self.emailuser_entry.pack()

        senhauser_label = tk.Label(master, text="Senha de Usuário")
        senhauser_label.pack()
        self.senhauser_entry.pack()

        telefoneuser_label = tk.Label(master, text="Telefone de Usuário")
        telefoneuser_label.pack()
        self.telefoneuser_entry.pack()

        paisuser_label = tk.Label(master, text="País de Usuário")
        paisuser_label.pack()
        self.paisuser_entry.pack()

        # botão de registro
        registro_button = tk.Button(master, text="Registrar", command=self.efetuar_registro)
        registro_button.pack()

    def efetuar_registro(self):
        nomeuser = self.nomeuser_entry.get()
        emailuser = self.emailuser_entry.get()
        senhauser = self.senhauser_entry.get()
        telefoneuser = self.telefoneuser_entry.get()
        paisuser = self.paisuser_entry.get()

        try:
            connection = psycopg2.connect(
                dbname="trabalhoPDB",
                user="postgres",
                password="271202",
                host="26.29.242.113",
                port="5432"
            )
            cursor = connection.cursor()

            consulta_sql = "INSERT INTO usuario(nomeuser, emailuser, senhauser, telefoneuser, paisuser) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(consulta_sql, (nomeuser, emailuser, senhauser, telefoneuser, paisuser))

            connection.commit()
            connection.close()

            self.nomeuser_entry.delete(0, tk.END)
            self.emailuser_entry.delete(0, tk.END)
            self.senhauser_entry.delete(0, tk.END)
            self.telefoneuser_entry.delete(0, tk.END)
            self.paisuser_entry.delete(0, tk.END)

            messagebox.showinfo("Nome do App", "Registro de usuário concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Nome do App", "Erro ao registrar usuário: " + str(e))




    def abrir_pagina_registro_filme(self):
        registro_filme_window = tk.Toplevel(self.master)
        registro_filme_page = CadastroFilmeWindow(registro_filme_window)




