import sqlite3 as sql

conexao = sql.connect('dados.bd')
cursor= conexao.cursor()

comando = 'CREATE TABLE if not exists livros (ISBN INTEGER PRIMARY KEY, TITULO VARCHAR(255), AUTOR VARCHAR(255), anoPublicação INTEGER, genero VARCHAR (255) )'
cursor.execute(comando)

comando = 'CREATE TABLE if not exists emprestimos (ISBN INTEGER PRIMARY KEY, TITULO VARCHAR(255), Membro VARCHAR(255), dataEmprestimo DATE, dataDevolucao date )'
cursor.execute(comando)

def select():
    comando = 'SELECT * from emprestimos'
    cursor.execute(comando)
    a=cursor.fetchall()
    print (a)

def insert():
    inserir = 'insert into emprestimos values(?, ?, ?, ?, ?)'
    regitros = (4, "teste4 ", "andre", 2024, "acao" )
    cursor.execute(inserir, regitros)
    conexao.commit()

#select()