from datetime import datetime, timedelta

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
        self.emprestimos = []

    def registrarEmprestimo(self, isbn, titulo, membro):
        emprestimo = Emprestimo(isbn, titulo, membro)
        self.emprestimos.append(emprestimo)
        return emprestimo

    def registrarDevolucao(self, emprestimo, dataDevolucao):
        emprestimo.registrarDevolucao(dataDevolucao)

    def livrosEmprestadosPorMembro(self, membro):
        return [e for e in self.emprestimos if e.membro == membro]

    def membrosQueEmprestaramLivro(self, titulo):
        return [e.membro for e in self.emprestimos if e.titulo == titulo]
    