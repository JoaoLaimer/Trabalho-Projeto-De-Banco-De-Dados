import tkinter as tk
import psycopg2

class database:
        def __init__(self, master=None):

            self.connection = psycopg2.connect(
                dbname="lista5",
                user="postgres",
                password="271202",
                host="localhost",
                port="5432"
            )

            self.cursor = self.connection.cursor()