import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
import customtkinter as ctk
from conexaoBD import database  
from datetime import datetime

class CadastroFilmeWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Filme")

        self.titulofilme_entry = tk.Entry(master)
        self.genero_entry = tk.Entry(master)
        self.classificacao_entry = tk.Entry(master)
        self.paisdeproducao_entry = tk.Entry(master)
        self.duracao_entry = tk.Entry(master)
        self.datalancamento_entry = tk.Entry(master)
        self.diretor_entry = tk.Entry(master)
        self.produtora_entry = tk.Entry(master)

        titulo_label = ctk.CTkLabel(master, text="Título do Filme")
        titulo_label.pack()
        self.titulofilme_entry.pack()

        diretor_label = ctk.CTkLabel(master, text="Nome do Diretor do Filme")
        diretor_label.pack()
        self.diretor_entry.pack()
        
        produtora_label = ctk.CTkLabel(master, text="Nome da Produtora do Filme")
        produtora_label.pack()
        self.produtora_entry.pack()

        genero_label = ctk.CTkLabel(master, text="Gênero do Filme")
        genero_label.pack()
        self.genero_entry.pack()

        classificacao_label = ctk.CTkLabel(master, text="Classificação do Filme")
        classificacao_label.pack()
        self.classificacao_entry.pack()

        pais_label = ctk.CTkLabel(master, text="País de Produção")
        pais_label.pack()
        self.paisdeproducao_entry.pack()

        duracao_label = ctk.CTkLabel(master, text="Duração do Filme")
        duracao_label.pack()
        self.duracao_entry.pack()

        ano_label = ctk.CTkLabel(master, text="Data de Lançamento (dd/mm/aaaa)")
        ano_label.pack()
        self.datalancamento_entry.pack()

        # Botão Adicionar Filme
        insert_button = ctk.CTkButton(master, text="Adicionar Filme", command=self.adicionar_filme)
        insert_button.pack(padx=10, pady=10)

    def adicionar_filme(self):
        titulofilme = self.titulofilme_entry.get()
        generofilme = self.genero_entry.get()
        classificacao = self.classificacao_entry.get()
        paisdeproducao = self.paisdeproducao_entry.get()
        duracao = self.duracao_entry.get()
        datalancamento = self.datalancamento_entry.get()
        nomeestudio = self.produtora_entry.get()
        nomediretor = self.diretor_entry.get()

        try:
            datalancamento = datetime.strptime(datalancamento, '%d/%m/%Y').date()
            
        except ValueError:
            messagebox.showinfo("MovieHub", "Data de lançamento inválida!")
            return

        try:
            db = database()
            db.insert_newMovie(titulofilme, generofilme, classificacao, paisdeproducao, duracao, datalancamento, nomediretor, nomeestudio)

            self.titulofilme_entry.delete(0, tk.END)
            self.genero_entry.delete(0, tk.END)
            self.classificacao_entry.delete(0, tk.END)
            self.paisdeproducao_entry.delete(0, tk.END)
            self.duracao_entry.delete(0, tk.END)
            self.datalancamento_entry.delete(0, tk.END)

            messagebox.showinfo("MovieHub", "Filme adicionado com sucesso!")
        except Exception as e:
            messagebox.showinfo("MovieHub", "Erro ao adicionar filme: " + str(e))
