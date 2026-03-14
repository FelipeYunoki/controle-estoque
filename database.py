import sqlite3

def conectar():
    return sqlite3.connect("estoque.db")

def criar_tabelas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        senha TEXT,
        perfil TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        quantidade INTEGER,
        minimo INTEGER
    )
    """)

    conn.commit()
    conn.close()

def criar_admin():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE username='admin'")

    if not cursor.fetchone():
        cursor.execute("""
        INSERT INTO usuarios(username,senha,perfil)
        VALUES('admin','123','admin')
        """)

    conn.commit()
    conn.close()