import tkinter as tk
import psycopg2
from conexaoBD import database
import customtkinter as ctk

class FilmePage:
    def __init__(self, master, top ,id_any, id_type):
        self.master = master
        self.top = top

        self.id_any = id_any
        self.id_type = id_type
        print(id_any,id_type)
        
        self.master.title("Resultado da Busca")

        db = database()
        if id_type != "Diretor" and id_type != "Produtora":
            self.qntd_filmes = db.qntd_filmes(self.id_type,self.top.get_search_value())
        else:
            self.qntd_filmes = db.qntd_filmes(self.id_type,self.id_any)
        print(self.qntd_filmes[0])

        self.master.geometry("400x500")

        if id_type == "Diretor":
            filme_info = db.return_filme(self.id_type,self.id_any)
            print(filme_info)
            diretor_nome = db.return_diretor(filme_info[0][6])
            for i in range(self.qntd_filmes[0]):
                estudio_nome = db.return_estudio(filme_info[i][7])
                filme_info_label = ctk.CTkLabel(master, text=f"Titulo: {filme_info[i][1]} \n Gênero: {filme_info[i][2]} \n Data de Lançamento: {filme_info[i][8]} \n Duração: {filme_info[i][3]} \n Classificação: {filme_info[i][4]} \n País de Produção: {filme_info[i][5]} \n Nome do Diretor: {diretor_nome[1]} \n Nome da Produtora: {estudio_nome[1]}")
                filme_info_label.grid(row=i, column=0, padx=10, pady=10)

                filme_adicionar_na_lista = ctk.CTkButton(master, text="Adicionar na Lista", command=lambda: self.adicionar_na_lista(filme_info[i][0]))
                filme_adicionar_na_lista.grid(row=i, column=1, padx=10, pady=10)

        elif id_type == "Produtora":
            filme_info = db.return_filme(self.id_type,self.id_any)
            estudio_nome = db.return_estudio(filme_info[0][7])
            for i in range(self.qntd_filmes[0]):
                diretor_nome = db.return_diretor(filme_info[i][6])
                filme_info_label = tk.Label(master, text=f"Titulo: {filme_info[i][1]} \n Gênero: {filme_info[i][2]} \n Data de Lançamento: {filme_info[i][8]} \n Duração: {filme_info[i][3]} \n Classificação: {filme_info[i][4]} \n País de Produção: {filme_info[i][5]} \n Nome do Diretor: {diretor_nome[1]} \n Nome da Produtora: {estudio_nome[1]}")
                filme_info_label.grid(row=i, column=0, padx=10, pady=10)
                
                filme_adicionar_na_lista = ctk.CTkButton(master, text="Adicionar na Lista", command=lambda: self.adicionar_na_lista(filme_info[i][0]))
                filme_adicionar_na_lista.grid(row=i+1, column=0, padx=10, pady=10)
        else:
            filme_info = db.return_search(self.id_type,self.top.get_search_value())
            print(filme_info)

            for i in range(self.qntd_filmes[0]):
                diretor_nome = db.return_diretor(filme_info[i][6])
                estudio_nome = db.return_estudio(filme_info[i][7])
                filme_info_label = tk.Label(master, text=f"Titulo: {filme_info[i][1]} \n Gênero: {filme_info[i][2]} \n Data de Lançamento: {filme_info[i][8]} \n Duração: {filme_info[i][3]} \n Classificação: {filme_info[i][4]} \n País de Produção: {filme_info[i][5]} \n Nome do Diretor: {diretor_nome[1]} \n Nome da Produtora: {estudio_nome[1]}")
                filme_info_label.grid(row=i, column=0, padx=10, pady=10)

                filme_adicionar_na_lista = ctk.CTkButton(master, text="Adicionar na Lista", command=lambda: self.adicionar_na_lista(filme_info[i][0]))
                filme_adicionar_na_lista.grid(row=i, column=1, padx=10, pady=10)

    def adicionar_na_lista(self,id_user_loggado, id_filme):
        db = database()
        db.add_movie_to_list(id_user_loggado, id_filme)
        db.connection.close()
    #consulta_sql = "SELECT titulofilme,generofilme,datalancamento,duracao,classificacao,paisdeproducao,nomediretor,nome_estudio FROM filme JOIN diretor on filme.id_diretor = diretor.id_diretor JOIN estudio on filme.id_estudio = estudio.id_estudio WHERE if_filme = %s"