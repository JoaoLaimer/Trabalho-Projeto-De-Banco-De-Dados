import tkinter as tk
import psycopg2
from tkinter import messagebox
from conexaoBD import database

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

    

    def efetuar_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            db = database()
            user_id = db.validate_login(username, password)[0] 
            if user_id is not None:
                #messagebox.showinfo("Nome do App", "Login bem-sucedido!")
                self.logged_in = True  # Define a variável para True após o login bem-sucedido
                self.master.withdraw()  # Oculta a janela de login
                self.app.ocultar_botao_login_registro()  # Oculta o botão de login e registrar
                self.app.set_user_id(db.validate_login(username, password)[0]) 
                self.app.create_landing_page()
            else:
                messagebox.showerror("Nome do App", "Credenciais inválidas. Tente novamente.")

            db.connection.close()
        except Exception as e:
            messagebox.showerror("Nome do App", "Erro ao efetuar login: " + str(e))
