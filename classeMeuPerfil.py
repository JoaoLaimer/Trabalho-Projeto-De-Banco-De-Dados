import tkinter as tk
import psycopg2
from conexaoBD import database


class MeuPerfilPage:
    def __init__(self, master,id_user, id_user_logged, app):
        self.master = master
        self.id_user_logged = id_user_logged
        self.id_user = id_user
        self.app = app  
        self.app.title("Meu Perfil")
        self.change_password_window = None
        
        db = database()
        self.user = db.return_user(self.id_user)

        self.name = self.user[3]
        self.followers = self.user[1]
        self.following = self.user[2]
        self.country = self.user[7]
        self.email = self.user[4]

        user_info_label = tk.Label(self.app, text=f"Nome do Usuário: {self.name} \n Seguidores:{self.followers} \tSeguindo: {self.following} \n País {self.country} \nEmail {self.email}").pack()
        user_my_list = tk.Button(self.app, text="Minhas Listas").pack()
        if id_user_logged == id_user:
            user_alter_password = tk.Button(self.app, text="Alternar Senha", command=self.change_password).pack()

    def change_password(self):
        self.change_password_window = tk.Toplevel(self.app)
        self.change_password_window.geometry("300x150")
        self.change_password_window.title("Alterar Senha")
        
        password_label = tk.Label(self.change_password_window , text="Senha atual: ")
        password_label.pack()
        self.password_entry = tk.Entry(self.change_password_window , width=30, show="*")
        self.password_entry.pack()

        new_password_label = tk.Label(self.change_password_window , text="Nova senha: ")
        new_password_label.pack()
        self.new_password_entry = tk.Entry(self.change_password_window , width=30, show="*")
        self.new_password_entry.pack()

        self.new_password = self.new_password_entry.get()
        confirm_password_button = tk.Button(self.change_password_window, text="Confirmar Senha", command=self.confirm_password)
        confirm_password_button.pack()

    def confirm_password(self):
        password = self.password_entry.get()
        db = database()
        result = db.validate_password(self.id_user_logged, password)[0]
        if result is not None:
                db.update_password(self.id_user_logged, self.new_password_entry.get())
                tk.messagebox.showinfo("Nome do App", "OK")
                self.change_password_window.destroy()
        else:
                #PARA DEPOIS, SE A SENHA ATUAL NÃO ESTIVER CORRETA MOSTRAR MENSAGEM DE ERRO
                tk.messagebox.showerror("Nome do App", "Credenciais inválidas. Tente novamente.")
