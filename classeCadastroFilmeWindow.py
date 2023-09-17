import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import messagebox
import customtkinter as ctk

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
        self.id_diretor_entry = tk.Entry(master)
        self.id_produtora_entry = tk.Entry(master)

        titulo_label = ctk.CTkLabel(master, text="Título do Filme")
        titulo_label.pack()
        self.titulofilme_entry.pack()

        id_diretor_label = ctk.CTkLabel(master, text="ID Diretor do Filme")
        id_diretor_label.pack()
        self.id_diretor_entry.pack()
        
        id_produtora_label = ctk.CTkLabel(master, text="ID Produtora do Filme")
        id_produtora_label.pack()
        self.id_produtora_entry.pack()

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

        ano_label = ctk.CTkLabel(master, text="Data de Lançamento")
        ano_label.pack()
        self.datalancamento_entry.pack()

        # Botão Adicionar Filme
        insert_button = ctk.CTkButton(master, text="Adicionar Filme", command=self.adicionar_filme)
        insert_button.pack(padx=10, pady=10)

    def adicionar_filme(self):
        titulo = self.titulofilme_entry.get()
        genero = self.genero_entry.get()
        classificacao = self.classificacao_entry.get()
        pais = self.paisdeproducao_entry.get()
        duracao = self.duracao_entry.get()
        ano = self.datalancamento_entry.get()
        produtora = self.id_produtora_entry.get()
        diretor = self.id_diretor_entry.get()

        try:
            connection = psycopg2.connect(
                dbname="trabalhoPDB",
                user="postgres",
                password="271202",
                host="26.29.242.113",
                port="5432"
            )
            cursor = connection.cursor()

            # Consulta SQL para inserir o filme na tabela
            consulta_sql = "INSERT INTO filme(titulofilme, generofilme, classificacao, paisdeproducao, duracao, datalancamento, id_diretor, id_estudio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(consulta_sql, (titulo, genero, classificacao, pais, duracao, ano, diretor, produtora))

            connection.commit()
            connection.close()

            self.titulofilme_entry.delete(0, tk.END)
            self.genero_entry.delete(0, tk.END)
            self.classificacao_entry.delete(0, tk.END)
            self.paisdeproducao_entry.delete(0, tk.END)
            self.duracao_entry.delete(0, tk.END)
            self.datalancamento_entry.delete(0, tk.END)

            messagebox.showinfo("Nome do App", "Filme adicionado com sucesso!")
        except Exception as e:
            messagebox.showinfo("Nome do App", "Erro ao adicionar filme: " + str(e))
