import tkinter as tk
from tkinter import Canvas, Frame, Scrollbar
from conexaoBD import database
import customtkinter as ctk

class ExibeReviewsPage:
    def __init__(self, master, id_user, bool):
        self.master = master
        self.id_user = id_user
        self.bool = bool
        self.master.geometry("400x420")
        self.master.title("Review")
        
        self.canvas = Canvas(self.master)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.scrollbar = Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        
        self.exibe_reviews(id_user)

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        if self.canvas.winfo_height() >= self.frame.winfo_reqheight():
            self.scrollbar.pack_forget()
        else:
            self.scrollbar.pack(side="right", fill="y")

    def exibe_reviews(self, id_user):
        db = database()
        reviews = db.return_review_by_user(id_user)

        for i in range(len(reviews)):
            frame = Frame(self.frame)
            frame.pack(fill=tk.X, padx=10, pady=5)

            titulo = tk.StringVar(value=f"Filme")
            label = ctk.CTkLabel(
                frame, 
                textvariable=titulo,
                width=250,
                height=25,
                fg_color=("SeaGreen2", "gray75"),
                corner_radius=5
            )
            label.pack(fill=tk.BOTH, expand=True)
            
            titulo_id = tk.StringVar(value=f"{reviews[i][1]}")
            label = ctk.CTkLabel(
                frame,  
                textvariable=titulo_id,
                width=250,
                height=25,
                fg_color=("gainsboro", "gray75"),
                corner_radius=5
            )
            label.pack(fill=tk.BOTH, expand=True)

            nota = tk.StringVar(value=f"Nota")
            label = ctk.CTkLabel(
                frame,  
                textvariable=nota,
                width=250,
                height=25,
                fg_color=("SeaGreen2", "gray75"),
                corner_radius=5
            )
            label.pack(fill=tk.BOTH, expand=True)

            nota_id = tk.StringVar(value=f"{reviews[i][2]}")
            label = ctk.CTkLabel(
                frame,  
                textvariable=nota_id,
                width=250,
                height=25,
                fg_color=("gainsboro", "gray75"),
                corner_radius=5
            )
            label.pack(fill=tk.BOTH, expand=True)

            if reviews[i][3] is not None:
                review = tk.StringVar(value=f"Review")
                label = ctk.CTkLabel(
                    frame, 
                    textvariable=review,
                    width=250,
                    height=25,
                    fg_color=("SeaGreen2", "gray75"),
                    corner_radius=5
                )
                label.pack(fill=tk.BOTH, expand=True)

                review_id = tk.StringVar(value=f"{reviews[i][3]}")
                label = ctk.CTkLabel(
                    frame,  
                    textvariable=review_id,
                    width=250,
                    height=100,
                    fg_color=("gainsboro", "gray75"),
                    corner_radius=5
                )
                label.pack(fill=tk.BOTH, expand=True)

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


