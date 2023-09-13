import tkinter as tk
import psycopg2

class app:
    def __init__(self, master=None):

        self.cidname_entry = tk.Entry(master)
        self.siglauf_entry = tk.Entry(master)

        cidname_label = tk.Label(master, text="Nome da Cidade")
        cidname_label.pack()
        self.cidname_entry.pack()

        siglauf_label = tk.Label(master, text="Sigla do Estado")
        siglauf_label.pack()
        self.siglauf_entry.pack()

        insert_button = tk.Button(master, text="Insert", command=self.insert_data)
        insert_button.pack()

    def test_button(self):
        cidname_value = self.cidname_entry.get()
        siglauf_value = self.siglauf_entry.get()
        self.cidname_entry.delete(0, tk.END)
        self.siglauf_entry.delete(0, tk.END)

    def insert_data(self): 

        cidnome = self.cidname_entry.get()
        siglauf = self.siglauf_entry.get()

        connection = psycopg2.connect(
            dbname="lista5",
            user="postgres",
            password="271202",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        cursor.execute("INSERT INTO cidade(nomcid, siglauf) VALUES (%s, %s)", (cidnome, siglauf))

        connection.commit()
        connection.close()

        self.cidname_entry.delete(0, tk.END)
        self.siglauf_entry.delete(0, tk.END)



root = tk.Tk()
root.title("Banco de Dados")
app(root)
root.mainloop()
