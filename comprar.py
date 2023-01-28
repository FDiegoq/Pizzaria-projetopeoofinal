from tkinter import*
import pickle
class comprar:
    def __init__(self):
        
        self.pizzas=["(1).Pizza de carne-R$ 33","(2).Pizza de Queijo-R$ 32","(3).Pizza de Frango-R$ 34","(4).Pizza de Calabresa-R$ 30","(5).Pizza Americana-R$ 32","(6).Pizza de Chocolate-R$ 30"]

        self.tela=Toplevel(master=None,background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200

        self.titulo=Label(self.tela,text="CARDAPIO PIZZAS FEITAS",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","italic","bold")
        self.titulo.pack()

        for x in range(6):
               self.cardapio1=Label(self.tela,text=self.pizzas[x],background="#781F25",foreground="white",bd=2,relief="solid")
               self.cardapio1["font"]=("Times new Roman","15","bold")
               self.cardapio1.pack()

        self.pizzas=Label(self.tela,text="Digite o número da pizza desejada",background="#781F25",foreground="white")
        self.pizzas["font"]=("Times new Roman","15","bold")
        self.pizzas.pack()

        self.entradapizzas=Entry(self.tela,background="#FF6347")
        self.entradapizzas.config(width=40)
        self.entradapizzas.pack()

        self.botao_comprar=Button(self.tela,text="COMPRAR",background="#B50011",foreground="white")
        self.botao_comprar["font"]=("Times new Roman","10","bold")
        self.botao_comprar.config(width=40)
        self.botao_comprar["command"]=self.comprar_pizza()
        self.botao_comprar.pack()

        self.botao_fechar=Button(self.tela,text="FECHAR",background="#90A74C",foreground="white")
        self.botao_fechar["font"]=("Times new Roman","10","bold")
        self.botao_fechar.config(width=40)
        self.botao_fechar["command"]= self.tela.destroy
        self.botao_fechar.pack()

        self.mensagem=Label(self.tela,text="",background="#781F25",foreground="white")
        self.mensagem["font"]=("Times new Roman","10","bold")
        self.mensagem.pack()

    def comprar_pizza(self):
        pizza=self.entradapizzas.get()
        if pizza==1:
            self.mensagem["text"]=("Você comprou {}").format(self.pizzas[0])
        if pizza==2:
            self.mensagem["text"]=("Você comprou {}").format(self.pizzas[1])
        if pizza==3:
            self.mensagem["text"]=("Você comprou {}").format(self.pizzas[2])
        if pizza==4:
            self.mensagem["text"]=("Você comprou {}").format(self.pizzas[3])
        if pizza==5:
            self.mensagem["text"]=("Você comprou {}").format(self.pizzas[4])
        if pizza==6:
            self.mensagem["text"]=("Você comprou {}").format(self.pizzas[5])

            
            
