from tkinter import*
from telaadm import*
class telaloginadm:
    def __init__(self):

        self.tela=Toplevel(background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200

        self.titulo=Label(self.tela,text="FAÇA LOGIN!",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","bold")
        self.titulo.pack()

        self.nome=Label(self.tela,text="Nome:",background="#781F25",foreground="white")
        self.nome["font"]=("Times new Roman","10","bold")
        self.nome.pack()

        self.entradanome=Entry(self.tela)
        self.entradanome.pack()

        self.nome=Label(self.tela,text="Senha:",background="#781F25",foreground="white")
        self.nome["font"]=("Times new Roman","10","bold")
        self.nome.pack()

        self.entradasenha=Entry(self.tela)
        self.entradasenha.pack()

        self.botaologin=Button(self.tela,text="ENTRAR",background="#B50011",foreground="white")
        self.botaologin["font"]=("Times new Roman","10","bold")
        self.botaologin.config(width=15)
        self.botaologin["command"]= self.entrar
        self.botaologin.pack()

        self.botao_fechar=Button(self.tela,text="FECHAR",background="#90A74C",foreground="white")
        self.botao_fechar["font"]=("Times new Roman","10","bold")
        self.botao_fechar.config(width=15)
        self.botao_fechar["command"]= self.tela.destroy
        self.botao_fechar.pack()

        self.testelogin=Label(self.tela,text="",background="#781F25",foreground="white")
        self.testelogin["font"]=("Times new Roman","10","bold")
        self.testelogin.pack()

    def entrar(self):
        nome=self.entradanome.get()
        senha=self.entradasenha.get()
        if nome=="Diego" and senha=="12345":
            self.testelogin["text"]=("Você logou...")
            telaadm
        else:
            self.testelogin["text"]=("Erro!")

