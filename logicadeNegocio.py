import sqlite3 as sql
import membros
import livros
#Regra de negocio
#consultar livros disponiveis
#devolucao (remover livros do ephrem)

conexao = sql.connect('dados.bd')
cursor= conexao.cursor()

#criando nova tabela para livros disponiveis
def disponiveis():
    cursor.execute('Select * from livros where ISBN not in (select ISBN from emprestimos )')
    disponiveis= cursor.fetchall()
    return (disponiveis)


#criando a condicional da regra de negocio:
def condicionalEmprestimo(x):
    comando = ('SELECT membro, COUNT(membro)  FROM emprestimos where membro ='  + '"' + x + '"')
    cursor.execute(comando)
    x,condicional= (cursor.fetchall()[0])
    if condicional < 3:
        return True
    else:
        return False

def select(x):
    comando = 'SELECT * from ' + x
    cursor.execute(comando)
    a=cursor.fetchall()
    return (a)


#membro1= membros.membro( 10, "fabao","14/06", "perto do aeroporto" )
#print (membro1)
#membro1.cadastrarMembro()
#select()

#livro1= livros.Livro(3, 'teste', 'teste', '20/05','acao')
#livro1.cadastrarLivro()
#print(livro1.ISBN)
#livro1.deletarLivro()

