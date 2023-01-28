from tkinter import*
class comprar:
    def __init__(self):
        
        self.dict={
                   "pizza de carne": 33,
                   "pizza de Queijo": 32,
                   "pizza de Frango": 34,
                   "pizza de calabresa":30,
                   "pizza mista": 32,
                   "pizza de Chocolate": 30 
                   }
        
        self.tela=Toplevel(master=None,background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200

        self.titulo=Label(self.tela,text="CARDAPIO PIZZAS FEITAS",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","italic","bold")
        self.titulo.pack()

        for pizza, preco in self.dict.items():
               self.cardapio1=Label(self.tela,text="{0}---R${1}".format(pizza,preco),background="#781F25",foreground="white",bd=2,relief="solid")
               self.cardapio1["font"]=("Times new Roman","15","bold")
               self.cardapio1.pack()

        self.pizzas=Label(self.tela,text="Digite a pizza que você deseja:",background="#781F25",foreground="white")
        self.pizzas["font"]=("Times new Roman","15","bold")
        self.pizzas.pack()

        self.entradapizzas=Entry(self.tela,background="#FF6347")#.lower()
        self.entradapizzas.lower()
        self.entradapizzas.config(width=48)
        self.entradapizzas.pack()

        self.botao_comprar=Button(self.tela,text="COMPRAR",background="#B50011",foreground="white")
        self.botao_comprar["font"]=("Times new Roman","10","bold")
        self.botao_comprar.config(width=40)
        self.botao_comprar["command"]= self.comprar
        self.botao_comprar.pack()

        self.botao_fechar=Button(self.tela,text="FECHAR",background="#90A74C",foreground="white")
        self.botao_fechar["font"]=("Times new Roman","10","bold")
        self.botao_fechar.config(width=40)
        self.botao_fechar["command"]= self.tela.destroy
        self.botao_fechar.pack()

        self.mensagem=Label(self.tela,text="",background="#781F25",foreground="white")
        self.mensagem["font"]=("Times new Roman","18","bold")
        self.mensagem.pack()

    def comprar(self):
        if self.entradapizzas.get() in self.dict:
            self.mensagem["text"]=("Você comprou:{}").format(self.entradapizzas.get())
        else:
            self.mensagem["text"]=("A pizza não está em nosso cardápio")