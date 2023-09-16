import tkinter as tk
import psycopg2
from classeCadastroFilmeWindow import CadastroFilmeWindow
from classeLogin import LoginPage
from classeRegistro import RegistroPage

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Nome do App")
        self.botao_registro_filme = None  # none pq ele nao aparece
        self.botao_login_registro = None

        # botao pra tela de login
        open_login_signup_button = tk.Button(master, text="Login", command=self.abrir_pagina_login)
        open_login_signup_button.pack()
        
        open_registro_button = tk.Button(master, text="Sign Up", command=self.abrir_pagina_registro)
        open_registro_button.pack()

    def abrir_pagina_login(self):
        login_window = tk.Toplevel(self.master)
        login_page = LoginPage(login_window, self)
        self.botao_login_registro = login_page.botao_login_registro 
        
    def abrir_pagina_registro(self):
        registro_window = tk.Toplevel(self.master)
        registro_page = RegistroPage(registro_window)

    def exibir_botao_registro_filme(self):
        # botão de registro de filme na tela principal
        if self.botao_registro_filme is None:
            self.botao_registro_filme = tk.Button(self.master, text="Registrar Filme", command=self.abrir_pagina_registro_filme)
            self.botao_registro_filme.pack()

    def abrir_pagina_registro_filme(self):
        registro_filme_window = tk.Toplevel(self.master)
        registro_filme_page = CadastroFilmeWindow(registro_filme_window)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()