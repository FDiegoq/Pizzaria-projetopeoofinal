from tkinter import*
from comprar import*
from telaadm import*
from telalogin import*
class janela:
    def __init__(self,master):

        self.tela=Frame(master,background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200
        self.tela.pack()

        self.titulo=Label(self.tela,text="COMPRE SUA PIZZA AQUI!",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","italic","bold")
        self.titulo.pack()

        self.comprar=Button(self.tela,text="COMPRAR",background="#B50011",foreground="white")
        self.comprar["font"]=("Times new Roman","10","bold")
        self.comprar.config(width=100)
        self.comprar["command"]= telalogin
        self.comprar.pack()

        self.botao_abriradm=Button(self.tela,text="ADICIONAR PIZZA AO CARDÁPIO",background="#B50011",foreground="white")
        self.botao_abriradm["font"]=("Times new Roman","10","bold")
        self.botao_abriradm.config(width=100)
        self.botao_abriradm["command"]= telaadm
        self.botao_abriradm.pack()

        self.botao_fechar=Button(self.tela,text="FECHAR",background="#90A74C",foreground="white")
        self.botao_fechar["font"]=("Times new Roman","10","bold")
        self.botao_fechar.config(width=100)
        self.botao_fechar["command"]= janelinha.destroy
        self.botao_fechar.pack()

janelinha=Tk()
janela(janelinha)
janelinha.mainloop()