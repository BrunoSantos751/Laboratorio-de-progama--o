import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from tkinter import *
from ttkbootstrap.constants import *
import logicadeNegocio
import livros
import membros

def controle():
    pass

#Criando janela
root = ttk.Window(themename="darkly")
root.title("Biblioteca de Serra-Leoa")
root.geometry('400x350')

#Criando estilo
my_style = ttk.Style()
my_style.configure('info.TButton', font=('Roboto', 15))

my_style = ttk.Style()
my_style.configure('success.TButton', font=('Roboto', 10))

my_style = ttk.Style()
my_style.configure('light.Outline.TButton', font=('Roboto', 15))



#funções uteis
def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

def createButton(x,y,z):
    b=ttk.Button(root, text=x, style='info.TButton', width=18, command= z)
    b.pack(pady=y)

def menu_button(x):
    back = ttk.Button(root, text="Voltar", style='info.Tbutton', command= x)
    back.place(x=10, y=10)

def operacaoConcluida():#confirmar que o codigo foi executado e retornar para o menu
    clear_widgets()
    label=ttk.Label(root, text='Operação concluida', font= ('Roboto', 20))
    label.pack( pady=50)
    back = ttk.Button(root, text="Voltar", style='info.Outline.Tbutton', command=mainMenu)
    back.pack(pady=10)


def dataList(x):
    getList = logicadeNegocio.select(x)
    # A função fetchall() retorna uma lista de tuplas, precisamos extrair os valores de dentro das tuplas
    list = [str(item[0]) +' - '+ str(item[1]) for item in getList]
    return (list) 

def telaLivros():
    clear_widgets()
    menu_button(mainMenu)
    root.geometry('400x350')
    label=ttk.Label(root, text='Escolha uma opção:', font= ('Roboto', 15))
    label.pack(padx= 30, pady=20)
    createButton('Consultar livros', 10, consultarLivro)
    createButton('Adicionar livros', 10, addLivros)
    createButton('Remover livros', 10, removerLivros)

def consultarLivro():
    clear_widgets()
    root.geometry('600x350')
    label=ttk.Label(root, text='              Verifique a sua tabela a baixo:', font= ('Roboto', 15))
    label.pack( pady=5)
   
    menu_button(telaLivros)
    colors = root.style.colors
    columns = [
        {"text": "ISBN", "stretch": True},
        {"text": "TITULO", "stretch": True},
        {"text": "AUTOR", "stretch": True},
        {"text": "Ano_de_publicação", "stretch": True},
        {"text": "Gênero", "stretch": True}
    ]

    row_data = logicadeNegocio.select('livros')
    table = Tableview(
        master=root,
        coldata=columns,
        rowdata=row_data,
        paginated=True,
        autofit=True,
        searchable=True,
        bootstyle=INFO,
        stripecolor=(colors.light)
    )

    table.pack(fill=BOTH, expand=YES, padx=10, pady=10)

def addLivros():
    clear_widgets()
    menu_button(telaLivros)
    root.geometry('400x350')

    label=ttk.Label(root, text='Após preencher clique:', font= ('Roboto', 15))
    label.pack(padx= 30, pady=10)

    label=ttk.Label(root, text='ISBN:', font= ('Roboto', 10))
    label.pack(pady=2)
    ISBN= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    ISBN.pack(pady=2)

    label2=ttk.Label(root, text='Titulo:', font= ('Roboto', 10))
    label2.pack(pady=2)
    Titulo= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    Titulo.pack(pady=2)

    label3=ttk.Label(root, text='Autor:', font= ('Roboto', 10))
    label3.pack(pady=2)
    Autor= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    Autor.pack(pady=2)

    label4=ttk.Label(root, text='Ano de pulicação:', font= ('Roboto', 10))
    label4.pack(pady=2)
    anoPulicacao= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    anoPulicacao.pack(pady=2)

    label5=ttk.Label(root, text='genero:', font= ('Roboto', 10))
    label5.pack(pady=2)
    genero= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    genero.pack(pady=2)

    b=ttk.Button(root, text='confirmar', style='success.TButton', command= lambda: callLivro(ISBN.get(), Titulo.get(), Autor.get(), anoPulicacao.get(), genero.get()))
    b.place(x=320, y= 10)

