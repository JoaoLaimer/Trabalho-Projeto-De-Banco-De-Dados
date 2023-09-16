import tkinter as tk
import psycopg2


class MeuPerfil:
    def __init__(self, master, id_userLogged, app):
        self.master = master
        self.id_user_logged = id_userLogged
        self.app = app  
        self.master.title("Meu Perfil")
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.name = self.user_name()
        self.followers = self.user_followers()
        self.following = self.user_following()
        self.country = self.user_country()
        self.email = self.user_email()

        user_info_label = tk.Label(self.master, text=f"Nome do Usuário: {self.name} Seguidores {self.followers} Seguindo {self.following} \n País {self.country} \nEmail {self.following}").pack()
        button_frame = tk.Frame(master)
        button_frame.pack()
        user_my_list = tk.Button(button_frame, text="Minha Lista").pack()

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
    root.mainloop()