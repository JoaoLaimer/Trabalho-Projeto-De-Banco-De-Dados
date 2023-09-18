import tkinter as tk
from tkinter import ttk, messagebox
from conexaoBD import database
import customtkinter as ctk
from ttkthemes import ThemedTk

class ReviewPage:
    def __init__(self, master,id_filme, id_user):
        self.master = master
        self.master.geometry("320x500")
        self.master.title("Review")
        self.id_filme = id_filme
        self.id_user = id_user

        self.label_nota = ctk.CTkLabel(self.master, text="Nota:")
        self.label_nota.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.scale_nota = ttk.Scale(self.master, from_=0, to=5, orient=tk.HORIZONTAL, style="TScale.Horizontal.TScale")
        self.scale_nota.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.label_review = tk.Label(self.master, text="Review:")
        self.label_review.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.text_box = tk.Text(self.master, wrap=tk.WORD, height=10, width=40)
        self.text_box.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        self.review_button = ctk.CTkButton(self.master, text="Enviar Review", command=lambda id_filme = self.id_filme, id_user = self.id_user: self.enviar_review(id_filme,id_user))
        self.review_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)


    def enviar_review(self,id_filme,id_user):
        db = database()
        db.insert_review(self.id_filme,self.id_user,self.scale_nota.get(),self.text_box.get("1.0",tk.END))
        self.master.destroy()
        messagebox.showinfo("Review","Review enviado com sucesso!")
    
        