import tkinter as tk
import psycopg2
from tkinter import messagebox
from classeCadastroFilmeWindow import CadastroFilmeWindow
from conexaoBD import database
import customtkinter

class RegistroPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("320x400")
        self.master.title("Nome do App")

        # atributos de registro usuario
        self.nomeuser_entry = tk.Entry(master, width=30)
        self.emailuser_entry = tk.Entry(master, width=30)
        self.senhauser_entry = tk.Entry(master, width=30, show="*")
        self.telefoneuser_entry = tk.Entry(master, width=30)
        self.paisuser_entry = tk.Entry(master, width=30)

        nomeuser_label = customtkinter.CTkLabel(master, text="Nome de Usuário")
        nomeuser_label.pack()
        self.username_entry = customtkinter.CTkEntry(master, width=100)
        self.username_entry.pack()

        emailuser_label = customtkinter.CTkLabel(master, text="Email do Usuário")
        emailuser_label.pack()
        self.emailuser_entry = customtkinter.CTkEntry(master, width=100)
        self.emailuser_entry.pack()

        senhauser_label = customtkinter.CTkLabel(master, text="Senha de Usuário")
        senhauser_label.pack()
        self.senhauser_entry = customtkinter.CTkEntry(master, width=100, show="*")
        self.senhauser_entry.pack()

        telefoneuser_label = customtkinter.CTkLabel(master, text="Telefone do Usuário")
        telefoneuser_label.pack()
        self.telefoneuser_entry = customtkinter.CTkEntry(master, width=100)
        self.telefoneuser_entry.pack()

        paisuser_label = customtkinter.CTkLabel(master, text="País do Usuário")
        paisuser_label.pack()
        self.paisuser_entry = customtkinter.CTkEntry(master, width=100)
        self.paisuser_entry.pack()

        # botão de registro
        registro_button = customtkinter.CTkButton(master, text="Registrar", command=self.efetuar_registro)
        registro_button.pack(padx=10, pady=10)
        

    def efetuar_registro(self):
        nomeuser = self.nomeuser_entry.get()
        emailuser = self.emailuser_entry.get()
        senhauser = self.senhauser_entry.get()
        telefoneuser = self.telefoneuser_entry.get()
        paisuser = self.paisuser_entry.get()
        
        try:
            db = database()
            db.insert_newUser(nomeuser, emailuser, senhauser, telefoneuser, paisuser)

            self.nomeuser_entry.delete(0, tk.END)
            self.emailuser_entry.delete(0, tk.END)
            self.senhauser_entry.delete(0, tk.END)
            self.telefoneuser_entry.delete(0, tk.END)
            self.paisuser_entry.delete(0, tk.END)

            messagebox.showinfo("Nome do App", "Registro de usuário concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Nome do App", "Erro ao registrar usuário: " + str(e))






