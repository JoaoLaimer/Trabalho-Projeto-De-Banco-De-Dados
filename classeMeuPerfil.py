import tkinter as tk
import psycopg2
from conexaoBD import database


class MeuPerfilPage:
    def __init__(self, master, id_userLogged, app):
        self.master = master
        self.id_user_logged = id_userLogged
        self.app = app  
        self.app.title("Meu Perfil")

        db = database()
        self.user = db.return_user(self.id_user_logged)

        self.name = self.user[3]
        self.followers = self.user[1]
        self.following = self.user[2]
        self.country = self.user[7]
        self.email = self.user[4]

        user_info_label = tk.Label(self.app, text=f"Nome do Usuário: {self.name} \n Seguidores:{self.followers} \tSeguindo: {self.following} \n País {self.country} \nEmail {self.following}").pack()
        user_my_list = tk.Button(self.app, text="Minha Lista").pack()
'''
    def user_name(self):
        return "USER_NAME"
    def user_followers( self ):
        return "10"
    def user_following( self ):
        return "10"
    def user_country( self ):
        return "USER_COUNTRY"
    def user_email(self):
        return "USER_EMAIL"

if __name__ == "__main__":
    root = tk.Tk()
    id_userLogged = 1 
    app = MeuPerfil(root, id_userLogged, None)  
    root.mainloop() '''