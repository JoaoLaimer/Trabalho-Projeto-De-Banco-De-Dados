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
            elif search_type == "Ator":
                self.table = "ator"
                search_type = "nomeator"
                consulta_sql = "SELECT * FROM filme JOIN atua on filme.id_filme = atua.id_filme JOIN ator on atua.id_ator = ator.id_ator WHERE ator.nomeator = %s"
                self.cursor.execute(consulta_sql, (search_value,))
                return self.cursor.fetchall()
            elif search_type == "Ano":
                self.table = "filme"
                search_type = "datalancamento"
                consulta_sql = "SELECT * FROM filme WHERE EXTRACT( YEAR FROM datalancamento) = %s"
                self.cursor.execute(consulta_sql, (search_value,))
                return self.cursor.fetchall()

            consulta_sql = "SELECT * FROM " + self.table + " WHERE " + search_type + " = %s"
            self.cursor.execute(consulta_sql, (search_value,))
            return self.cursor.fetchall()
        
        def return_filme(self, id_type, id_any):
            if id_type == "Diretor":
                consulta_sql = "SELECT * FROM filme WHERE id_diretor = %s"
                self.cursor.execute(consulta_sql, (id_any,))
                return self.cursor.fetchall()
            if id_type == "Estudio":
                consulta_sql = "SELECT * FROM filme WHERE id_estudio = %s"
                self.cursor.execute(consulta_sql, (id_any,))
                return self.cursor.fetchall()
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
                return self.cursor.fetchone()
            elif id_type == "Estudio":
                consulta_sql = "SELECT COUNT(*) FROM filme WHERE id_estudio = %s"
                self.cursor.execute(consulta_sql, (id_any,))
                return self.cursor.fetchone()
            elif id_type == "Gênero":
                consulta_sql = "SELECT COUNT(*) FROM filme WHERE generofilme = %s"
                self.cursor.execute(consulta_sql, (id_any,))
                return self.cursor.fetchone()
            elif id_type == "Ator":
                consulta_sql = "SELECT COUNT(*) FROM filme JOIN atua on filme.id_filme = atua.id_filme JOIN ator on atua.id_ator = ator.id_ator WHERE ator.nomeator = %s"
                self.cursor.execute(consulta_sql, (id_any,))
                return self.cursor.fetchone()
            elif id_type == "Ano":
                consulta_sql = "SELECT COUNT(*) FROM filme WHERE EXTRACT(YEAR FROM datalancamento) = %s"
                self.cursor.execute(consulta_sql, (id_any,))
                return self.cursor.fetchone()
            else:
                consulta_sql = "SELECT COUNT(*) FROM filme WHERE titulofilme = %s OR generofilme = %s OR paisdeproducao = %s"
                self.cursor.execute(consulta_sql, (id_any,id_any,id_any,))
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
        
        def get_list_name(self, id_list):
            consulta_sql = "SELECT nomelista FROM lista WHERE id_lista = %s"
            self.cursor.execute(consulta_sql, (id_list,))
            return self.cursor.fetchone()
        
        def get_user_id(self, username):
            consulta_sql = "SELECT id_user FROM usuario WHERE nomeuser = %s"
            self.cursor.execute(consulta_sql, (username,))
            return self.cursor.fetchone()
        
        def insert_movie(self, id_list, id_movie):
            consulta_sql = "INSERT INTO pertence_lista(id_lista, id_filme) VALUES (%s, %s)"
            self.cursor.execute(consulta_sql, (id_list, id_movie))
            self.connection.commit()
            self.connection.close()

        def like_list(self, id_list, id_user):
            consulta_sql = "INSERT INTO curtir_lista(id_user, id_lista) VALUES (%s, %s)"
            self.cursor.execute(consulta_sql, (id_user, id_list))
            self.connection.commit()
            self.connection.close()

        def unlike_list(self, id_list, id_user):
            consulta_sql = "DELETE FROM curtir_lista WHERE id_user = %s AND id_lista = %s"
            self.cursor.execute(consulta_sql, (id_user, id_list))
            self.connection.commit()
            self.connection.close()

        def return_liked_lists(self, id_user):
            consulta_sql = "SELECT id_lista FROM curtir_lista WHERE id_user = %s"
            self.cursor.execute(consulta_sql, (id_user,))
            return self.cursor.fetchall()
        
        def check_like(self, id_list, id_user):
            consulta_sql = "SELECT * FROM curtir_lista WHERE id_user = %s AND id_lista = %s"
            self.cursor.execute(consulta_sql, (id_user, id_list))
            return self.cursor.fetchone()
        
        def follow_user(self, id_user, id_followed):
                consulta_sql = "INSERT INTO seguir(id_user_seguidor, id_user_seguido) VALUES (%s, %s)"
                self.cursor.execute(consulta_sql, (id_user, id_followed))
                self.connection.commit()
                self.connection.close()

        def unfollow_user(self, id_user, id_followed):
            consulta_sql = "DELETE FROM seguir WHERE id_user_seguidor = %s AND id_user_seguido = %s"
            self.cursor.execute(consulta_sql, (id_user, id_followed))
            self.connection.commit()
            self.connection.close()

        def check_follow(self, id_user, id_followed):
            consulta_sql = "SELECT * FROM seguir WHERE id_user_seguidor = %s AND id_user_seguido = %s"
            self.cursor.execute(consulta_sql, (id_user, id_followed))
            return self.cursor.fetchone()
        
        def add_movie_to_list(self, id_filme, id_list):
            consulta_sql = "INSERT INTO pertence_lista(id_filme, id_lista) VALUES (%s, %s)"
            try:
                self.cursor.execute(consulta_sql, (id_filme, id_list))
            except psycopg2.IntegrityError:
                self.connection.rollback()
                return False
            
            self.connection.commit()
            self.connection.close()
            return True

        def insert_review(self,id_filme,id_user,nota,review):
            if(review == ""):
                review = None

            consulta_sql = "INSERT INTO review(id_filme,id_user,nota,texto_review) VALUES (%s,%s,%s,%s)"

            consulta_sql2= "UPDATE review SET nota = %s,texto_review = %s WHERE id_filme = %s AND id_user = %s"
            try:
                self.cursor.execute(consulta_sql, (id_filme, id_user, nota, review))
            except psycopg2.IntegrityError:
                self.connection.rollback()
                self.cursor.execute(consulta_sql2, (nota, review, id_filme, id_user))
            finally:
                self.connection.commit()
                self.connection.close()


        def delete_list(self, id_list):
            consula_sql = "SELECT * FROM lista WHERE id_lista = %s"
            self.cursor.execute(consula_sql, (id_list,))
            if self.cursor.fetchone() is not None:
                consulta_sql = "DELETE FROM lista WHERE id_lista = %s "
                self.cursor.execute(consulta_sql, (id_list,))
                self.connection.commit()
                self.connection.close()

        def delete_movie(self, id_movie, id_list):
            consulta_sql = ("DELETE FROM pertence_lista WHERE id_filme = %s AND id_lista = %s")
            self.cursor.execute(consulta_sql, (id_movie, id_list))
            self.connection.commit()
            self.connection.close()

        def return_review_by_user(self, id_user):
            consulta_sql = ("SELECT usuario.nomeuser, filme.titulofilme, review.nota, review.texto_review FROM review JOIN usuario on review.id_user = usuario.id_user JOIN filme on review.id_filme = filme.id_filme WHERE usuario.id_user = %s")
            self.cursor.execute(consulta_sql, (id_user,))
            return self.cursor.fetchall()
