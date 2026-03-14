import tkinter as tk
from tkinter import messagebox
import sqlite3
from utils import centralizar

def verificar_login(user, senha):

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT perfil FROM usuarios
    WHERE username=? AND senha=?
    """,(user,senha))

    resultado = cursor.fetchone()
    conn.close()

    return resultado


def tela_login(abrir_menu):

    janela = tk.Tk()
    janela.title("Login")

    centralizar(janela,300,200)
    janela.resizable(False,False)

    tk.Label(janela,text="Usuário").pack(pady=5)
    usuario = tk.Entry(janela)
    usuario.pack()

    tk.Label(janela,text="Senha").pack(pady=5)
    senha = tk.Entry(janela,show="*")
    senha.pack()

    def logar():

        resultado = verificar_login(usuario.get(),senha.get())

        if resultado:
            perfil = resultado[0]
            janela.destroy()
            abrir_menu(perfil)

        else:
            messagebox.showerror("Erro","Login inválido")

    tk.Button(janela,text="Entrar",command=logar).pack(pady=15)

    janela.mainloop()