import tkinter as tk
from tkinter import messagebox
import customtkinter
from conexaoBD import database  

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

class LoginPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.master.geometry("320x400")
        self.master.title("Nome do App")
        self.logged_in = False

        # login
        username_label = customtkinter.CTkLabel(master, text="Nome de Usuário")
        username_label.pack()
        self.username_entry = customtkinter.CTkEntry(master, width=100)
        self.username_entry.pack()

        # senha com *
        password_label = customtkinter.CTkLabel(master, text="Senha")
        password_label.pack()
        self.password_entry = customtkinter.CTkEntry(master, width=100, show="*")
        self.password_entry.pack()

        # botão de login
        login_button = customtkinter.CTkButton(master, text="Login", command=self.efetuar_login)
        login_button.pack(padx=10, pady=10)

    def efetuar_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            db = database()
            user_id = db.validate_login(username, password)[0]
            if user_id is not None:
                self.logged_in = True
                self.master.withdraw()
                self.app.ocultar_botao_login_registro()
                self.app.set_user_id_loggado(db.validate_login(username, password)[0])
                self.app.create_landing_page()
            else:
                messagebox.showerror("Nome do App", "Credenciais inválidas. Tente novamente.")

            db.connection.close()
        except Exception as e:
            messagebox.showerror("Nome do App", "Erro ao efetuar login: " + str(e))