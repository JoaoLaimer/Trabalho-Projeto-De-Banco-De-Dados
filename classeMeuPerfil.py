import tkinter as tk
import psycopg2
from conexaoBD import database
import customtkinter


class MeuPerfilPage:
    def __init__(self, master, id_user, id_user_logged, app):
        self.master = master
        self.master.geometry("320x400")
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
        
        nome = tk.StringVar(value=f"Nome do Usuário")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=nome,
                                       width=120,
                                       height=25,
                                       fg_color=("white", "gray75"),
                                       corner_radius=3)
        label.grid(row=1, column=0, padx=10, pady=10)
        
        nome_id = tk.StringVar(value=f"{self.name}")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=nome_id,
                                       width=120,
                                       height=25,
                                       fg_color=("silver", "gray75"),
                                       corner_radius=3)
        label.grid(row=1, column=1, padx=10, pady=10)
        
        seguidores = tk.StringVar(value=f"Seguidores")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=seguidores,
                                       width=120,
                                       height=25,
                                       fg_color=("white", "gray75"),
                                       corner_radius=3)
        label.grid(row=2, column=0, padx=10, pady=10)
        
        seguidores_id = tk.StringVar(value=f"{self.followers} Usuário(s)")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=seguidores_id,
                                       width=120,
                                       height=25,
                                       fg_color=("silver", "gray75"),
                                       corner_radius=3)
        label.grid(row=2, column=1, padx=10, pady=10)
        
        seguindo = tk.StringVar(value=f"Seguindo")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=seguindo,
                                       width=120,
                                       height=25,
                                       fg_color=("white", "gray75"),
                                       corner_radius=3)
        label.grid(row=3, column=0, padx=10, pady=10)
        
        seguindo_id = tk.StringVar(value=f"{self.following} Usuário(s)")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=seguindo_id,
                                       width=120,
                                       height=25,
                                       fg_color=("silver", "gray75"),
                                       corner_radius=3)
        label.grid(row=3, column=1, padx=10, pady=10)
        
        pais = tk.StringVar(value=f"País")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=pais,
                                       width=120,
                                       height=25,
                                       fg_color=("white", "gray75"),
                                       corner_radius=3)
        label.grid(row=4, column=0, padx=10, pady=10)
        
        pais_id = tk.StringVar(value=f"{self.country}")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=pais_id,
                                       width=120,
                                       height=25,
                                       fg_color=("silver", "gray75"),
                                       corner_radius=3)
        label.grid(row=4, column=1, padx=10, pady=10)
        
        email = tk.StringVar(value=f"E-mail:")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=email,
                                       width=120,
                                       height=25,
                                       fg_color=("white", "gray75"),
                                       corner_radius=3)
        label.grid(row=5, column=0, padx=10, pady=10)
        
        email_id = tk.StringVar(value=f"{self.email}")
        label = customtkinter.CTkLabel(self.app,
                                       textvariable=email_id,
                                       width=120,
                                       height=25,
                                       fg_color=("silver", "gray75"),
                                       corner_radius=3)
        label.grid(row=5, column=1, padx=10, pady=10)



        
        if id_user_logged == id_user: 
            user_my_list = customtkinter.CTkButton(self.app, text="Lista de Filmes", command=lambda: self.master.exibir_lista_filmes(id_user, True))
            user_my_list.grid(row=6, column=0, padx=10, pady=10)
            user_alter_password = customtkinter.CTkButton(self.app, text="Alternar Senha", command=self.change_password)
            user_alter_password.grid(row=6, column=1, padx=10, pady=10)
        else:
            user_my_list = customtkinter.CTkButton(self.app, text="Lista de Filmes", command=lambda: self.master.exibir_lista_filmes(id_user, False))
            user_my_list.grid(row=6, column=0, padx=10, pady=10)

            if db.check_follow(self.id_user_logged, self.id_user):
                self.user_follow = customtkinter.CTkButton(self.app, text="Deixar de Seguir", command=lambda: self.unfollow_user(id_user))
                self.user_follow.grid(row=6, column=1, padx=10, pady=10)
            else:
                self.user_follow = customtkinter.CTkButton(self.app, text="Seguir", command=lambda: self.follow_user(id_user))
                self.user_follow.grid(row=6, column=1, padx=10, pady=10)
                

    def change_password(self):
        self.change_password_window = tk.Toplevel(self.app)
        self.change_password_window.geometry("300x150")
        self.change_password_window.title("Alterar Senha")
        
        password_label = customtkinter.CTkLabel(self.change_password_window, text="Senha atual")
        password_label.grid(row=0, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.change_password_window , width=30, show="*")
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)

        new_password_label = customtkinter.CTkLabel(self.change_password_window, text="Nova senha")
        new_password_label.grid(row=1, column=0, padx=10, pady=10)
        self.new_password_entry = tk.Entry(self.change_password_window , width=30, show="*")
        self.new_password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.new_password = self.new_password_entry.get()
        confirm_password_button = customtkinter.CTkButton(self.change_password_window, text="Confirmar Senha", command=self.confirm_password)
        confirm_password_button.grid(row=2, columnspan=2, padx=10, pady=10)

    def confirm_password(self):
        current_password = self.password_entry.get()
        new_password = self.new_password_entry.get()
        
        if current_password == new_password:
            tk.messagebox.showerror("Nome do App", "A nova senha não pode ser igual à senha atual.")
        else:
            db = database()
            result = db.validate_password(self.id_user_logged, current_password)[0]
            if result is not None:
                db.update_password(self.id_user_logged, new_password)
                tk.messagebox.showinfo("Nome do App", "Senha atualizada com sucesso.")
                self.change_password_window.destroy()
            else:
                tk.messagebox.showerror("Nome do App", "Credenciais inválidas. Tente novamente.")
            db.connection.close()

    def follow_user(self, id_user):
        db = database()
        db.follow_user(self.id_user_logged, id_user)
        tk.messagebox.showinfo("Nome do App", "Usuário seguido com sucesso.")
        self.user_follow.grid_remove()
        self.user_follow = customtkinter.CTkButton(self.app, text="Deixar de Seguir", command=lambda: self.unfollow_user(id_user))
        self.user_follow.grid(row=6, column=1, padx=10, pady=10)
        db.connection.close()
    
    def unfollow_user(self, id_user):
        db = database()
        db.unfollow_user(self.id_user_logged, id_user)
        tk.messagebox.showinfo("Nome do App", "Usuário deixado de seguir com sucesso.")
        self.user_follow.grid_remove()
        self.user_follow = customtkinter.CTkButton(self.app, text="Seguir", command=lambda: self.follow_user(id_user))
        self.user_follow.grid(row=6, column=1, padx=10, pady=10)
        db.connection.close()

