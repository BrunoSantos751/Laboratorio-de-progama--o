import sqlite3 as sqlite3


conexao = sqlite3.connect('dados.bd')
cursor= conexao.cursor()

#criando classe membro
class membro():
    def __init__(self, ID, nome, dataNascimento, endereco ):
        
        #Atributos da classe
        self.ID = ID
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.endereco = endereco
    
    #Metodos da classe
    def cadastrarMembro(self):
        cursor.execute('CREATE TABLE if not exists membros(ID integer unique, nome VARCHAR(255), dataNascimento DATE, endereco VARCHAR(255))')
        inserir = 'insert into membros values(?, ?, ?, ?)'
        regitros = (self.ID, self.nome, self.dataNascimento, self.endereco )
        print (regitros)
        cursor.execute(inserir, regitros)
        conexao.commit()
















#comando = 'CREATE TABLE livros (ISBN INTEGER PRIMARY KEY, TITULO VARCHAR(255), AUTOR VARCHAR(255), ano_de_publicação INTEGER, gênero VARCHAR (255) )'
#cursor.execute(comando)

def select():
    comando = 'SELECT * from membros'
    cursor.execute(comando)
    a=cursor.fetchall()
    print (a)

def insert():
    inserir = 'insert into livros values(?, ?, ?, ?, ?)'
    regitros = (4, "pizzas ", "andre", 2024,"" )
    cursor.execute(inserir, regitros)
    conexao.commit()

#select()
