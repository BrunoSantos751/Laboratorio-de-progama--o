import sqlite3 as sql

conexao = sql.connect('dados.bd')
cursor = conexao.cursor()

class Livro:
    def __init__(self, titulo, autor, anoPublicacao, genero, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.genero = genero
        self.ISBN = ISBN

    def cadastrarLivro(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS livros(titulo VARCHAR(255), autor VARCHAR(255), anoPublicacao INTEGER, genero VARCHAR(255), ISBN VARCHAR(13) UNIQUE)')
        inserir = 'INSERT INTO livros VALUES(?, ?, ?, ?, ?)'
        registros = (self.titulo, self.autor, self.anoPublicacao, self.genero, self.ISBN)
        cursor.execute(inserir, registros)
        conexao.commit()

    def deletarLivro(self, ISBN):
        cursor.execute('DELETE FROM livros WHERE ISBN = ?', (ISBN,))
        conexao.commit()

    @staticmethod
    def buscarLivro(ISBN):
        cursor.execute('SELECT * FROM livros WHERE ISBN = ?', (ISBN,))
        livro = cursor.fetchone()
        if livro:
            return {
                'titulo': livro[0],
                'autor': livro[1],
                'anoPublicacao': livro[2],
                'genero': livro[3],
                'ISBN': livro[4]
            }
        else:
            return None


livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia', 1234567890123)
livro1.cadastrarLivro()
    
livro_busca = Livro.buscarLivro('1234567890123')
if livro_busca:
    print(f"Livro encontrado: {livro_busca}")
else:
        print("Livro não encontrado.")
    
livro1.deletarLivro('1234567890123')
livro_busca = Livro.buscarLivro('1234567890123')
if livro_busca:
    print(f"Livro encontrado: {livro_busca}")
else:
    print("Livro não encontrado.")