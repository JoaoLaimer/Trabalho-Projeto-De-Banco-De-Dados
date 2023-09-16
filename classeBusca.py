import tkinter as tk
from conexaoBD import database

class BuscaPage:
    def __init__(self,master,app):
        self.master = master
        self.app = app
        self.app.title("Busca")

        self.search_value = None
        self.search_type = None

        opcoes = ["Ator", "Diretor", "Filme", "Gênero", "Ano","Usuário"]
        self.opcoes_var = tk.StringVar(app)
        self.opcoes_var.set(opcoes[0])

        option_menu = tk.OptionMenu(app, self.opcoes_var, *opcoes)
        option_menu.grid(row=0, column=1,padx=10, pady=10)

        self.busca_entry = tk.Entry(app, width=30)
        self.busca_entry.grid(row=0, column=0,padx=10, pady=10)
        
        busca_button = tk.Button(app, text="Buscar", command= self.set_entry_menu)
        busca_button.grid(row=0, column=2,padx=10, pady=10)
        
    def set_entry_menu(self):
        self.search_value = self.busca_entry.get() 
        self.search_type = self.opcoes_var.get()
        db = database()
        if db.return_search(self.search_type,self.search_value):
            print("ok")
        else:
            print("nao encontrado")
            
        db.connection.close()

