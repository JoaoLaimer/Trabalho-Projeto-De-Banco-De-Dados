import tkinter as tk
import psycopg2

class database:
        def __init__(self, master=None):

            self.connection = psycopg2.connect(
                dbname="trabalhoPDB",
                user="postgres",
                password="271202",
                host="26.29.242.113",
                port="5432"
            )
            self.cursor = self.connection.cursor()
        def insert_newUser(self,nomeuser, emailuser, senhauser, telefoneuser, paisuser):
            consulta_sql = "INSERT INTO usuario(nomeuser, emailuser, senhauser, telefoneuser, paisuser) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(consulta_sql, (nomeuser, emailuser, senhauser, telefoneuser, paisuser))
            self.connection.commit()
            self.connection.close()

        def validate_login(self, username, password):
            consulta_sql = "SELECT * FROM usuario WHERE (nomeuser = %s OR emailuser = %s) AND senhauser = %s"
            self.cursor.execute(consulta_sql, (username, username, password)) 
            return self.cursor.fetchone()
        
        def return_user(self, id_user):
            print(id_user)
            consulta_sql = "SELECT * FROM usuario WHERE id_user = %s"
            self.cursor.execute(consulta_sql, (id_user,))
            return self.cursor.fetchone()
        
        def return_search(self, search_type, search_value): 
            
            if search_type == "Filme":
                self.table = "filme"
                search_type = "titulofilme"
            elif search_type == "Gênero":
                self.table = "filme"
                search_type = "generofilme"
            elif search_type == "Pais":
                self.table = "filme"
                search_type = "paisdeproducao"
            elif search_type == "Usuário":
                self.table = "usuario"
                search_type = "nomeuser"
            elif search_type == "Diretor":
                self.table = "diretor"
                search_type = "nomediretor"
            elif search_type == "Estudio":
                self.table = "estudio"
                search_type = "nome_estudio"

            consulta_sql = "SELECT * FROM " + self.table + " WHERE " + search_type + " = %s"
            self.cursor.execute(consulta_sql, (search_value,))
            return self.cursor.fetchone()
        
        def return_filme(self, id_type, id_any):
            if id_type == "Diretor":
                consulta_sql = "SELECT * FROM filme WHERE id_diretor = %s"
                self.cursor.execute(consulta_sql, (id_any,))
            if id_type == "Estudio":
                consulta_sql = "SELECT * FROM filme WHERE id_estudio = %s"
                self.cursor.execute(consulta_sql, (id_any,))
            else:
                consulta_sql = "SELECT * FROM filme WHERE id_filme = %s"
                self.cursor.execute(consulta_sql, (id_any,))
            return self.cursor.fetchall()
        
        def return_diretor(self, id_any):
            consulta_sql = "SELECT * FROM diretor WHERE id_diretor = %s"
            self.cursor.execute(consulta_sql, (id_any,))
            return self.cursor.fetchone()
        def return_estudio(self, id_any):
            consulta_sql = "SELECT * FROM estudio WHERE id_estudio = %s"
            self.cursor.execute(consulta_sql, (id_any,))
            return self.cursor.fetchone()
        
        def qntd_filmes(self, id_type, id_any):
            if id_type == "Diretor":
                consulta_sql = "SELECT COUNT(*) FROM filme WHERE id_diretor = %s"
                self.cursor.execute(consulta_sql, (id_any,))
            if id_type == "Estudio":
                consulta_sql = "SELECT COUNT(*) FROM filme WHERE id_estudio = %s"
                self.cursor.execute(consulta_sql, (id_any,))
            else:
                consulta_sql = "SELECT COUNT(*) FROM filme WHERE id_filme = %s"
                self.cursor.execute(consulta_sql, (id_any,))

            return self.cursor.fetchone()

        def validate_password(self, id_user, password):
            consulta_sql = "SELECT * FROM usuario WHERE id_user = %s AND senhauser = %s"
            self.cursor.execute(consulta_sql, (id_user, password))
            return self.cursor.fetchone()
        
        def update_password(self, id_user, new_password):
            consulta_sql = "UPDATE usuario SET senhauser = %s WHERE id_user = %s"
            self.cursor.execute(consulta_sql, (new_password, id_user))
            self.connection.commit()
            self.connection.close()

        def check_total_user_lists(self, id_user):
            consulta_sql = "SELECT COUNT(*) FROM lista WHERE id_user = %s"
            self.cursor.execute(consulta_sql, (id_user,))
            return self.cursor.fetchone()
        
        def create_new_list(self, id_user, list_name):
            consulta_sql = "INSERT INTO lista(id_user, nomelista) VALUES (%s, %s)"
            self.cursor.execute(consulta_sql, (id_user, list_name))
            self.connection.commit()
            self.connection.close()

        def return_user_lists(self, id_user):
            consulta_sql = "SELECT * FROM lista WHERE id_user = %s"
            self.cursor.execute(consulta_sql, (id_user,))
            return self.cursor.fetchall()
        
        def return_movies_in_list(self, id_list):
            consulta_sql = "SELECT id_filme FROM pertence_lista WHERE id_lista = %s"
            self.cursor.execute(consulta_sql, (id_list,))
            return self.cursor.fetchall()
        
        def get_movie_name(self, id_movie):
            consulta_sql = "SELECT titulofilme FROM filme WHERE id_filme = %s"
            self.cursor.execute(consulta_sql, (id_movie,))
            return self.cursor.fetchone()
        
        def get_user_id(self, username):
            consulta_sql = "SELECT id_user FROM usuario WHERE nomeuser = %s"
            self.cursor.execute(consulta_sql, (username,))
            return self.cursor.fetchone()
        