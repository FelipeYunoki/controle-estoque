import tkinter as tk
from tkinter import messagebox
import sqlite3
from utils import centralizar

def atualizar_lista(lista):

    lista.delete(0, tk.END)

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")

    for p in cursor.fetchall():

        texto = f"{p[0]} - {p[1]} | Estoque: {p[2]}"

        if p[2] <= p[3]:
            texto += " ⚠ ESTOQUE BAIXO"

        lista.insert(tk.END, texto)

    conn.close()


def tela_produtos():

    janela = tk.Toplevel()
    janela.title("Controle de Produtos")

    centralizar(janela,600,500)
    janela.resizable(False,False)

    lista = tk.Listbox(janela,width=50)
    lista.pack(pady=10)

    atualizar_lista(lista)

    frame = tk.Frame(janela)
    frame.pack(pady=10)

    tk.Label(frame,text="Nome").grid(row=0,column=0)
    nome = tk.Entry(frame)
    nome.grid(row=0,column=1)

    tk.Label(frame,text="Quantidade Inicial").grid(row=1,column=0)
    quantidade = tk.Entry(frame)
    quantidade.grid(row=1,column=1)

    tk.Label(frame,text="Estoque mínimo").grid(row=2,column=0)
    minimo = tk.Entry(frame)
    minimo.grid(row=2,column=1)

    def cadastrar():

        if not quantidade.get().isdigit():
            messagebox.showerror("Erro","Quantidade deve ser número")
            return

        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO produtos(nome,quantidade,minimo)
        VALUES(?,?,?)
        """,(nome.get(),quantidade.get(),minimo.get()))

        conn.commit()
        conn.close()

        atualizar_lista(lista)

    tk.Button(frame,text="Cadastrar Produto",command=cadastrar).grid(row=3,columnspan=2,pady=5)

    tk.Label(janela,text="Quantidade para movimentação").pack()

    mover = tk.Entry(janela)
    mover.pack()

    def entrada():

        if not mover.get().isdigit():
            messagebox.showerror("Erro","Digite um número")
            return

        selecionado = lista.get(tk.ACTIVE)

        if not selecionado:
            messagebox.showerror("Erro","Selecione um produto")
            return

        id_produto = selecionado.split(" - ")[0]

        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE id=?
        """,(mover.get(),id_produto))

        conn.commit()
        conn.close()

        atualizar_lista(lista)

    def saida():

        if not mover.get().isdigit():
            messagebox.showerror("Erro","Digite um número")
            return

        selecionado = lista.get(tk.ACTIVE)

        if not selecionado:
            messagebox.showerror("Erro","Selecione um produto")
            return

        id_produto = selecionado.split(" - ")[0]

        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade - ?
        WHERE id=?
        """,(mover.get(),id_produto))

        conn.commit()
        conn.close()

        atualizar_lista(lista)

    def excluir():

        selecionado = lista.get(tk.ACTIVE)

        if not selecionado:
            messagebox.showerror("Erro","Selecione um produto")
            return

        confirmar = messagebox.askyesno("Confirmar","Deseja excluir este produto?")

        if confirmar:

            id_produto = selecionado.split(" - ")[0]

            conn = sqlite3.connect("estoque.db")
            cursor = conn.cursor()

            cursor.execute("DELETE FROM produtos WHERE id=?",(id_produto,))

            conn.commit()
            conn.close()

            atualizar_lista(lista)

    tk.Button(janela,text="Adicionar ao Estoque",command=entrada).pack(pady=5)
    tk.Button(janela,text="Retirar do Estoque",command=saida).pack(pady=5)
    tk.Button(janela,text="Excluir Produto",command=excluir).pack(pady=5)