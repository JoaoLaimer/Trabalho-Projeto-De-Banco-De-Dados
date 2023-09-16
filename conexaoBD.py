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
        
        def validate_password(self, id_user, password):
            consulta_sql = "SELECT * FROM usuario WHERE id_user = %s AND senhauser = %s"
            self.cursor.execute(consulta_sql, (id_user, password))
            return self.cursor.fetchone()
        
        def update_password (self, id_user, new_password):
            consulta_sql = "UPDATE usuario SET senhauser = %s WHERE id_user = %s"
            self.cursor.execute(consulta_sql, (new_password, id_user))
            self.connection.commit()
            self.connection.close()