from datetime import date
import sqlite3 as sql
import logicadeNegocio

conexao = sql.connect('dados.bd')
cursor = conexao.cursor()

dataAtual = date.today()
dataTexto = '{}/{}/{}'.format(dataAtual.day, dataAtual.month, dataAtual.year)
class Emprestimo:
    """
    emprestimo dos livros na biblioteca
    """


    def __init__(self, isbn, titulo, membro, dataDevolucaoPrevista):
        self.isbn = isbn
        self.titulo = titulo
        self.membro = membro
        self.dataEmprestimo = dataTexto  # data e hora atuais como data de emprestimo
        self.dataDevolucaoPrevista = dataDevolucaoPrevista  # data de devolução pra daqui 7 dias

    def registrarEmprestimo(self):
        if logicadeNegocio.condicionalEmprestimo(self.membro):
            cursor.execute('CREATE TABLE IF NOT EXISTS emprestimos(ISBN INTEGER UNIQUE, titulo VARCHAR(255), membro VARCHAR(255), dataEmprestimo DATE, dataDevolucaoPrevista VARCHAR(255))')
            inserir = 'INSERT INTO emprestimos VALUES(?, ?, ?, ?, ?)'
            regitros = (self.isbn, self.titulo, self.membro, self.dataEmprestimo, self.dataDevolucaoPrevista)
            cursor.execute(inserir, regitros)
            conexao.commit()
            return True
        else:
            return False

    def registrarDevolucao(self):
        inserir = 'DELETE FROM emprestimos WHERE isbn = (' + str(self.isbn) + ")" 
        cursor.execute(inserir)
        conexao.commit()


