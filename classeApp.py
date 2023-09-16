import tkinter as tk
import psycopg2
from classeCadastroFilmeWindow import CadastroFilmeWindow
from classeLogin import LoginPage
from classeRegistro import RegistroPage
from classeMeuPerfil import MeuPerfilPage

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.master.title("Nome do App")
        self.botao_registro_filme = None  # none pq ele nao aparece
        self.botao_login_registro = None

        # botao pra tela de login
        self.login_button = tk.Button(master, text="Login", command=self.abrir_pagina_login)
        self.login_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.signup_button = tk.Button(master, text="Sign Up", command=self.abrir_pagina_registro)
        self.signup_button.grid(row=0, column=1, padx=10, pady=10)

        self.user_id = None

    def abrir_pagina_login(self):
        login_window = tk.Toplevel(self.master)
        login_page = LoginPage(login_window, self)
        
    def abrir_pagina_registro(self):
        registro_window = tk.Toplevel(self.master)
        registro_page = RegistroPage(registro_window)

    def ocultar_botao_login_registro(self):
        # ocultar botão de login e registrar
        if self.login_button is not None and self.signup_button is not None:
            self.login_button.grid_remove()
            self.signup_button.grid_remove()
    
    def set_user_id(self, user_id):
        self.user_id = user_id

    def create_landing_page(self):
        self.master.geometry("500x500")

        self.perfil_button = tk.Button(self.master, text="Perfil", command=self.abrir_pagina_perfil)
        self.perfil_button.grid(row=0, column=0, padx=10, pady=10)
    
    def abrir_pagina_perfil(self):
        perfil_window = tk.Toplevel(self.master)
        perfil_page = MeuPerfilPage(self,self.user_id, perfil_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()