def callLivro(ISBN, titulo, autor, ano, genero):
    livro1= livros.Livro(ISBN, titulo, autor, ano, genero )
    livro1.cadastrarLivro()
    operacaoConcluida()


def removerLivros():
    clear_widgets()
    label=ttk.Label(root, text='        Qual livro deseja remover?', font= ('Roboto', 15))
    label.pack( pady=20)
    menu_button(telaLivros)
    label=ttk.Label(root, text='Clique na setinha e escolha a opção a ser removida:', font= ('Roboto', 10))
    label.pack( pady=20)
    ISBN=ttk.Combobox(root,bootstyle="info", font=("Helvetica", 15), values= dataList('livros'))
    ISBN.pack (pady = 5)
    b=ttk.Button(root, text='confirmar', style='success.TButton', command= lambda: callrl(ISBN.get()))
    b.pack(pady = 10)

def callrl(x):
    elementos = x.split(' - ')
    ISBN= elementos[0]
    livro= livros.Livro(ISBN, 'teste', 'teste', 2005, 'teste')
    livro.deletarLivro()
    operacaoConcluida()

def telaMembros():
    root.geometry('400x350')
    clear_widgets()
    menu_button(mainMenu)
    label=ttk.Label(root, text='Escolha uma opção:', font= ('Roboto', 15))
    label.pack(padx= 30, pady=20)
    createButton('Consultar membros', 10, consutarMembros)
    createButton('Cadastrar membros', 10, addMembro)
    createButton('Remover membros', 10, removerMembros)

def addMembro():
    clear_widgets()
    root.geometry('400x350')
    menu_button(telaMembros)

    label=ttk.Label(root, text='Após preencher clique:', font= ('Roboto', 15))
    label.pack(padx= 30, pady=10)

    label=ttk.Label(root, text='ID:', font= ('Roboto', 10))
    label.pack(pady=2)
    ID= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    ID.pack(pady=2)

    label2=ttk.Label(root, text='Nome:', font= ('Roboto', 10))
    label2.pack(pady=2)
    nome= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    nome.pack(pady=2)

    label3=ttk.Label(root, text='Data de nascimento:', font= ('Roboto', 10))
    label3.pack(pady=2)
    dataDeNascimento= ttk.DateEntry(root, style= 'light.Outline.TButton', width=15)
    dataDeNascimento.pack(pady=2)

    label4=ttk.Label(root, text='Endereço', font= ('Roboto', 10))
    label4.pack(pady=2)
    endereco= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    endereco.pack(pady=2)

    b=ttk.Button(root, text='confirmar', style='success.TButton', command= lambda: callMembro(ID.get(), nome.get(), dataDeNascimento.entry.get(), endereco.get()))
    b.place(x=320, y= 10)

def callMembro(ID, nome, dataDeNascimento, endereco):
    print (ID, nome, dataDeNascimento, endereco)
    membro= membros.membro(ID, nome, dataDeNascimento, endereco)
    membro.cadastrarMembro()
    operacaoConcluida()

def consutarMembros():
    clear_widgets()
    root.geometry('600x350')
    label=ttk.Label(root, text='              Verifique a sua tabela a baixo:', font= ('Roboto', 15))
    label.pack( pady=5)
   
    menu_button(telaMembros)
    colors = root.style.colors
    columns = [
        {"text": "ID", "stretch": True},
        {"text": "Nome", "stretch": True},
        {"text": "Data_de_nascimento", "stretch": True},
        {"text": "Endereço", "stretch": True}
    ]

    row_data = logicadeNegocio.select('membros')
    table = Tableview(
        master=root,
        coldata=columns,
        rowdata=row_data,
        paginated=True,
        autofit=True,
        searchable=True,
        bootstyle=INFO,
        stripecolor=(colors.light)
    )

    table.pack(fill=BOTH, expand=YES, padx=10, pady=10)


