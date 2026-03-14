import tkinter as tk
from database import criar_tabelas, criar_admin
from login import tela_login
from produtos import tela_produtos
from usuarios import tela_usuarios
from utils import centralizar

criar_tabelas()
criar_admin()

def abrir_menu(perfil):

    janela = tk.Tk()
    janela.title("Sistema de Estoque")

    centralizar(janela,400,300)
    janela.resizable(False,False)

    tk.Label(janela,text=f"Perfil: {perfil}",font=("Arial",12)).pack(pady=10)

    tk.Button(janela,text="Produtos",width=20,command=tela_produtos).pack(pady=5)

    if perfil == "admin":
        tk.Button(janela,text="Cadastrar Usuário",width=20,command=tela_usuarios).pack(pady=5)

    def logout():

        janela.destroy()
        tela_login(abrir_menu)

    tk.Button(janela,text="Logout",width=20,command=logout).pack(pady=20)

    janela.mainloop()

tela_login(abrir_menu)