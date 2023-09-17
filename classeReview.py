import tkinter as tk
from tkinter import messagebox
from conexaoBD import database

class ReviewPage:
    def __init__(self,master,id_filme,id_user):
        self.master = master
        self.master.geometry("600x320")
        self.master.title("Review")
        self.id_filme = id_filme
        self.id_user = id_user

        self.label_nota = tk.Label(master, text="Nota")
        self.label_nota.grid(row=0, column=0, padx=10, pady=10)

        self.scale_nota = tk.Scale(master, from_=0, to=5, orient=tk.HORIZONTAL)
        self.scale_nota.grid(row=0, column=1, padx=10, pady=10)

        self.label_review = tk.Label(master, text="Review")
        self.label_review.grid(row=1, column=0, padx=10, pady=10)

        self.text_box = tk.Text(master, wrap=tk.WORD, height=10, width=40)
        self.text_box.grid(row=2, column=0, padx=10, pady=10)

        self.review_button = tk.Button(master, text="Enviar Review", command=lambda: self.enviar_review(self.id_filme,self.id_user))
        self.review_button.grid(row=3, column=0, padx=10, pady=10)

    def enviar_review(self,id_filme,id_user):
        db = database()
        db.insert_review(self.id_filme,self.id_user,self.scale_nota.get(),self.text_box.get("1.0",tk.END))
        self.master.destroy()
        messagebox.showinfo("Review","Review enviado com sucesso!")
    
        