def removerMembros():
    clear_widgets()
    label=ttk.Label(root, text='        Qual membro deseja remover?', font= ('Roboto', 15))
    label.pack( pady=20)
    menu_button(telaMembros)
    label=ttk.Label(root, text='Clique na setinha e escolha a opção a ser removida:', font= ('Roboto', 10))
    label.pack( pady=20)
    ID=ttk.Combobox(root,bootstyle="info", font=("Helvetica", 15), values= dataList('membros'))
    ID.pack (pady = 5)
    b=ttk.Button(root, text='confirmar', style='success.TButton', command= lambda: callrm(ID.get()))
    b.pack(pady = 10)


def callrm(x):
    elementos = x.split(' - ')
    ID= elementos[0]
    membro= membros.membro(ID, 'teste', 'teste', 2005)
    membro.deletarMembro()
    operacaoConcluida()


def telaEmprestimo():
    clear_widgets()
    menu_button(mainMenu)
    root.geometry('400x350')
    label=ttk.Label(root, text='Escolha uma opção:', font= ('Helvetica', 15))
    label.pack(padx= 30, pady=20)
    createButton('Consultar emprestimo', 10, consultarEmprestimo)
    createButton('Registrar emprestimo', 10, addEmprestimo)
    createButton('Devolução livros', 10, controle)
    createButton('Livros disponiveis', 10, controle)


def consultarEmprestimo():
    clear_widgets()
    root.geometry('600x350')
    label=ttk.Label(root, text='              Verifique a sua tabela a baixo:', font= ('Roboto', 15))
    label.pack( pady=5)
   
    menu_button(telaEmprestimo)
    colors = root.style.colors
    columns = [
        {"text": "ISBN", "stretch": True},
        {"text": "TITULO", "stretch": True},
        {"text": "Membro", "stretch": True},
        {"text": "Data do emprestimo", "stretch": True},
        {"text": "Data da devolução", "stretch": True}
    ]

    row_data = logicadeNegocio.select('emprestimos')
    table = Tableview(
        master=root,
        coldata=columns,
        rowdata=row_data,
        paginated=True,
        autofit=True,
        searchable=True,
        bootstyle=INFO,
        stripecolor=(colors.light)
    )

    table.pack(fill=BOTH, expand=YES, padx=10, pady=10)


def addEmprestimo():
    clear_widgets()
    menu_button(telaEmprestimo)
    root.geometry('400x350')

    label=ttk.Label(root, text='Após preencher clique:', font= ('Roboto', 15))
    label.pack(padx= 30, pady=10)

    label=ttk.Label(root, text='ISBN:', font= ('Roboto', 10))
    label.pack(pady=2)
    ISBN= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    ISBN.pack(pady=2)

    label2=ttk.Label(root, text='Titulo:', font= ('Roboto', 10))
    label2.pack(pady=2)
    Titulo= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    Titulo.pack(pady=2)

    label3=ttk.Label(root, text='Membro:', font= ('Roboto', 10))
    label3.pack(pady=2)
    membro= ttk.Entry(root, style= 'light.Outline.TButton', width=18)
    membro.pack(pady=2)

    label4=ttk.Label(root, text='Data emprestimo', font= ('Roboto', 10))
    label4.pack(pady=2)
    dataEmprestimo= ttk.DateEntry(root, style= 'light.Outline.TButton', width=15)
    dataEmprestimo.pack(pady=2)

    label5=ttk.Label(root, text='Data devolução:', font= ('Roboto', 10))
    label5.pack(pady=2)
    dataDevolucao= ttk.DateEntry(root, style= 'light.Outline.TButton', width=15)
    dataDevolucao.pack(pady=2)

    b=ttk.Button(root, text='confirmar', style='success.TButton')
    b.place(x=320, y= 10)


def mainMenu():
    clear_widgets()
    root.geometry('400x350')
    label=ttk.Label(root, text='Escolha uma opção:', font= ('Helvetica', 15))
    label.pack(padx= 30, pady=20)
    createButton('Livros', 10, telaLivros)
    createButton('Membros', 10, telaMembros)
    createButton('Emprestimos', 10, telaEmprestimo)



mainMenu()
root.mainloop()