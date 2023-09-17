import tkinter as tk
import psycopg2
import customtkinter
from classeCadastroFilmeWindow import CadastroFilmeWindow
from classeLogin import LoginPage
from classeRegistro import RegistroPage
from classeMeuPerfil import MeuPerfilPage
from classeBusca import BuscaPage
from classeMinhasListas import MinhasListasPage
from classeCriarLista import CriarListaPage
from classeFilme import FilmePage
import tkinter.messagebox


customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("blue")  


class App(customtkinter.CTk):

    def __init__(self, master):
        super().__init__()
        
        self.master = master
        self.master.geometry("320x400")
        self.master.title("Nome do App")
        self.master.configure(bg="lightgray")
        self.button_style = ("Arial", 28)
        self.botao_registro_filme = None  # none pq ele nao aparece
        self.botao_login_registro = None

        # botao pra tela de login
        self.login_button = customtkinter.CTkButton(master, text="Login", command=self.abrir_pagina_login)
        self.login_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.signup_button = customtkinter.CTkButton(master, text="Sign Up", command=self.abrir_pagina_registro)
        self.signup_button.grid(row=0, column=1, padx=10, pady=10)


        self.user_id_loggado = None
        

    def abrir_pagina_login(self):
        login_window = tk.Toplevel(self.master)
        login_page = LoginPage(login_window, self)
        
    def abrir_pagina_registro(self):
        registro_window = tk.Toplevel(self.master)
        registro_page = RegistroPage(registro_window)

    def ocultar_botao_login_registro(self):
        if self.login_button is not None and self.signup_button is not None:
            self.login_button.grid_remove()
            self.signup_button.grid_remove()
    
    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_user_id_loggado(self, user_id):
        self.user_id_loggado = user_id

    def create_landing_page(self):
        self.master.geometry("320x400")
        
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.perfil_button = customtkinter.CTkButton(self.master, text="Perfil", command=lambda :self.abrir_pagina_perfil(self.user_id_loggado))
        self.perfil_button.grid(row=2, column=0, padx=20, pady=10)

        self.busca_button = customtkinter.CTkButton(self.master, text="Busca", command=self.abrir_pagina_busca)
        self.busca_button.grid(row=3, column=0, padx=20, pady=10)

        self.minha_lista_button = customtkinter.CTkButton(self.master, text="Minhas Listas", command=lambda :self.exibir_lista_filmes(self.user_id_loggado, True))
        self.minha_lista_button.grid(row=4, column=0, padx=20, pady=10)

<<<<<<< HEAD
        self.minha_lista_button = tk.Button(self.master, text="Minhas Listas", command=lambda :self.exibir_lista_filmes(self.user_id_loggado, True))
        self.minha_lista_button.grid(row=0, column=2, padx=10, pady=10)

        self.cria_lista_button = tk.Button(self.master, text="Criar Lista", command=self.abrir_pagina_criar_lista)
        self.cria_lista_button.grid(row=0, column=3, padx=10, pady=10)
=======
        self.cria_lista_button = customtkinter.CTkButton(self.master, text="Criar Lista", command=self.abrir_pagina_criar_lista)
        self.cria_lista_button.grid(row=5, column=0, padx=10, pady=10)
>>>>>>> 91e5745453fa1051049e4ab7e1bbc5f6aa27dea1

    def abrir_pagina_perfil(self,user_id):
        perfil_window = tk.Toplevel(self.master)
        perfil_page = MeuPerfilPage(self, user_id, self.user_id_loggado, perfil_window)
    
    def abrir_pagina_busca(self):
        busca_window = tk.Toplevel(self.master)
        busca_page = BuscaPage(self, busca_window,self.user_id_loggado)
    
    def exibir_lista_filmes(self, id_user, bool):
        lista_window = tk.Toplevel(self.master)
        lista_page = MinhasListasPage(self, id_user, bool, lista_window)

    def abrir_pagina_criar_lista(self):
        cria_lista_window = tk.Toplevel(self.master)
        cria_lista_page = CriarListaPage(self,self.user_id_loggado, cria_lista_window)


    

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()