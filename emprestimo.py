from datetime import datetime, timedelta
import sqlite3

class Emprestimo:
    """
    emprestimo dos livros na biblioteca
    """

    def __init__(self, isbn, titulo, membro):
        self.isbn = isbn
        self.titulo = titulo
        self.membro = membro
        self.dataEmprestimo = datetime.now()  # data e hora atuais como data de emprestimo
        self.dataDevolucaoPrevista = self.dataEmprestimo + timedelta(days=7)  # data de devolução pra daqui 7 dias
        self.dataDevolucao = None
    
    def registrarDevolucao(self, dataDevolucao):
        self.dataDevolucao = dataDevolucao
    
    def __str__(self):
        status = "Devolvido" if self.dataDevolucao else "Pendente"
        return f"{self.titulo} emprestado para {self.membro} ({status})"


class Biblioteca:
    """
    gerencia os empréstimos dos livros na biblioteca
    """

    def __init__(self):
        self.conn = sqlite3.connect('biblioteca.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Cria a tabela 'emprestimos' no banco de dados se ela não existir.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn TEXT,
                titulo TEXT,
                membro TEXT,
                data_emprestimo TEXT,
                data_devolucao_prevista TEXT,
                data_devolucao TEXT
            )
        ''')
        self.conn.commit()

    def registrarEmprestimo(self, isbn, titulo, membro):
        emprestimo = Emprestimo(isbn, titulo, membro)
        if emprestimo.condicionalEmprestimo():
            self.cursor.execute('''
                INSERT INTO emprestimos (isbn, titulo, membro, data_emprestimo, data_devolucao_prevista, data_devolucao)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (emprestimo.isbn, emprestimo.titulo, emprestimo.membro, emprestimo.dataEmprestimo, emprestimo.dataDevolucaoPrevista, emprestimo.dataDevolucao))
            self.conn.commit()
            return emprestimo
        else:
            return False

    def registrarDevolucao(self, emprestimo, dataDevolucao):
        emprestimo.registrarDevolucao(dataDevolucao)
        self.cursor.execute('''
            UPDATE emprestimos SET data_devolucao = ? WHERE id = ?
        ''', (dataDevolucao, emprestimo.id))
        self.conn.commit()

    def livrosEmprestadosPorMembro(self, membro):
        self.cursor.execute('''
            SELECT * FROM emprestimos WHERE membro = ?
        ''', (membro,))
        emprestimos = self.cursor.fetchall()
        return emprestimos

    def membrosQueEmprestaramLivro(self, titulo):
        self.cursor.execute('''
            SELECT DISTINCT membro FROM emprestimos WHERE titulo = ?
        ''', (titulo,))
        membros = self.cursor.fetchall()
        return [m[0] for m in membros]

    def close(self):
        self.conn.close()
    