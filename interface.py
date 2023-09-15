import tkinter as tk
import psycopg2
from tkinter import messagebox

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


    def abrir_pagina_registro_filme(self):
        registro_filme_window = tk.Toplevel(self.master)
        registro_filme_page = CadastroFilmeWindow(registro_filme_window)

class CadastroFilmeWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Filme")
    
        # entrada pros atributos do filme
        self.titulofilme_entry = tk.Entry(master)
        self.diretorfilme_entry = tk.Entry(master)
        self.genero_entry = tk.Entry(master)
        self.classificacao_entry = tk.Entry(master)
        self.paisdeproducao_entry = tk.Entry(master)
        self.duracao_entry = tk.Entry(master)
        self.elencofilme_entry = tk.Entry(master)
        self.datalancamento_entry = tk.Entry(master)

        titulo_label = tk.Label(master, text="Título do Filme")
        titulo_label.pack()
        self.titulofilme_entry.pack()

        diretor_label = tk.Label(master, text="Diretor do Filme")
        diretor_label.pack()
        self.diretorfilme_entry.pack()

        genero_label = tk.Label(master, text="Gênero do Filme")
        genero_label.pack()
        self.genero_entry.pack()

        classificacao_label = tk.Label(master, text="Classificação do Filme")
        classificacao_label.pack()
        self.classificacao_entry.pack()

        pais_label = tk.Label(master, text="País de Produção")
        pais_label.pack()
        self.paisdeproducao_entry.pack()

        duracao_label = tk.Label(master, text="Duração do Filme")
        duracao_label.pack()
        self.duracao_entry.pack()

        elenco_label = tk.Label(master, text="Elenco do Filme")
        elenco_label.pack()
        self.elencofilme_entry.pack()

        ano_label = tk.Label(master, text="Ano de Lançamento")
        ano_label.pack()
        self.datalancamento_entry.pack()

        # botao add
        insert_button = tk.Button(master, text="Adicionar Filme", command=self.adicionar_filme)
        insert_button.pack()

    def adicionar_filme(self):
        titulo = self.titulofilme_entry.get()
        diretor = self.diretorfilme_entry.get()
        genero = self.genero_entry.get()
        classificacao = self.classificacao_entry.get()
        pais = self.paisdeproducao_entry.get()
        duracao = self.duracao_entry.get()
        elenco = self.elencofilme_entry.get()
        ano = self.datalancamento_entry.get()

        try:
            connection = psycopg2.connect(
                dbname="trabalhoPDB",
                user="postgres",
                password="271202",
                host="26.29.242.113",
                port="5432"
            )
            cursor = connection.cursor()

            # Consulta SQL para inserir o filme
            consulta_sql = "INSERT INTO filme(titulofilme, diretorfilme, generofilme, classificacao, paisdeproducao, duracao, elencofilme, datalancamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(consulta_sql, (titulo, diretor, genero, classificacao, pais, duracao, elenco, ano))

            connection.commit()
            connection.close()

            # limpa as caixas dps de inserir
            self.titulofilme_entry.delete(0, tk.END)
            self.diretorfilme_entry.delete(0, tk.END)
            self.genero_entry.delete(0, tk.END)
            self.classificacao_entry.delete(0, tk.END)
            self.paisdeproducao_entry.delete(0, tk.END)
            self.duracao_entry.delete(0, tk.END)
            self.elencofilme_entry.delete(0, tk.END)
            self.datalancamento_entry.delete(0, tk.END)
            
            messagebox.showinfo("Nome do App", "Filme adicionado com sucesso!")
        except Exception as e:
            messagebox.showinfo("Nome do App", "Erro ao adicionar filme: " + str(e))

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
