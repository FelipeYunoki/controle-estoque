import tkinter as tk
from tkinter import messagebox
import sqlite3
from utils import centralizar

def tela_usuarios():

    janela = tk.Toplevel()
    janela.title("Cadastrar Usuário")

    centralizar(janela,350,250)
    janela.resizable(False,False)

    tk.Label(janela,text="Usuário").pack()
    user = tk.Entry(janela)
    user.pack()

    tk.Label(janela,text="Senha").pack()
    senha = tk.Entry(janela)
    senha.pack()

    tk.Label(janela,text="Perfil (admin/comum)").pack()
    perfil = tk.Entry(janela)
    perfil.pack()

    def cadastrar():

        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        try:

            cursor.execute("""
            INSERT INTO usuarios(username,senha,perfil)
            VALUES(?,?,?)
            """,(user.get(),senha.get(),perfil.get()))

            conn.commit()

            messagebox.showinfo("Sucesso","Usuário criado")

        except:
            messagebox.showerror("Erro","Usuário já existe")

        conn.close()

    tk.Button(janela,text="Cadastrar",command=cadastrar).pack(pady=10)