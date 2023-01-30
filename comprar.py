from tkinter import*
from tkinter import ttk
from pickle import*
class comprar:
    def __init__(self):
        
        self.tela=Toplevel(background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200

        self.titulo=Label(self.tela,text="CARDAPIO PIZZAS FEITAS",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","italic","bold")
        self.titulo.pack()

        self.tabela = ttk.Treeview(self.tela, column=("c1", "c2"), show='headings', height=8)
        self.tabela.column("# 1", anchor=CENTER)
        self.tabela.heading("# 1", text="Pizza")
        self.tabela.column("# 2", anchor=CENTER)
        self.tabela.heading("# 2", text="Preço")
        self.tabela.pack()



        self.botao_comprar=Button(self.tela,text="COMPRAR",background="#B50011",foreground="white")
        self.botao_comprar["font"]=("Times new Roman","10","bold")
        self.botao_comprar.config(width=40)
        self.botao_comprar["command"]#self.comprar
        self.botao_comprar.pack()

        self.botao_fechar=Button(self.tela,text="FECHAR",background="#90A74C",foreground="white")
        self.botao_fechar["font"]=("Times new Roman","10","bold")
        self.botao_fechar.config(width=40)
        self.botao_fechar["command"]= self.tela.destroy
        self.botao_fechar.pack()



        #self.mensagem=Label(self.tela,text="",background="#781F25",foreground="white")
        #self.mensagem["font"]=("Times new Roman","18","bold")
        #self.mensagem.pack()
