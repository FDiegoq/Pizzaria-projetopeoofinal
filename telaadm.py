from tkinter import*
from comprar import*
class telaadm(comprar):
    def __init__(self):

        self.tela=Toplevel(background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200

        self.titulo=Label(self.tela,text="Espaço administrativo",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","bold")
        self.titulo.pack()

        self.mudarpizza=Button(self.tela,text="Adicionar usuário",background="#B50011",foreground="white")
        self.mudarpizza["font"]=("Times new Roman","10","bold")
        self.mudarpizza.config(width=100)
        self.mudarpizza["command"]#= apagar_pizza()
        self.mudarpizza.pack()

        self.mudarpizza=Button(self.tela,text="Apagar usuário",background="#B50011",foreground="white")
        self.mudarpizza["font"]=("Times new Roman","10","bold")
        self.mudarpizza.config(width=100)
        self.mudarpizza["command"]#= adicionar_pizza()
        self.mudarpizza.pack()

        