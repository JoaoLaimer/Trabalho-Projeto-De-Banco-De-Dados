import tkinter as tk
from conexaoBD import database

class ExibeReviewsPage:
    def __init__(self,master,id_user, bool):
        self.master = master
        self.id_user = id_user
        self.bool = bool
        self.master.geometry("600x320")
        self.master.title("Review")
        
        self.exibe_reviews(id_user)

    def exibe_reviews(self,id_user):
        db = database()
        reviews = db.return_review_by_user(id_user)
        for i in range(len(reviews)):
            self.label_filme = tk.Label(self.master, text=f"Filme: {reviews[i][1]}")
            self.label_filme.grid(row=i, column=0, padx=10, pady=10)

            self.label_nota = tk.Label(self.master, text=f"Nota: {reviews[i][2]}")
            self.label_nota.grid(row=i, column=1, padx=10, pady=10)

            if reviews[i][3] != None:
                self.label_review = tk.Label(self.master, text=f"Review: {reviews[i][3]}")
                self.label_review.grid(row=i, column=2, padx=10, pady=10)

        
