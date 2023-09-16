import tkinter as tk
import psycopg2
from tkinter import messagebox

class LoginPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app  
        self.master.title("Nome do App")
        self.logged_in = False

        # login
        username_label = tk.Label(master, text="Nome de Usuário")
        username_label.pack()
        self.username_entry = tk.Entry(master, width=30)
        self.username_entry.pack()

        # senha com *
        password_label = tk.Label(master, text="Senha")
        password_label.pack()
        self.password_entry = tk.Entry(master, width=30, show="*")  # Mostrar asteriscos para a senha
        self.password_entry.pack()

        # botão de login
        login_button = tk.Button(master, text="Login", command=self.efetuar_login)
        login_button.pack()

        # botao de registro do filme
        self.registro_filme_button = tk.Button(master, text="Registrar Filme", command=self.abrir_pagina_registro_filme)
        self.registro_filme_button.pack()
        self.registro_filme_button.pack_forget()  # Oculta o botão no início

    def efetuar_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        try:
            connection = psycopg2.connect(
                dbname="trabalhoPDB",
                user="postgres",
                password="271202",
                host="26.29.242.113",
                port="5432"
            )
            cursor = connection.cursor()

            # Consulta SQL para verificar o login do usuario
            consulta_sql = "SELECT * FROM usuario WHERE (nomeuser = %s OR emailuser = %s) AND senhauser = %s"
            cursor.execute(consulta_sql, (username, username, password))
            resultado = cursor.fetchone()

            if resultado:
                messagebox.showinfo("Nome do App", "Login bem-sucedido!")
                self.logged_in = True  # Define a variável para True após o login bem-sucedido
                self.master.withdraw()  # Oculta a janela de login
                self.app.exibir_botao_registro_filme()  # Exibe o botão de registro de filme na janela principal
                self.app.ocultar_botao_login_registro()  # Oculta o botão de login e registrar
            else:
                messagebox.showerror("Nome do App", "Credenciais inválidas. Tente novamente.")

            connection.close()
        except Exception as e:
            messagebox.showerror("Nome do App", "Erro ao efetuar login: " + str(e))
