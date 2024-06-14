import sqlite3 as sql

conexao = sql.connect('dados.bd')
cursor = conexao.cursor()

#criando classe 
class Livro:
    def __init__(self, ISBN, titulo, autor, anoPublicacao, genero):

        #Atributos da classe
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.genero = genero
        

    #Metodos da classe
    def cadastrarLivro(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS livros(ISBN INTEGER UNIQUE, titulo VARCHAR(255), autor VARCHAR(255), anoPublicacao DATE, genero VARCHAR(255))')
        inserir = 'INSERT INTO livros VALUES(?, ?, ?, ?, ?)'
        registros = (self.ISBN, self.titulo, self.autor, self.anoPublicacao, self.genero)
        cursor.execute(inserir, registros)
        conexao.commit()

    def deletarLivro(self):
        inserir = 'DELETE FROM livros WHERE isbn = (' + str(self.ISBN) + ")" 
        print (inserir)
        cursor.execute(inserir)
        conexao.commit()