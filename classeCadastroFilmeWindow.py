import tkinter as tk
import psycopg2
from tkinter import messagebox

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